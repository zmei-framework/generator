from zmei_generator.contrib.admin.extras.collection_set.suit import SuitCsExtra
from zmei_generator.contrib.admin.extras.model.admin import AdminExtra, AdminInlineConfig
from zmei_generator.domain.collection_set_def import CollectionSetDef
from zmei_generator.parser.errors import TabsSuitRequiredValidationError
from zmei_generator.parser.gen.ZmeiLangParser import ZmeiLangParser
from zmei_generator.parser.utils import BaseListener


class AdminParserListener(BaseListener):
    def __init__(self, collection_set: CollectionSetDef) -> None:
        super().__init__(collection_set)

        self.inline = None  # type

    ############################################
    # Admin
    ############################################

    def enterAn_admin(self, ctx: ZmeiLangParser.An_adminContext):
        self.model.admin = AdminExtra(self.model)
        self.collection_set.admin = True
        self.collection_set.extras.append(self.model.admin)

    def enterAn_admin_list(self, ctx: ZmeiLangParser.An_admin_listContext):
        self.model.admin.admin_list = self.model.filter_fields(self._get_fields(ctx))

    def enterAn_admin_read_only(self, ctx: ZmeiLangParser.An_admin_read_onlyContext):
        self.model.admin.read_only = self.model.filter_fields(self._get_fields(ctx))

    def enterAn_admin_list_editable(self, ctx: ZmeiLangParser.An_admin_list_editableContext):
        self.model.admin.list_editable = self.model.filter_fields(self._get_fields(ctx))

    def enterAn_admin_list_filter(self, ctx: ZmeiLangParser.An_admin_list_filterContext):
        self.model.admin.list_filter = self.model.filter_fields(self._get_fields(ctx))

    def enterAn_admin_list_search(self, ctx: ZmeiLangParser.An_admin_list_searchContext):
        self.model.admin.list_search = self.model.filter_fields(self._get_fields(ctx))

    def enterAn_admin_fields(self, ctx: ZmeiLangParser.An_admin_fieldsContext):
        self.model.admin.fields = self.model.filter_fields(self._get_fields(ctx))

    def enterAn_admin_tabs(self, ctx: ZmeiLangParser.An_admin_tabsContext):
        if not self.collection_set.suit:
            raise TabsSuitRequiredValidationError(ctx.start)

    def enterAn_admin_tab(self, ctx: ZmeiLangParser.An_admin_tabContext):
        fields = self._get_fields(ctx)
        name = ctx.tab_name().getText()
        vname = ctx.tab_verbose_name()
        if vname:
            vname = vname.getText().strip('"\' ')
        else:
            vname = None
        self.model.admin.register_tab(name, vname, fields)

    def enterAn_admin_inline(self, ctx: ZmeiLangParser.An_admin_inlineContext):
        self.inline = AdminInlineConfig(self.model.admin, ctx.inline_name().getText())

    def enterInline_type(self, ctx: ZmeiLangParser.Inline_typeContext):
        type_name = ctx.KW_INLINE_TYPE().getText()

        if type_name == 'polymorphic':
            self.model.admin.has_polymorphic_inlines = True

        self.inline.inline_type = type_name

    def enterInline_fields(self, ctx: ZmeiLangParser.Inline_fieldsContext):
        self.inline.fields_expr = self._get_fields(ctx)

    def enterInline_extra(self, ctx: ZmeiLangParser.Inline_extraContext):
        self.inline.extra_count = int(ctx.DIGIT().getText())

    def enterAn_admin_css_file_name(self, ctx: ZmeiLangParser.An_admin_css_file_nameContext):
        self.model.admin.css.append(ctx.getText().strip('"\''))

    def enterAn_admin_js_file_name(self, ctx: ZmeiLangParser.An_admin_js_file_nameContext):
        self.model.admin.js.append(ctx.getText().strip('"\''))

    def exitAn_admin_inline(self, ctx: ZmeiLangParser.An_admin_inlineContext):
        self.model.admin.inlines.append(
            self.inline
        )
        self.inline = None

    # Suit

    def enterAn_suit(self, ctx: ZmeiLangParser.An_suitContext):
        suit = SuitCsExtra(self.collection_set)
        self.collection_set.extras.append(suit)
        self.collection_set.suit = suit

    def enterAn_suit_app_name(self, ctx: ZmeiLangParser.An_suit_app_nameContext):
        self.collection_set.suit.app_name = ctx.getText().strip('"\'')
