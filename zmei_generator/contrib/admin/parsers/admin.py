from zmei_generator.contrib.admin.extensions.application.suit import SuitAppExtension
from zmei_generator.contrib.admin.extensions.model.admin import AdminModelExtension, AdminInlineConfig
from zmei_generator.domain.application_def import ApplicationDef
from zmei_generator.parser.errors import TabsSuitRequiredValidationError
from zmei_generator.parser.gen.ZmeiLangParser import ZmeiLangParser
from zmei_generator.parser.utils import BaseListener


class AdminParserListener(BaseListener):
    def __init__(self, application: ApplicationDef) -> None:
        super().__init__(application)

        self.inline = None  # type

    ############################################
    # Admin
    ############################################

    def enterAn_admin(self, ctx: ZmeiLangParser.An_adminContext):
        self.application.extensions.append(AdminModelExtension(self.model))

    def enterAn_admin_list(self, ctx: ZmeiLangParser.An_admin_listContext):
        self.model[AdminModelExtension].admin_list = self.model.filter_fields(self._get_fields(ctx))

    def enterAn_admin_read_only(self, ctx: ZmeiLangParser.An_admin_read_onlyContext):
        self.model[AdminModelExtension].read_only = self.model.filter_fields(self._get_fields(ctx))

    def enterAn_admin_list_editable(self, ctx: ZmeiLangParser.An_admin_list_editableContext):
        self.model[AdminModelExtension].list_editable = self.model.filter_fields(self._get_fields(ctx))

    def enterAn_admin_list_filter(self, ctx: ZmeiLangParser.An_admin_list_filterContext):
        self.model[AdminModelExtension].list_filter = self.model.filter_fields(self._get_fields(ctx))

    def enterAn_admin_list_search(self, ctx: ZmeiLangParser.An_admin_list_searchContext):
        self.model[AdminModelExtension].list_search = self.model.filter_fields(self._get_fields(ctx))

    def enterAn_admin_fields(self, ctx: ZmeiLangParser.An_admin_fieldsContext):
        self.model[AdminModelExtension].fields = self.model.filter_fields(self._get_fields(ctx))

    def enterAn_admin_tabs(self, ctx: ZmeiLangParser.An_admin_tabsContext):
        if not self.application.supports(SuitAppExtension):
            raise TabsSuitRequiredValidationError(ctx.start)

    def enterAn_admin_tab(self, ctx: ZmeiLangParser.An_admin_tabContext):
        fields = self._get_fields(ctx)
        name = ctx.tab_name().getText()
        vname = ctx.tab_verbose_name()
        if vname:
            vname = vname.getText().strip('"\' ')
        else:
            vname = None
        self.model[AdminModelExtension].register_tab(name, vname, fields)

    def enterAn_admin_inline(self, ctx: ZmeiLangParser.An_admin_inlineContext):
        self.inline = AdminInlineConfig(self.model[AdminModelExtension], ctx.inline_name().getText())

    def enterInline_type(self, ctx: ZmeiLangParser.Inline_typeContext):
        type_name = ctx.inline_type_name().getText()

        if type_name == 'polymorphic':
            self.model[AdminModelExtension].has_polymorphic_inlines = True

        self.inline.inline_type = type_name

    def enterInline_fields(self, ctx: ZmeiLangParser.Inline_fieldsContext):
        self.inline.fields_expr = self._get_fields(ctx)

    def enterInline_extension(self, ctx: ZmeiLangParser.Inline_extensionContext):
        self.inline.extension_count = int(ctx.DIGIT().getText())

    def enterAn_admin_css_file_name(self, ctx: ZmeiLangParser.An_admin_css_file_nameContext):
        self.model[AdminModelExtension].css.append(ctx.getText().strip('"\''))

    def enterAn_admin_js_file_name(self, ctx: ZmeiLangParser.An_admin_js_file_nameContext):
        self.model[AdminModelExtension].js.append(ctx.getText().strip('"\''))

    def exitAn_admin_inline(self, ctx: ZmeiLangParser.An_admin_inlineContext):
        self.model[AdminModelExtension].inlines.append(
            self.inline
        )
        self.inline = None
