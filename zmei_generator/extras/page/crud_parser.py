import re

from zmei_generator.config.domain.collection_set_def import CollectionSetDef
from zmei_generator.extras.page.crud import CrudField, CrudPageExtra
from zmei_generator.parser.gen.ZmeiLangParser import ZmeiLangParser
from zmei_generator.parser.utils import BaseListener


class CrudBasePageExtraParserListener(BaseListener):

    def __init__(self, collection_set: CollectionSetDef) -> None:
        super().__init__(collection_set)

        self.crud = None
        self.crud_field = None

    def extra_start(self, cls, ctx):
        extra = cls(self.page)
        self.collection_set.extras.append(
            extra
        )
        self.collection_set.crud = True
        self.crud = extra

    def extra_end(self, cls, ctx):
        self.crud = None

    def enterAn_crud_descriptor(self, ctx: ZmeiLangParser.An_crud_descriptorContext):
        self.crud.descriptor = ctx.getText()

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


class CrudPageExtraParserListener(CrudBasePageExtraParserListener):

    def enterAn_crud(self, ctx: ZmeiLangParser.An_crudContext):
        self.extra_start(CrudPageExtra, ctx)

    def exitAn_crud(self, ctx: ZmeiLangParser.An_crudContext):
        self.extra_end(CrudPageExtra, ctx)
