import re

from zmei_generator.domain.application_def import ApplicationDef
from zmei_generator.domain.page_def import PageDef
from zmei_generator.contrib.web.extensions.page.crud import CrudField, CrudPageExtension
from zmei_generator.parser.gen.ZmeiLangParser import ZmeiLangParser
from zmei_generator.parser.utils import BaseListener


class CrudBasePageExtensionParserListener(BaseListener):

    def __init__(self, application: ApplicationDef) -> None:
        super().__init__(application)

        self.crud = None
        self.crud_field = None
        self.page_stack = []
        self.crud_stack = []

    def extension_start(self, cls, ctx):
        extension = cls(self.page)
        self.application.extensions.append(
            extension
        )
        # self.application.crud = True
        if self.crud:
            self.crud_stack.append(self.crud)
        self.crud = extension

    def extension_end(self, cls, ctx):
        if len(self.crud_stack):
            self.crud = self.crud_stack.pop()
        else:
            self.crud = None

    def enterAn_crud_descriptor(self, ctx: ZmeiLangParser.An_crud_descriptorContext):
        self.crud.descriptor = ctx.getText()

    # Crud page overrides

    def enterAn_crud_page_override(self, ctx: ZmeiLangParser.An_crud_page_overrideContext):
        page = self.page
        self.page_stack.append(self.page)

        crud_name = ctx.an_crud_view_name().getText()

        if self.crud.descriptor:
            name_suffix = f'_{self.crud.descriptor}'
        else:
            name_suffix = ''

        crud_page_name = f"{page.name}{name_suffix}_{crud_name}"

        if crud_page_name not in page.application.pages:
            self.page = PageDef(self.application, override=True)
            self.page.page_items = {}
            self.page.parent_name = page.name
            self.page.name = crud_page_name

            page.application.pages[crud_page_name] = self.page
        else:
            self.page = page.application.pages[crud_page_name]

    def exitAn_crud_page_override(self, ctx: ZmeiLangParser.An_crud_page_overrideContext):
        self.page = self.page_stack.pop()

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
            field.filter_expr = self._get_code(ctx.an_crud_field_filter())

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

    def exitAn_crud_list_type_var(self, ctx: ZmeiLangParser.An_crud_list_type_varContext):
        self.crud.params.list_type = ctx.getText()

    def exitAn_crud_header_enabled(self, ctx:ZmeiLangParser.An_crud_header_enabledContext):
        self.crud.params.header = ctx.getText() == 'true'

    def enterAn_crud_target_filter(self, ctx: ZmeiLangParser.An_crud_target_filterContext):
        self.crud.params.query = self._get_code(ctx)

    def enterAn_crud_url_prefix_val(self, ctx: ZmeiLangParser.An_crud_url_prefix_valContext):
        self.crud.params.url_prefix = ctx.getText().strip(' "\'')

    def enterAn_crud_link_suffix_val(self, ctx: ZmeiLangParser.An_crud_link_suffix_valContext):
        self.crud.params.link_suffix = ctx.getText().strip(' "\'')

    def enterAn_crud_next_page(self, ctx: ZmeiLangParser.An_crud_next_pageContext):
        code = self._get_code(ctx)

        self.add_next_page(code, ctx)

    def enterAn_crud_next_page_url(self, ctx: ZmeiLangParser.An_crud_next_page_urlContext):
        code = ctx.an_crud_next_page_url_val().getText()

        self.add_next_page(code, ctx)

    def add_next_page(self, code, ctx):
        if ctx.an_crud_next_page_event_name():
            event = ctx.an_crud_next_page_event_name().getText()
        else:
            event = 'all'
        self.crud.params.next_page[event] = code


class CrudPageExtensionParserListener(CrudBasePageExtensionParserListener):

    def enterAn_crud(self, ctx: ZmeiLangParser.An_crudContext):
        self.extension_start(CrudPageExtension, ctx)

    def exitAn_crud(self, ctx: ZmeiLangParser.An_crudContext):
        self.extension_end(CrudPageExtension, ctx)
