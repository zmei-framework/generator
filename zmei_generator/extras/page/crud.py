import re
from copy import copy

from zmei_generator.config.domain.collection_set_def import CollectionSetDef
from zmei_generator.config.domain.page_def import PageDef
from zmei_generator.config.extras import PageExtra
from zmei_generator.parser.gen.ZmeiLangParser import ZmeiLangParser
from zmei_generator.parser.utils import BaseListener

from zmei_generator.config.domain.exceptions import ValidationException
from zmei_generator.config.domain.page_expression import PageExpression
from zmei_generator.extras.page.auth import add_page_auth
from zmei_generator.extras.page.block import PageBlock, InlineTemplatePageBlock, InlineFilePageBlock, \
    ThemeFileIncludePageBlock


class CrudBasePageExtraParserListener(BaseListener):

    def __init__(self, collection_set: CollectionSetDef) -> None:
        super().__init__(collection_set)

        self.crud = None

    def extra_start(self, cls):
        extra = cls(self.page)
        self.collection_set.extras.append(
            extra
        )
        self.collection_set.crud = True
        self.crud = extra

    def extra_end(self, cls):
        self.crud = None

    # Params

    def enterAn_crud_target_model(self, ctx: ZmeiLangParser.An_crud_target_modelContext):
        self.crud.params.model = ctx.getText().strip()


class CrudPageExtraParserListener(CrudBasePageExtraParserListener):

    def enterAn_crud(self, ctx: ZmeiLangParser.An_crudContext):
        self.extra_start(CrudPageExtra)

    def exitAn_crud(self, ctx: ZmeiLangParser.An_crudContext):
        self.extra_end(CrudPageExtra)


class CrudParams(object):
    def __init__(self) -> None:
        self.model = None
        self.filter_expr = None
        self.spec = None
        self.query = None
        self.fields = None
        self.list_fields = None
        self.skip = None
        self.block_name = None
        self.theme = None
        self.url_prefix = None
        self.pk_param = None
        self.object_expr = None
        self.edit_auth = None
        self.item_name = None
        self.link_extra = None
        self.link_suffix = None
        self.next_page = None


class CrudPageExtra(PageExtra):
    @classmethod
    def get_name(cls):
        return 'crud'

    link_extra = None
    link_extra_params = None
    name_prefix = None
    name_suffix = None
    block_name = None
    theme = 'default'
    url_prefix = None
    pk_param = None
    crud_pages = None
    app_name = None
    model_cls = None
    fields = None
    list_fields = None
    formatted_query = None
    context_object_name = None
    object_expr = None
    edit_auth = None
    query = None
    next_page_expr = None
    item_name = None
    field_filters = None
    create_list = True
    link_suffix = ''

    def __init__(self, page, params=None, descriptor=None):
        super().__init__(page)

        self.params = params or CrudParams()

        self.descriptor = descriptor

        if page.defined_uri is None:
            raise ValidationException('@crud annotations require page to have url')

    def post_process(self):
        if self.descriptor not in self.page.cruds:
            self.page.cruds[self.descriptor or '_'] = {}

        self.page.cruds[self.descriptor or '_'][self.get_name()] = self

        self.prepare_environment(self.params, self.page)

        self.build_pages(self.page)

    def prepare_environment(self, crud, page):
        # next page
        if crud.next_page:
            self.next_page_expr = f"return reverse({crud.next_page})" + self.link_suffix
        else:
            self.next_page_expr = f"return self.request.get_full_path()" + self.link_suffix

        self.field_filters = {}
        if crud.fields:
            all_fields = []
            for field in crud.fields:
                all_fields.append(field.spec)
                if field.filter_expr and not field.spec.startswith('^'):
                    self.field_filters[field.spec] = field.filter_expr

            crud.fields = all_fields

        # appname, model_cls, fields
        if crud.model.startswith('#'):
            self.app_name = page.collection_set.app_name + '.models'
            collection = page.collection_set.collections[crud.model[1:]]
            self.model_cls = collection.class_name
            self.fields = {field.name: field.verbose_name or field.name.replace('_', ' ').capitalize() for field in
                           collection.filter_fields(crud.fields or '*') if not field.read_only}
            self.list_fields = {field.name: field.verbose_name or field.name.replace('_', ' ').capitalize() for field in
                                collection.filter_fields(crud.list_fields or crud.fields or '*') if not field.read_only}
        else:
            parts = crud.model.split('.')
            self.app_name = '.'.join(parts[:-1]) + '.models'
            self.model_cls = parts[-1]
            self.fields = {field: field.replace('_', ' ').capitalize() for field in crud.fields}
            self.list_fields = {field: field.replace('_', ' ').capitalize() for field in
                                crud.list_fields} or crud.fields
            if not self.fields:
                raise ValidationException('@crud -> fields for external models are required: {}'.format(crud.model))

        # link extra
        if crud.link_extra:
            self.link_extra = crud.link_extra
            link_extra_params = []
            for item in re.split('\s+', self.link_extra):
                key, val = item.split('=')
                link_extra_params.append(f"'{key}': {val}")
            self.link_extra_params = ', '.join(link_extra_params)
        else:
            self.link_extra = ''
            self.link_extra_params = ''

        if crud.link_suffix:
            self.link_suffix = crud.link_suffix

        # name_prefix
        if self.descriptor:
            self.name_prefix = f'{self.descriptor}_'
            self.name_suffix = f'_{self.descriptor}'
        else:
            self.name_prefix = ''
            self.name_suffix = ''

        # item name
        if crud.item_name:
            self.context_object_name = crud.item_name
        else:
            self.context_object_name = self.name_prefix + 'item'

        # block name
        if crud.block_name:
            self.block_name = crud.block_name
        elif self.descriptor:
            self.block_name = f'{self.descriptor}_content'
        else:
            self.block_name = 'content'

        # crud theme
        if crud.theme:
            self.theme = crud.theme

        # url prefix
        if crud.url_prefix:
            self.url_prefix = crud.url_prefix
            if not self.url_prefix.endswith('/'):
                self.url_prefix = self.url_prefix + '/'
        elif self.descriptor:
            self.url_prefix = f'{self.descriptor}/'
        else:
            self.url_prefix = ''
        if not page.defined_uri.endswith('/'):
            self.url_prefix = '/' + self.url_prefix

        # pk
        if crud.pk_param:
            self.pk_param = crud.pk_param
        elif self.descriptor:
            self.pk_param = f'{self.descriptor}_pk'
        else:
            self.pk_param = 'pk'

        # object
        if crud.object_expr:
            self.object_expr = 'self.object = ' + crud.object_expr
        else:
            self.object_expr = 'self.object = self.get_object()'

        # auth
        if crud.edit_auth:
            self.edit_auth = crud.edit_auth

        # formated_query
        if self.query:
            self.query = crud.query.strip()
            self.formatted_query = '.filter({})'.format(self.query)
        else:
            self.formatted_query = '.all()'

        if crud.skip:
            self.create_list = 'list' not in list(crud.skip)
        else:
            self.create_list = True

        # pages that are not needed
        self.crud_pages = [
            x for x in ['detail', 'create', 'edit', 'delete'] if x not in list(crud.skip or [])
        ]

    def prepare_block_fields(self, page):
        link_extra = self.link_extra
        if link_extra:
            link_extra = ' ' + link_extra

        # edit_auth = self.edit_auth or None
        edit_auth = None
        if edit_auth:
            edit_auth = edit_auth.strip()
            if len(edit_auth) == 0:
                edit_auth = None

            if edit_auth.startswith('data'):
                edit_auth = edit_auth[5:]

        ctx = {
            'link_suffix': repr(self.link_suffix),
            'can_edit': repr(edit_auth or True),
            'fields': repr(self.fields),
            'list_fields': repr(self.list_fields),
            # 'meta': f'{self.name_prefix}{self.item_name}_meta',
            # 'item': repr(f"{self.context_object_name}"),
            # 'items': repr(f"{self.context_object_name}_list"),
            'pk_param': repr(self.pk_param),
            'context_object_name': repr(self.context_object_name),
            'by_id': repr(f"{self.pk_param}={self.context_object_name}.pk"),
            'crud_prefix': repr(str(self.name_prefix)),
        }

        if page:
            links = {f'crud_{x}_link': repr(f"{page.collection_set.app_name}.{page.name}{self.name_suffix}_{x}") for
                     x in
                     self.crud_pages}
            links['crud_list_link'] = repr(f"{page.collection_set.app_name}.{page.name}")

            ctx.update(links)

        return ctx

    def build_pages(self, page):

        if self.create_list:
            page.imports.append(
                (self.app_name, self.model_cls)
            )

            page.page_items[f'meta'] = PageExpression(
                f'meta', f"{self.model_cls}._meta", page)

            # page.page_items[f'_{self.context_object_name}_list'] = PageExpression(
            #     f'{self.context_object_name}_list', f"{se

            page.page_items[f'_items'] = PageExpression(
                f'items', f"{self.model_cls}.objects{self.formatted_query}", page)

            page.add_block(
                self.block_name,

                ThemeFileIncludePageBlock(page, "theme/crud_list.html", "list.html", ns='crud', theme=self.theme)
            )

            for key, val in self.prepare_block_fields(page).items():
                page.page_items[key] = PageExpression(key, val, page)

        for crud_page in self.crud_pages:

            new_page = PageDef(self.page.collection_set)
            new_page.extra_bases = []
            new_page.parent_name = page.name
            new_page.name = f"{page.name}{self.name_suffix}_{crud_page}"
            new_page.url_alias = new_page.name

            if crud_page == 'create':
                new_page.set_uri(f"{page.defined_uri}{self.url_prefix}{crud_page}")
            else:
                new_page.set_uri(f"{page.defined_uri}{self.url_prefix}<{self.pk_param}>/{crud_page}")

            params = copy(self.params)
            params.next_page = f"'{page.collection_set.app_name}.{page.name}', kwargs={{{self.link_extra_params}}}"

            crud = crud_cls_by_name(crud_page)(new_page, params=params, descriptor=self.descriptor)

            page.collection_set.pages[new_page.name] = new_page
            page.collection_set.extras.append(crud)
            page.children.append(new_page)


def crud_cls_by_name(name):
    from zmei_generator.extras.page.crud_create import CrudCreatePageExtra
    from zmei_generator.extras.page.crud_delete import CrudDeletePageExtra
    from zmei_generator.extras.page.crud_detail import CrudDetailPageExtra
    from zmei_generator.extras.page.crud_edit import CrudEditPageExtra

    return dict((
        ("create", CrudCreatePageExtra),
        ("delete", CrudDeletePageExtra),
        ("detail", CrudDetailPageExtra),
        ("edit", CrudEditPageExtra),
    ))[name]


class BaseCrudSubpageExtra(CrudPageExtra):
    crud_page = None

    def build_pages(self, page):
        page.imports.append(
            (self.app_name, self.model_cls)
        )

        page.add_block(
            self.block_name,

            ThemeFileIncludePageBlock(page, f"theme/crud_{self.crud_page}.html", f"{self.crud_page}.html", ns='crud', theme=self.theme)
        )

        for key, val in self.prepare_block_fields(page.get_parent()).items():
            page.page_items[key] = PageExpression(key, val, page.get_parent())

        if self.crud_page == 'detail':
            page.imports.append(
                ('django.views.generic.detail', self.get_view_class_name())
            )
        else:
            page.imports.append(
                ('django.views.generic.edit', self.get_view_class_name())
            )

        if self.crud_page in ('edit', 'create') and len(self.field_filters):
            code = "form = super().get_form(*args, **kwargs)\n"

            for name, expr in self.field_filters.items():
                code += "form.fields['{}'].queryset = {}\n".format(name, expr)
            code += "return form\n"

            page.methods['get_form'] = code

        if self.crud_page in ('edit', 'delete', 'create', 'detail'):
            page.imports.append(('django.urls', 'reverse'))
            page.options['pk_url_kwarg'] = f"'{self.pk_param}'"
            page.methods['get_success_url'] = self.next_page_expr

        if self.crud_page in ('edit', 'delete', 'create'):
            if self.edit_auth:
                add_page_auth(self.edit_auth, page)

        if self.crud_page in ('edit', 'delete', 'create', 'detail'):
            page.methods['get_queryset'] = "return " + self.model_cls + ".objects" + self.formatted_query
            page.options['model'] = self.model_cls
            page.options['context_object_name'] = f"'{self.context_object_name}'"

        if self.crud_page in ('edit', 'create'):
            page.options['fields'] = repr([key for key, val in self.fields.items()])

        if self.crud_page in ('edit', 'delete', 'detail'):
            page.methods['get'] = self.object_expr + "\nreturn super().get(self.request, *args, **kwargs)"
            page.methods['post'] = self.object_expr + "\nreturn super().post(self.request, *args, **kwargs)"
            if 'get_object()' not in self.object_expr:
                page.methods['get_object'] = self.object_expr + "\nreturn self.object"

        if self.crud_page in ('create',):
            page.methods['get'] = \
                "self.object = None\nreturn super().get(self.request, *args, **kwargs)"

            page.methods['get_initial'] = f"self.object = {self.model_cls}({self.query})\nreturn super().get_initial()"

        page.extra_bases.append(self.get_view_class_name())

    def get_view_class_name(self):
        if self.crud_page == 'edit':
            return 'UpdateView'
        else:
            return '{}View'.format(self.crud_page.capitalize())
