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
        self.crud_field = None

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

    def enterAn_crud_theme(self, ctx: ZmeiLangParser.An_crud_themeContext):
        self.crud.params.theme = ctx.id_or_kw().getText().strip()

    def enterAn_crud_skip(self, ctx: ZmeiLangParser.An_crud_skipContext):
        self.crud.params.skip = re.split('\s*,\s*', ctx.an_crud_skip_values().getText().strip())

    def enterAn_crud_fields(self, ctx: ZmeiLangParser.An_crud_fieldsContext):
        self.crud.params.fields = []

    def enterAn_crud_field(self, ctx: ZmeiLangParser.An_crud_fieldContext):
        field = CrudField()
        field.spec = ctx.an_crud_field_spec().getText().strip()
        if ctx.an_crud_field_filter():
            field.filter_expr = ctx.an_crud_field_filter().getText().strip()

        self.crud.params.fields.append(field)

    def enterAn_crud_list_fields(self, ctx: ZmeiLangParser.An_crud_list_fieldsContext):
        self.crud.params.list_fields = []

    def enterAn_crud_list_field(self, ctx: ZmeiLangParser.An_crud_list_fieldContext):
        field = ctx.an_crud_list_field_spec().getText().strip()

        self.crud.params.list_fields.append(field)

    def enterAn_crud_pk_param(self, ctx: ZmeiLangParser.An_crud_pk_paramContext):
        self.crud.params.pk_param = ctx.id_or_kw().getText().strip()

    def enterAn_crud_item_name(self, ctx: ZmeiLangParser.An_crud_item_nameContext):
        self.crud.params.item_name = ctx.id_or_kw().getText().strip()

    def enterAn_crud_block(self, ctx: ZmeiLangParser.An_crud_blockContext):
        self.crud.params.block_name = ctx.id_or_kw().getText().strip()

    def enterAn_crud_object_expr(self, ctx: ZmeiLangParser.An_crud_object_exprContext):
        self.crud.params.object_expr = self._get_code(ctx)

    def enterAn_crud_can_edit(self, ctx: ZmeiLangParser.An_crud_can_editContext):
        self.crud.params.can_edit = self._get_code(ctx)

    def enterAn_crud_target_filter(self, ctx: ZmeiLangParser.An_crud_target_filterContext):
        self.crud.params.query = self._get_code(ctx)

    def enterAn_crud_url_prefix_val(self, ctx: ZmeiLangParser.An_crud_url_prefix_valContext):
        self.crud.params.url_prefix = ctx.getText().strip(' "\'')

    def enterAn_crud_link_suffix_val(self, ctx:ZmeiLangParser.An_crud_link_suffix_valContext):
        self.crud.params.link_suffix = ctx.getText().strip(' "\'')

    def enterAn_crud_next_page(self, ctx: ZmeiLangParser.An_crud_next_pageContext):
        self.crud.params.next_page = self._get_code(ctx)

    def enterAn_crud_next_page_url_val(self, ctx:ZmeiLangParser.An_crud_next_page_url_valContext):
        self.crud.params.next_page = ctx.getText()


class CrudPageExtraParserListener(CrudBasePageExtraParserListener):

    def enterAn_crud(self, ctx: ZmeiLangParser.An_crudContext):
        self.extra_start(CrudPageExtra)

    def exitAn_crud(self, ctx: ZmeiLangParser.An_crudContext):
        self.extra_end(CrudPageExtra)


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
    can_edit = None
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
            self.next_page_expr = f"return {crud.next_page}"
        else:
            self.next_page_expr = f"return self.request.get_full_path()" + self.link_suffix

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
            self.app_name = page.collection_set.app_name + '.models'
            collection = page.collection_set.collections[crud.model[1:]]
            self.model_cls = collection.class_name
            self.fields = {field.name: field.verbose_name or field.name.replace('_', ' ').capitalize() for field in
                           collection.filter_fields(crud_fields or '*') if not field.read_only}
            self.list_fields = {field.name: field.verbose_name or field.name.replace('_', ' ').capitalize() for field in
                                collection.filter_fields(crud.list_fields or crud_fields or '*') if not field.read_only}
        else:
            parts = crud.model.split('.')
            self.app_name = '.'.join(parts[:-1]) + '.models'
            self.model_cls = parts[-1]
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
        if crud.can_edit:
            self.can_edit = crud.can_edit
        else:
            self.can_edit = repr(True)

        # formatted_query
        if crud.query:
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

        ctx = {
            'link_suffix': repr(self.link_suffix),
            'can_edit': self.can_edit,
            'fields': repr(self.fields),
            'list_fields': repr(self.list_fields),
            'link_extra': repr(link_extra),
            # 'meta': f'{self.name_prefix}{self.item_name}_meta',
            # 'item': repr(f"{self.context_object_name}"),
            # 'items': repr(f"{self.context_object_name}_list"),
            'pk_param': repr(self.pk_param),
            'context_object_name': repr(self.context_object_name),
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
            link_extra_params = "{key: val for key, val in self.kwargs.items() if key != self.pk_url_kwarg}"
            params.next_page = f"reverse('{page.collection_set.app_name}.{page.name}', kwargs={link_extra_params})"

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
            if self.can_edit:
                add_page_auth(self.can_edit, page)

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
