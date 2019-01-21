from zmei_generator.config.domain.page_def import PageDef
from zmei_generator.config.domain.page_expression import PageExpression
from zmei_generator.extras.page.crud_create import CrudCreatePageExtra
from zmei_generator.extras.page.crud_parser import CrudBasePageExtraParserListener
from zmei_generator.parser.gen.ZmeiLangParser import ZmeiLangParser


class CrudEditPageExtra(CrudCreatePageExtra):
    @classmethod
    def get_name(cls):
        return 'crud_edit'

    @property
    def crud_page(self):
        return 'edit'

    def get_form_init(self):
        return f"request.POST if request.method == 'POST' else None, instance={self.item_name}"

    def build_pages(self, base_page: PageDef):

        base_page.page_items[self.item_name] = PageExpression(
            self.item_name, self.object_expr, base_page)

        super().build_pages(base_page)

    def get_template_name(self):
        return "theme/crud_edit.html"


class CrudEditPageExtraParserListener(CrudBasePageExtraParserListener):

    def enterAn_crud_edit(self, ctx:ZmeiLangParser.An_crud_editContext):
        self.extra_start(CrudEditPageExtra, ctx)

    def exitAn_crud_edit(self, ctx:ZmeiLangParser.An_crud_editContext):
        self.extra_end(CrudEditPageExtra, ctx)
