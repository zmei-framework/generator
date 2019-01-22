import re
from copy import copy

from zmei_generator.extras.page.block import ThemeFileIncludePageBlock, InlineTemplatePageBlock
from zmei_generator.parser.errors import GlobalScopeValidationError as ValidationException
from zmei_generator.config.domain.page_def import PageDef
from zmei_generator.config.domain.page_expression import PageExpression
from zmei_generator.config.extras import PageExtra


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
        self.skip = None
        self.block_name = None
        self.theme = None
        self.url_prefix = None
        self.pk_param = None
        self.object_expr = None
        self.can_edit = None
        self.item_name = None
        self.link_extra = None
        self.link_suffix = None
        self.next_page = {}


class CrudPageExtra(PageExtra):
    @classmethod
    def get_name(cls):
        return 'crud'

    crud_page = None

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
    can_edit = None
    query = None
    next_page_expr = None
    item_name = None
    items_name = None
    field_filters = None
    create_list = True
    link_suffix = ''

    parent_base_page = None

    def __init__(self, page, params=None, descriptor=None):
        super().__init__(page)

        self.params = params or CrudParams()

        self.descriptor = descriptor
        self.parent_crud = None

        if page.defined_uri is None and not page.override:  # override -> allow empty urls for override @crud's functionality
            raise ValidationException('@crud annotations require page to have url')

    def post_process(self):
        if self.descriptor not in self.page.cruds:
            self.page.cruds[self.descriptor or '_'] = {}

        self.page.cruds[self.descriptor or '_'][self.get_name()] = self

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
            self.next_page_expr = f"self.request.get_full_path()" + self.link_suffix

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
            collection = page.collection_set.resolve_collection(crud.model[1:])
            self.app_name = collection.collection_set.app_name + '.models'
            self.model_cls = collection.class_name
            self.model_name = collection.name or collection.class_name
            self.model_name_plural = collection.name_plural or f'{self.model_name} items'
            self.fields = {field.name: field.verbose_name or field.name.replace('_', ' ').capitalize() for field in
                           collection.filter_fields(crud_fields or '*') if not field.read_only}
            self.list_fields = {field.name: field.verbose_name or field.name.replace('_', ' ').capitalize() for field in
                                collection.filter_fields(crud.list_fields or crud_fields or '*') if not field.read_only}
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

        self.context_object_name = 'item'

        # block name
        if crud.block_name:
            self.block_name = crud.block_name
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
            x for x in ['detail', 'create', 'edit', 'delete'] if x not in list(crud.skip or [])
        ]

        if self.parent_crud:
            link_crud = self.parent_crud
            link_page = self.parent_base_page
        else:
            link_crud = self
            link_page = self.page

        self.links = {x: f"{link_page.collection_set.app_name}.{link_page.name}" f"{link_crud.name_suffix}_{x}" for x in
                      link_crud.crud_pages}

        if self.create_list:
            self.links['list'] = f"{link_page.collection_set.app_name}.{link_page.name}"

        if self.parent_base_page:
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

    def build_pages(self, base_page):

        base_page.add_crud(self.descriptor, self)

        if self.create_list:
            base_page.template_libs.append('i18n')

            base_page.page_items[self.items_name] = PageExpression(
                self.items_name, f"{self.model_cls}.objects{self.formatted_query}", base_page)

            base_page.page_items[self.can_edit_item] = PageExpression(
                self.can_edit_item, self.can_edit, base_page)

            base_page.add_block(
                self.block_name,

                InlineTemplatePageBlock(f"theme/crud_list.html", {
                    'page': base_page,
                    'crud': self,
                })
            )

        for crud_page in self.crud_pages:

            crud_page_name = f"{base_page.name}{self.name_suffix}_{crud_page}"

            if crud_page_name in base_page.collection_set.pages:
                append = True
                new_page = base_page.collection_set.pages[crud_page_name]
            else:
                append = False
                new_page = PageDef(self.page.collection_set)
                new_page.parent_name = base_page.name
                new_page.name = crud_page_name
                base_page.collection_set.pages[new_page.name] = new_page

            if crud_page == 'create':
                new_page.set_uri(f"./{self.url_prefix}{crud_page}")
            else:
                new_page.set_uri(f"./{self.url_prefix}<{self.pk_param}>/{crud_page}")

            # after we have assigned uri, we can remove override flag
            # new_page.override = False

            new_page.template_libs.append('i18n')

            params = copy(self.params)
            link_extra_params = ', '.join([f"{x}=url.{x}" for x in self.page.get_uri_params() if x != self.pk_param])

            if crud_page not in params.next_page:
                if 'all' not in params.next_page:
                    params.next_page[
                        crud_page] = f"'{base_page.collection_set.app_name}.{base_page.name}', {link_extra_params}"

            crud = crud_cls_by_name(crud_page)(new_page, params=params, descriptor=self.descriptor,
                                               parent_crud=self, parent_base_page=base_page, append=append)

            base_page.collection_set.extras.append(crud)


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

    def __init__(self, page, params=None, descriptor=None, parent_crud=None, parent_base_page=None, append=False):
        super().__init__(page, params, descriptor)
        self.append = append
        self.parent_crud = parent_crud
        self.parent_base_page = parent_base_page

    def build_pages(self, base_page):
        pass
