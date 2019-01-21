from zmei_generator.config.domain.page_def import PageDef
from zmei_generator.config.domain.page_expression import PageExpression
from zmei_generator.extras.page.block import InlineTemplatePageBlock
from zmei_generator.extras.page.crud import BaseCrudSubpageExtra
from zmei_generator.extras.page.crud_create import CrudCreatePageExtra
from zmei_generator.extras.page.crud_parser import CrudBasePageExtraParserListener
from zmei_generator.parser.gen.ZmeiLangParser import ZmeiLangParser


class CrudDeletePageExtra(CrudCreatePageExtra):
    @classmethod
    def get_name(cls):
        return 'crud_delete'

    @property
    def crud_page(self):
        return 'delete'

    def get_model_fields(self):
        return repr([])

    def get_form_action(self):
        return f"""
            {self.item_name}.delete()
        """

    def get_form_init(self):
        return f"instance={self.item_name}"

    def build_pages(self, base_page: PageDef):

        base_page.page_items[self.item_name] = PageExpression(
            self.item_name, self.object_expr, base_page)

        super().build_pages(base_page)

    def get_template_name(self):
        return "theme/crud_delete.html"


class CrudDeletePageExtraParserListener(CrudBasePageExtraParserListener):

    def enterAn_crud_delete(self, ctx:ZmeiLangParser.An_crud_deleteContext):
        self.extra_start(CrudDeletePageExtra, ctx)

    def exitAn_crud_delete(self, ctx:ZmeiLangParser.An_crud_deleteContext):
        self.extra_end(CrudDeletePageExtra, ctx)
