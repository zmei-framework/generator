from zmei_generator.domain.page_def import PageDef
from zmei_generator.domain.page_expression import PageExpression
from zmei_generator.contrib.web.extensions.page.crud_create import CrudCreatePageExtension
from zmei_generator.contrib.web.extensions.page.crud_parser import CrudBasePageExtensionParserListener
from zmei_generator.parser.gen.ZmeiLangParser import ZmeiLangParser


class CrudDeletePageExtension(CrudCreatePageExtension):
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
        items = {}
        items[self.item_name] = PageExpression(
            self.item_name, self.object_expr, base_page)

        if self.append:
            items.update(base_page.page_items)
            base_page.page_items = items
        else:
            base_page.page_items.update(items)

        super().build_pages(base_page)

    def get_template_name(self):
        return "theme/crud_delete.html"


class CrudDeletePageExtensionParserListener(CrudBasePageExtensionParserListener):

    def enterAn_crud_delete(self, ctx:ZmeiLangParser.An_crud_deleteContext):
        self.extension_start(CrudDeletePageExtension, ctx)

    def exitAn_crud_delete(self, ctx:ZmeiLangParser.An_crud_deleteContext):
        self.extension_end(CrudDeletePageExtension, ctx)
