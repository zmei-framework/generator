import re
from copy import copy

from zmei_generator.contrib.web.extensions.page.block import InlineTemplatePageBlock
from zmei_generator.parser.errors import GlobalScopeValidationError as ValidationException, GlobalScopeValidationError
from zmei_generator.domain.page_def import PageDef
from zmei_generator.domain.page_expression import PageExpression
from zmei_generator.domain.extensions import PageExtension


def to_camel_case(name):
    return ''.join([x.capitalize() for x in name.split('_')])


def to_camel_case_decap(name):
    name = ''.join([x.capitalize() for x in name.split('_')])
    return name[0].lower() + name[1:]


def to_camel_case_path(name):
    return '.'.join([to_camel_case_decap(x) for x in name.split('.')])


def format_field_names(names):
    return '{%s}' % ', '.join([f"'{key}': _('{val}')" for key, val in names.items()])


class CrudField(object):
    def __init__(self) -> None:
        self.spec = None
        self.filter_expr = None


class CrudParams(object):
    def __init__(self) -> None:
        self.model = None
        self.filter_expr = None
        self.spec = None
        self.query = None
        self.fields = None
        self.list_fields = None
        self.list_type = 'stacked'
        self.header = True
        self.skip = None
        self.block_name = None
        self.theme = None
        self.url_prefix = None
        self.pk_param = None
        self.object_expr = None
        self.can_edit = None
        self.item_name = None
        self.link_extension = None
        self.link_suffix = None
        self.next_page = {}


class CrudPageExtension(PageExtension):
    crud_page = None

    list_type = None
    header = None
    link_extension = None
    model_name = None
    model_name_plural = None
    link_extension_params = None
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
    can_edit = None
    query = None
    next_page_expr = None
    item_name = None
    items_name = None
    field_filters = None
    create_list = True
    link_suffix = ''

    parent_base_page = None

    @classmethod
    def get_name(cls):
        return 'crud'

    def __init__(self, page, params=None, descriptor=None):
        self.descriptor = descriptor

        super().__init__(page)

        self.params = params or CrudParams()
        self.parent_crud = None

        if page.defined_uri is None and not page.override:  # override -> allow empty urls for override @crud's functionality
            raise ValidationException('@crud annotations require page to have url')

        self.page.template_libs.append('i18n')

    def format_extension_value(self, current_value):
        if not current_value:
            current_value = {}
        descriptor = self.descriptor or '_'

        if descriptor not in current_value:
            current_value[descriptor] = {}

        if self.get_name() in current_value[descriptor]:
            raise GlobalScopeValidationError("Can not add another crud with same descriptor. Consider to specify"
                                             "explicit descriptors for subsequent descriptors")
        current_value[descriptor][self.get_name()] = self

        return current_value

    def get_extension_type(self):
        return CrudPageExtension

    def post_process(self):
        self.page.register_extension(self)
        self.prepare_environment(self.params, self.page)
        self.build_pages(self.page)

    def prepare_environment(self, crud, page):
        if self.crud_page in crud.next_page:
            next_page = crud.next_page[self.crud_page]
        elif 'all' in crud.next_page:
            next_page = crud.next_page['all']
        else:
            next_page = None

        if next_page:
            self.next_page_expr = f"{next_page}"
        else:
            self.next_page_expr = f"url=self.request.get_full_path()" + self.link_suffix

        self.field_filters = {}
        if crud.fields:
            all_fields = []
            for field in crud.fields:
                all_fields.append(field.spec)
                if field.filter_expr and not field.spec.startswith('^'):
                    self.field_filters[field.spec] = field.filter_expr

            crud_fields = all_fields
        else:
            crud_fields = None

        # appname, model_cls, fields
        if crud.model.startswith('#'):
            model = page.application.resolve_model(crud.model[1:])
            self.app_name = model.application.app_name + '.models'
            self.model_cls = model.class_name
            self.model_name = model.name or model.class_name
            self.model_name_plural = model.name_plural or f'{self.model_name} items'
            self.fields = {field.name: field.verbose_name or field.name.replace('_', ' ').capitalize() for field in
                           model.filter_fields(crud_fields or '*') if not field.read_only}
            self.list_fields = {field.name: field.verbose_name or field.name.replace('_', ' ').capitalize() for field in
                                model.filter_fields(crud.list_fields or crud_fields or '*')}
        else:
            parts = crud.model.split('.')
            self.app_name = '.'.join(parts[:-1]) + '.models'
            self.model_cls = parts[-1]
            self.model_name = self.model_cls
            self.model_name_plural = f'{self.model_name} items'
            self.fields = {field: field.replace('_', ' ').capitalize() for field in crud_fields}
            self.list_fields = {field: field.replace('_', ' ').capitalize() for field in
                                crud.list_fields or crud_fields}
            if not self.fields:
                raise ValidationException('@crud -> fields for external models are required: {}'.format(crud.model))

        # link extension
        if crud.link_extension:
            self.link_extension = crud.link_extension
            link_extension_params = []
            for item in re.split('\s+', self.link_extension):
                key, val = item.split('=')
                link_extension_params.append(f"'{key}': {val}")
            self.link_extension_params = ', '.join(link_extension_params)
        else:
            self.link_extension = ''
            self.link_extension_params = ''

        if crud.link_suffix:
            self.link_suffix = crud.link_suffix

        # name_prefix
        if self.descriptor:
            self.name_prefix = f'{self.descriptor}_'
            self.name_suffix = f'_{self.descriptor}'
        else:
            self.name_prefix = ''
            self.name_suffix = ''

        self.context_object_name = 'item'

        # block name
        if crud.block_name:
            self.block_name = crud.block_name
        else:
            self.block_name = 'content'

        # crud theme
        if crud.theme:
            self.theme = crud.theme

        if crud.list_type:
            self.list_type = crud.list_type

        self.header = crud.header

        # url prefix
        if crud.url_prefix:
            self.url_prefix = crud.url_prefix
            if not self.url_prefix.endswith('/'):
                self.url_prefix = self.url_prefix + '/'
        elif self.descriptor:
            self.url_prefix = f'{self.descriptor}/'
        else:
            self.url_prefix = ''
        if page.defined_uri:
            if not page.defined_uri.endswith('/'):
                self.url_prefix = '/' + self.url_prefix

        # pk
        if crud.pk_param:
            self.pk_param = crud.pk_param

        self.pk_param = f'{self.name_prefix}pk'
        self.item_name = crud.item_name or f"{self.name_prefix}item"
        self.items_name = f"{self.item_name}_list"

        # formatted_query
        if crud.query:
            self.query = crud.query.strip()
            self.formatted_query = '.filter({})'.format(self.query)
        else:
            self.formatted_query = '.all()'

        # object
        if crud.object_expr:
            self.object_expr = crud.object_expr
        else:
            self.object_expr = f'{self.model_cls}.objects{self.formatted_query}.get(pk=url.{self.pk_param})'

        # auth
        if crud.can_edit:
            self.can_edit = crud.can_edit
        else:
            self.can_edit = repr(True)

        if self.descriptor:
            self.can_edit_item = f'{self.descriptor}_can_edit'
        else:
            self.can_edit_item = f'can_edit'

        if crud.skip:
            self.create_list = 'list' not in list(crud.skip)
        else:
            self.create_list = True

        # pages that are not needed
        self.crud_pages = [
            x for x in ['detail', 'create', 'edit', 'delete', 'list'] if x not in list(crud.skip or [])
        ]

        if self.parent_crud:
            link_crud = self.parent_crud
            link_page = self.parent_base_page
        else:
            link_crud = self
            link_page = self.page

        self.links = {x: f"{link_page.application.app_name}.{link_page.name}" f"{link_crud.name_suffix}_{x}" for x in
                      link_crud.crud_pages}

        if self.create_list:
            self.links['list'] = f"{link_page.application.app_name}.{link_page.name}"

        if self.parent_base_page and 'list' in self.links:
            self.links['parent'] = self.links['list']

    def format_link(self, kind):
        if kind not in self.links:
            return ''

        url = repr(self.links[kind])

        for param in self.page.get_uri_params():
            if param != self.pk_param:
                url += f' {param}=url.{param}'

        if kind in ('edit', 'detail', 'delete'):
            url += f' {self.pk_param}={self.item_name}.pk'

        return "{% url " + url + " %}" + self.link_suffix

    def format_link_django(self, kind):
        if kind not in self.links:
            return ''

        params = []
        for param in self.page.get_uri_params():
            if param != self.pk_param:
                params.append(f'"{param}":url.{param}')

        if kind in ('edit', 'detail', 'delete'):
            params.append(f'"{self.pk_param}":{self.item_name}.pk')

        url = f"reverse_lazy({repr(self.links[kind])}, kwargs={{{','.join(params)}}})"

        if self.link_suffix:
            url += ' + ' + repr(self.link_suffix)

        return url

    def format_link_react(self, kind):
        if kind not in self.links:
            return ''

        params = []
        for param in self.page.get_uri_params():
            if param != self.pk_param:
                params.append(f'"{param}":url.{param}')

        if kind in ('edit', 'detail', 'delete'):
            params.append(f'"{self.pk_param}": this.props.store.data.{self.item_name}? this.props.store.data.{self.item_name}.id : {self.item_name}.id')

        url = f"reverse(routes.{self.links[kind]}, {{{','.join(params)}}})"

        if self.link_suffix:
            url += ' + ' + repr(self.link_suffix)

        return url

    def format_link_flutter(self, kind):
        if kind not in self.links:
            return ''

        params = []
        for param in self.page.get_uri_params():
            if param != self.pk_param:
                params.append(f'{to_camel_case(param)}:url.{param}')

        if kind in ('edit', 'detail', 'delete'):
            params.append(f"{to_camel_case_decap(self.pk_param)}: {to_camel_case_decap(self.item_name)}['id']")

        url = f"App.url.{to_camel_case_path(self.links[kind])}({','.join(params)})"

        if self.link_suffix:
            url += ' + ' + repr(self.link_suffix)

        return url

    def build_pages(self, base_page):
        from zmei_generator.contrib.web.extensions.page.crud_list import build_list_page

        for crud_page in self.crud_pages:

            if crud_page == 'list':

                build_list_page(self, base_page)

                continue

            crud_page_name = f"{base_page.name}{self.name_suffix}_{crud_page}"

            if crud_page_name in base_page.application.pages:
                append = True
                new_page = base_page.application.pages[crud_page_name]
            else:
                append = False
                new_page = PageDef(self.page.application)
                new_page.parent_name = base_page.name
                new_page.name = crud_page_name
                base_page.application.pages[new_page.name] = new_page

            # copy extensions
            for ext in base_page.get_extensions():
                if isinstance(ext, PageExtension) and ext.can_inherit:
                    new_page.register_extension(ext)

            if crud_page == 'create':
                new_page.set_uri(f"./{self.url_prefix}{crud_page}")
            else:
                new_page.set_uri(f"./{self.url_prefix}<{self.pk_param}>/{crud_page}")

            # after we have assigned uri, we can remove override flag
            # new_page.override = False

            new_page.template_libs.append('i18n')

            params = copy(self.params)
            link_extension_params = ', '.join([f"{x}=url.{x}" for x in self.page.get_uri_params() if x != self.pk_param])

            if crud_page not in params.next_page:
                if 'all' not in params.next_page:
                    params.next_page[
                        crud_page] = f"'{base_page.application.app_name}.{base_page.name}', {link_extension_params}"

            crud = crud_cls_by_name(crud_page)(new_page, params=params, descriptor=self.descriptor,
                                               parent_crud=self, parent_base_page=base_page, append=append)

            base_page.application.extensions.append(crud)


def crud_cls_by_name(name):
    from zmei_generator.contrib.web.extensions.page.crud_create import CrudCreatePageExtension
    from zmei_generator.contrib.web.extensions.page.crud_delete import CrudDeletePageExtension
    from zmei_generator.contrib.web.extensions.page.crud_detail import CrudDetailPageExtension
    from zmei_generator.contrib.web.extensions.page.crud_edit import CrudEditPageExtension
    from zmei_generator.contrib.web.extensions.page.crud_list import CrudListPageExtension

    return dict((
        ("create", CrudCreatePageExtension),
        ("delete", CrudDeletePageExtension),
        ("detail", CrudDetailPageExtension),
        ("edit", CrudEditPageExtension),
        ("list", CrudListPageExtension),
    ))[name]


class BaseCrudSubpageExtension(CrudPageExtension):
    crud_page = None

    def __init__(self, page, params=None, descriptor=None, parent_crud=None, parent_base_page=None, append=False):
        super().__init__(page, params, descriptor)
        self.append = append
        self.parent_crud = parent_crud
        self.parent_base_page = parent_base_page

    def build_pages(self, base_page):
        pass
