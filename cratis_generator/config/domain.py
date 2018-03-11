from copy import copy

import re

from abc import abstractmethod, abstractproperty
from collections import namedtuple

import sys
from cratis_generator.config.grammar import page as page_parser
from cratis_generator.generator.utils import StopGenerator, handle_parse_exception
from pyparsing import ParseException
from termcolor import colored
from typing import List, Dict


class ValidationException(Exception):
    pass


class PageExtra(object):

    def __init__(self, parsed_result, page):
        self.page = page

    @property
    def has_python_code(self):
        return False

    def get_imports(self):
        return []

    def get_python_code(self):
        return ''

    @abstractmethod
    def parse(self, extra, collection):
        pass

    def post_process(self):
        pass


class PageDef(object):
    def __init__(self, parse_result, collection_set) -> None:
        super().__init__()

        self.raw_ = parse_result

        """:type: CollectionSetDef"""
        self.collection_set = collection_set

        self.rss = None

        self.extra_bases = []

        self.name = parse_result.page_name
        self.url_alias = parse_result.url_alias or self.name
        self.parent_name = parse_result.parent_name
        self.parsed_template_name = parse_result.template_name
        self.parsed_template_expr = parse_result.template_expr
        self.page_code = '\n'.join([x.strip() for x in parse_result.page_code.split('\n')])

        # error handler for:
        self.handlers = []

        self.allow_post = False

        if self.parent_name and self.parent_name not in self.collection_set.pages:
            raise ValidationException('Parent "{}" for page "{}" does not exist'.format(self.parent_name, self.name))

        self.uri_params = []

        self.children = []

        self.imports = []

        self.options = {}
        self.methods = {}
        self.blocks = {}


        def find_params(match):
            param = match.group(1)
            expr = match.group(3) or '[^\/]+'

            self.uri_params.append(param)
            return '(?P<{}>{})'.format(param, expr)

        uri = parse_result.uri
        self.defined_uri = uri
        self.has_uri = bool(uri)

        self.i18n = False

        if uri.startswith('$'):
            uri = uri[1:]
            self.i18n = True


        self.uri = re.sub(r'<(\w+)(\s*:\s*([^\>]+))?>', find_params, uri)

        self.page_items = {x.key: PageExpression(x.key, x.expression, self) for x in parse_result.page_items}
        if 'sitemap' in self.page_items:
            self.sitemap_expr = self.page_items.pop('sitemap')
        else:
            self.sitemap_expr = None

        extras = self.collection_set.parser.get_page_extras_available()

        self.extras = []
        for extra in parse_result.extras:

            try:
                extra_cls = extras[extra.extra_name]
                try:
                    extra_instance = extra_cls(extra, self)
                    self.extras.append(extra_instance)

                except ParseException as e:
                    handle_parse_exception(e, extra.extra_body,
                                           '@{} expression for page "{}"'.format(extra.extra_name, self.name))
            except KeyError as e:
                raise ValidationException('Extra not found: {}, reason: {}'.format(extra.extra_name, e))

    @property
    def page_item_names(self):
        return list(self.page_items.keys())

    @property
    def parent_view_name(self):
        if not self.parent_name:
            return 'TemplateView'

        return self.collection_set.pages[self.parent_name].view_name

    def get_imports(self):
        return self.imports

    @property
    def has_sitemap(self):
        return self.sitemap_expr is not None

    @property
    def view_name(self):
        return '{}View'.format(''.join([x.capitalize() for x in self.name.split('_')]))

    @property
    def urls_line(self):

        uri = self.uri[1:] if self.uri.startswith('/') else self.uri
        return '^{}$'.format(uri)


    def render_method_headers(self, use_data=False, use_parent=False, use_url=False, use_request=False):
        code = ""
        if use_data:
            code += "data = super().get_context_data(**self.kwargs)\n"
        if use_parent:
            code += "parent = type('parent', (object,), data)\n"
        if use_request:
            code += "request = self.request\n"
        if use_url:
            code += "url = type('url', (object,), self.kwargs)\n"

        if len(code) > 0:
            code += "\n"

        return code

    def render_page_code(self):

        code = ""

        for key, item in self.page_items.items():
            if not item.or_404:
                code += key + " = " + item.render_python_code() + "\n"
            else:
                code += "try:\n"
                code += "   " + key + " = " + item.render_python_code() + "\n"
                code += "except ObjectDoesNotExist:\n"
                code += "   raise Http404\n"

        code += self.page_code

        code = self.render_method_headers(
            use_data=False,
            use_parent='parent' in code,
            use_request='request' in code,
            use_url='url' in code,
        ) + code

        if len(code.strip()) == 0:
            return ''

        return code

    @property
    def defined_template_name(self):
        """
        Returns name of template if it is not an expression
        """
        if self.parsed_template_expr:
            return None
        elif self.parsed_template_name:
            return '{}'.format(self.parsed_template_name)
        else:
            return '{}/{}.html'.format(self.collection_set.app_name, self.name)

    def render_template_name_expr(self):

        if self.parsed_template_expr:
            code = self.parsed_template_expr
        else:
            code = '"{tpl}"'.format(tpl=self.defined_template_name)

        code = self.render_method_headers(
            use_data='data' in code,
            use_parent='parent' in code,
            use_request='request' in code,
            use_url='url' in code,
        ) + 'return [' + code + ']\n'

        return code

    def render_method_expr(self, method_code):
        code = method_code

        code = self.render_method_headers(
            use_data='data' in code,
            use_parent='parent' in code,
            use_request='request' in code,
            use_url='url' in code,
        ) + code + '\n'

        return code



class PageExpression(object):
    def __init__(self, key, expression, page: PageDef) -> None:
        self.expression = expression
        self.page = page
        self.key = key

        self.or_404 = False

        self.cache_type = None
        self.cache_expr = None

        if '@cached_as' in self.expression:
            self.cache_type = 'cached_as'
        elif '@cached' in self.expression:
            self.cache_type = 'cached'

        if self.cache_type:
            self.expression, self.cache_expr = self.expression.split('@' + self.cache_type)

            self.expression = self.expression.strip()
            self.cache_expr = self.cache_expr.strip()

            if self.cache_expr == '':
                self.cache_expr = '()'

            if not (self.cache_expr.startswith('(') and self.cache_expr.endswith(')')):
                raise ValidationException('Cache expression must be surrounded with () in expression: {}, parsed cache expr: {}'.format(
                    expression,
                    self.cache_expr
                ))

            self.expression = '{me.cache_type}{me.cache_expr}(lambda: {me.expression})'.format(me=self)

        if '@or_404' in self.expression:
            self.expression = self.expression.replace('@or_404', '')
            self.or_404 = True

    def find_collection_by_ref(self, ref):
        try:
            return self.page.collection_set.collections[ref]
        except KeyError:
            raise ValidationException(
                'Can not parese page expression. Collection not found by ref: {} when parsing page: {}\n\n'
                '[..{}..]\n...\n{}: {}\n'.format(
                    '#' + ref,
                    self.page.name,
                    self.page.name,
                    self.key,
                    self.expression.replace('#' + ref, colored('#' + ref, 'white', 'on_red'))
                ))

    def get_imports(self):
        imports = []
        for match in re.findall(r'#(\w+)\.', self.expression):
            col = self.find_collection_by_ref(match)
            imports.append(('{}.models'.format(col.collection_set.app_name), col.class_name))

        if self.or_404:
            imports.append(('django.core.exceptions', 'ObjectDoesNotExist'))
            imports.append(('django.http', 'Http404'))

        if self.cache_type:
            imports.append(('cacheops', self.cache_type))

        if 'get_language(' in self.expression:
            imports.append(('django.utils.translation', 'get_language'))

        if 'thumb(' in self.expression:
            imports.append(('cratis_filer.utils', 'thumb'))

        return imports

    def render_python_code(self):
        def replace_col_names(match):
            return '{}.objects.'.format(self.find_collection_by_ref(match.group(1)).class_name)

        expr = self.expression.strip()
        expr = re.sub(r'#(\w+)\.', replace_col_names, expr)

        def replace_params(match):
            param = match.group(1)

            if param not in self.page.uri_params:
                raise ValidationException(
                    'Can not parese page expression. Parameter not found: #{}'.format(param))

            return "self.kwargs['{}']".format(param)

        expr = re.sub(r'<(\w+)>', replace_params, expr)


        return expr


class CollectionDef(object):
    #
    # ref: str
    # name: str
    # fields: Dict[str, FieldDef]

    # rest: False
    # translatable: False

    def __init__(self, parse_result, collection_set) -> None:
        super().__init__()

        self.raw_ = parse_result

        """:type: CollectionSetDef"""
        self.collection_set = collection_set

        self.ref = parse_result.ref
        self.short_ref = self.ref

        self.name = parse_result.name
        self.name_plural = parse_result.name_plural
        self.to_string = parse_result.to_string

        self.polymorphic = False
        self.parent = False
        self.child_collections = []

        self.mixin_classes = []

        if parse_result.parent:
            if parse_result.parent not in self.collection_set.collections:
                raise ValidationException(
                    'Collection "{}" marked as parent for "{}", but not yet loaded or do not exist.'.format(
                        parse_result.parent, self.ref
                    ))

            if parse_result.parent_separator == '~>':
                self.ref = '{}_{}'.format(parse_result.parent, self.ref)

            self.parent = self.collection_set.collections[parse_result.parent]  # type: CollectionDef
            if self.parent.parent:
                raise ValidationException(
                    'Collection "{}" marked as parent for "{}", but it\'s already has parent. Multilevel polymorphism is not supported yet.'.format(
                        parse_result.parent, self.ref
                    ))
            self.parent.polymorphic = True
            self.parent.child_collections.append(self)

        self.translatable = False
        self.admin = False

        self.tree = False
        self.tree_polymorphic_list = False
        self.sortable = False
        self.sortable_field = None

        if not self.name:
            self.name = ' '.join(self.ref.split('_')).capitalize()

        self.fields = {}
        for field in parse_result.fields:
            if field.calculated_expression or field.calculated_static_expression:
                from cratis_generator.fields.expression import ExpressionFieldDef
                field_cls = ExpressionFieldDef
            else:
                field_cls = self.collection_set.parser.get_field_class(field.type_name)

            self.fields[field.name] = field_cls(self, field)

        self.admin_list = None
        self.admin_js = []
        self.admin_css = []
        self.admin_list_editable = None
        self.admin_list_filter = None
        self.admin_list_search = None
        self.admin_list = None
        self.admin_fields = None
        self.admin_inlines = []
        self.admin_has_polymorphic_inlines = False

        self.admin_tab_fields = {}
        self.admin_tabs = []
        self.tab_names = {}

        self.rest_conf = None
        self.rest_mode = None
        self.rest = False

    def parse_extras(self):

        if self.parent:
            self.admin_tab_fields = self.parent.admin_tab_fields.copy()
            self.admin_tabs = self.parent.admin_tabs.copy()
            self.tab_names = self.parent.tab_names.copy()

            self.translatable = self.parent.translatable or self.translatable

        extras = self.collection_set.parser.get_extras_available()

        for extra in self.raw_.extras:

            try:
                extra_cls = extras[extra.extra_name]
                try:
                    extra_instance = extra_cls()
                    extra_instance.parse(extra, self)

                except ParseException as e:
                    handle_parse_exception(e, extra.extra_body,
                                           '@{} expression for collection "{}"'.format(extra.extra_name, self.name))
            except KeyError as e:
                raise ValidationException('Extra not found: {}, reason: {}'.format(extra.extra_name, e))

    @property
    def model_class_declaration(self):
        classes = []
        if self.parent:
            classes.append(self.parent.class_name)
        elif self.polymorphic:
            if self.tree:
                classes.append('PolymorphicMPTTModel')
            else:
                classes.append('PolymorphicModel')

        elif self.tree:
            classes.append('MPTTModel')

        if not classes:
            classes.append('models.Model')

        return ', '.join(classes)


    @property
    def child_model_classes(self):
        if not self.polymorphic:
            return []

        return [x.class_name for x in self.child_collections]

    @property
    def rest_class(self):
        if self.rest_mode == 'rw':
            return 'rest_framework.viewsets', 'ModelViewSet'
        elif self.rest_mode == 'w':
            return 'cratis_api.views', 'WriteOnlyModelViewSet'
        else:
            return 'rest_framework.viewsets', 'ReadOnlyModelViewSet'

    @property
    def admin_class_declaration(self):
        return ', '.join([x[1] for x in self.admin_classes])

    @property
    def admin_classes(self):
        classes = []

        model_admin_added = False

        if self.admin_has_polymorphic_inlines:
            classes.append(('polymorphic.admin', 'PolymorphicInlineSupportMixin'))

        if self.parent:
            classes.append(('polymorphic.admin', 'PolymorphicChildModelAdmin'))
            model_admin_added = True
        elif self.polymorphic:
            classes.append(('polymorphic.admin', 'PolymorphicParentModelAdmin'))
            model_admin_added = True

        if self.sortable:
            classes.append(('suit.admin', 'SortableModelAdmin'))
            model_admin_added = True

        if self.tree:
            classes.append(('mptt.admin', 'DraggableMPTTAdmin'))
            model_admin_added = True

        if self.translatable:
            classes.append(('cratis_i18n.admin', 'TranslatableModelAdmin'))
            model_admin_added = True

        if not model_admin_added:
            classes.append(('django.contrib.admin', 'ModelAdmin'))

        return classes

    @property
    def admin_inline_classes(self):
        return [x.class_name for x in self.admin_inlines]

    def fields_for_tab(self, tab):
        fields = []
        for name, tab_name in self.admin_tab_fields.items():
            # skip references
            if isinstance(self.all_and_inherited_fields_map[name], ReferenceField):
                continue

            if tab_name == tab:
                fields.append(self.all_and_inherited_fields_map[name])

        return fields

    @property
    def empty_admin(self):
        return not (self.admin_fields or self.admin_list)

    def check_field_exists(self, field_name):
        fields = self.expand_field_pattern(field_name)
        return len(fields) > 0

    def expand_field_pattern(self, field_pattern):
        fields = []

        # if local_only
        if field_pattern.startswith('.'):
            field_pattern = field_pattern[1:]
        else:
            if self.parent:
                fields += self.parent.expand_field_pattern(field_pattern)

        if field_pattern.endswith('*'):
            prefix = field_pattern[:-1]
            for key in self.fields.keys():
                if key.startswith(prefix):
                    fields.append(key)

        elif field_pattern.startswith('*'):
            suffix = field_pattern[1:]
            for key in self.fields.keys():
                if key.endswith(suffix):
                    fields.append(key)

        elif field_pattern in self.fields:
            fields.append(field_pattern)

        return fields

    def filter_fields(self, filter_spec, include_refs=False, field_set=None):
        allow_parents = filter_spec[0] != '.*'

        if not field_set:
            if not include_refs:

                fields = self.own_fields
                if allow_parents and self.parent:
                    fields = tuple(self.parent.own_fields) + tuple(fields)
            else:
                fields = self.fields.values()
                if allow_parents and self.parent:
                    fields = tuple(self.parent.fields.values()) + tuple(fields)
        else:
            fields = field_set

        if filter_spec[0] in ('*', '.*'):
            exclude_list = []
            for item in filter_spec[1:]:
                if item[0] != '^':
                    raise ValidationException(
                        'If * used in field list, then all other fields should start with ^ (exclude)')

                new_fields = self.expand_field_pattern(item[1:])
                if not new_fields:
                    raise ValidationException(
                        'Field name specified for exclude: "{}" does not exist'.format(item[1:]))
                exclude_list += new_fields

            return [field for field in fields if field.name not in exclude_list]

        else:
            inlcude_list = []
            for item in filter_spec:
                if item == '*':
                    raise ValidationException('* maybe used only as first item in field list')
                if item[0] == '^':
                    raise ValidationException('^ maybe used only with * as first item in field list')

                new_fields = self.expand_field_pattern(item)
                if not new_fields:
                    raise ValidationException(
                        'Field name specified for include: "{}" does not exist'.format(item))

                inlcude_list += new_fields

            return [field for field in fields if field.name in inlcude_list]

    @property
    def class_name(self):
        class_name = ''.join([x.capitalize() for x in self.ref.split('_')])

        # if not self.parent:
        return class_name
        # else:
        #     return '{}{}'.format(self.parent.class_name, class_name)

    @property
    def fqdn(self):
        return '.'.join([self.collection_set.app_name, self.class_name])

    @property
    def display_field(self):
        for field in self.fields.values():
            if field.display_field:
                return field

    @property
    def all_fields(self):
        return self.fields.values()

    @property
    def all_and_inherited_fields_map(self):
        if not self.parent:
            return self.fields

        all_fields = {}
        all_fields.update(self.parent.fields)
        all_fields.update(self.fields)
        return all_fields

    @property
    def own_fields(self):
        return [field for field in self.fields.values() if field.type_name not in ['ref']]

    @property
    def expression_fields(self):
        admin_list = [x.slug for x in self.admin_list]
        return [field for field in self.fields.values() if field.type_name == 'expr' and field.slug not in admin_list]

    @property
    def prepopulated_fields(self):
        prepopulated = {}

        for field in self.all_and_inherited_fields_map.values():
            info = field.get_prepopulated_from()
            if info:
                prepopulated[field.name] = info

        return prepopulated

    @property
    def translatable_fields(self):
        return [field for field in self.own_fields if field.translatable]

    @property
    def expression_fields(self):
        from cratis_generator.fields.expression import ExpressionFieldDef
        return [field for field in self.fields.values() if isinstance(field, ExpressionFieldDef)]

    @property
    def read_only_fields(self):
        return [x for x in self.expression_fields if x in self.all_fields]

    @property
    def relation_fields(self):
        from cratis_generator.fields.relation import RelationDef
        return [field for field in self.own_fields if isinstance(field, RelationDef)]


class CollectionSetDef(object):
    # app_name: str
    # collections: Dict[str, CollectionDef]

    rest = False

    # translatable: False

    def __init__(self, parse_result, parser, app_name: str) -> None:
        self.parser = parser
        self.app_name = app_name
        self.translatable = False
        self.admin = False
        self.collections = {}
        self.pages = {}

        self.deps = []
        self._apps = [app_name]

        self.page_imports = parse_result.page_imports
        self.collection_imports = parse_result.collection_imports

        for col in parse_result.collections:
            collection_def = CollectionDef(col, self)
            self.collections[collection_def.ref] = collection_def

        for page in parse_result.pages:
            page_def = PageDef(page, self)
            self.pages[page.page_name] = page_def

            for subpage_raw in page_def.children:
                try:
                    subpage_parsed = page_parser.parseString(subpage_raw, parseAll=True)[0]
                except ParseException as e:
                    handle_parse_exception(e, subpage_raw,
                                           'Page {} auto-generated subpages: {}'.format(page.page_name, e))

                self.pages[subpage_parsed.page_name] = PageDef(subpage_parsed, self)

        for page in self.pages.values():
            for extra in page.extras:
                extra.post_process()

        for col_name, collection in self.collections.items():
            for field_name, field in list(collection.fields.items()):
                try:
                    field.parse_options()
                except ParseException as e:
                    handle_parse_exception(e, field.options,
                                           'Options for "{}"->"{}": {}'.format(col_name, field_name, e))

        for col_name, collection in self.collections.items():
            collection.parse_extras()

    def add_deps(self, deps):
        for dep in deps:
            if dep not in self.deps:
                self.deps.append(dep)

    def add_apps(self, apps):
        for app in apps:
            if app not in self._apps:
                self._apps.append(app)

    @property
    def has_sitemap(self):
        for key, page in self.pages.items():
            if page.has_sitemap:
                return True

        return False

    @property
    def apps(self):
        app_names = self._apps
        return app_names


FieldDeclaration = namedtuple('FieldDeclaration', ['import_def', 'declaration'])


class NoModelField(Exception):
    pass


class ReferenceField(object):
    def __init__(self, collection: CollectionDef, target_collection: CollectionDef, name: str, source_field_name: str) -> None:
        super().__init__()

        self.target_collection = target_collection

        self.type_name = 'ref'
        self.name = name
        self.source_field_name = source_field_name

        self.collection = collection
        self.display_field = False
        self.translatable = False

        self.options = {}

        self.inline = False

    def parse_options(self):
        pass

    def get_model_field(self, collection: CollectionDef):
        raise NoModelField()

    def get_admin_widget(self):
        return None

    def get_prepopulated_from(self):
        return None

    def get_rest_field(self):
        return None

    def get_rest_inline_collection(self):
        return self.target_collection

    @property
    def is_many(self):
        return True

    @property
    def admin_list_renderer(self):
        return None


class FieldDef(object):
    def __init__(self, collection: CollectionDef, field) -> None:
        super().__init__()

        self.type_name = field.type_name
        self.name = field.name
        self.verbose_name = field.verbose_name
        self.help = field.field_help

        self.collection = collection
        self.required = field.required
        self.not_null = field.not_null
        self.unique = field.unique
        self.index = field.index
        self.display_field = field.display_field
        self.translatable = field.translatable
        self.comment = field.comment.strip() if field.comment else None

        self.read_only = False

        self.inline = False

        if self.translatable:
            collection.translatable = True
            collection.collection_set.translatable = True

        self.options = field.type_opts

    def prepare_field_arguemnts(self, own_args=None):
        args = {}

        if self.verbose_name:
            args['verbose_name'] = self.verbose_name

        if self.help:
            args['help_text'] = self.help

        if not self.not_null:
            args['null'] = True

        args['blank'] = not self.required

        if self.unique:
            args['unique'] = True

        if self.index:
            args['db_index'] = True

        if own_args:
            args.update(own_args)

        return args

    def parse_options(self):
        self.options = {}

    def get_model_field(self, collection: CollectionDef):
        raise NotImplementedError('Field "{}" ({}) is not yet implemented.'.format(self.type_name, type(self)))

    def get_admin_widget(self):
        return None

    def get_prepopulated_from(self):
        return None

    def get_rest_field(self):
        return None

    def get_rest_inline_collection(self):
        return None

    @property
    def admin_list_renderer(self):
        return None
