from zmei_generator.config.domain.page_def import PageDef
from zmei_generator.parser.gen.ZmeiLangParser import ZmeiLangParser
from zmei_generator.parser.utils import BaseListener


class PageCrudOverrideExtraListener(
    BaseListener
):
    # Page crud

    def enterAn_crud_descriptor(self, ctx: ZmeiLangParser.An_crud_descriptorContext):
        self.page._last_crud_descriptor = ctx.getText()

    def enterAn_crud_page_override(self, ctx: ZmeiLangParser.An_crud_page_overrideContext):
        crud_name = ctx.an_crud_view_name().getText()

        if hasattr(self.page, '_last_crud_descriptor'):
            override_id = f"{self.page._last_crud_descriptor}_{crud_name}"
        else:
            override_id = crud_name

        self.page_backup = self.page

        if override_id not in self.page_backup.crud_overrides:
            self.page = PageDef(self.collection_set, override=True)
            self.page.page_items = {}
        else:
            self.page = self.page_backup.crud_overrides[override_id]

        self.page_backup.crud_overrides[override_id] = self.page

    def exitAn_crud_page_override(self, ctx: ZmeiLangParser.An_crud_page_overrideContext):
        self.page = self.page_backup



