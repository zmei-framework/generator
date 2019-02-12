from zmei_generator.domain.page_def import PageDef
from zmei_generator.domain.page_expression import PageExpression
from zmei_generator.contrib.web.extensions.page.crud_create import CrudCreatePageExtension
from zmei_generator.contrib.web.extensions.page.crud_parser import CrudBasePageExtensionParserListener
from zmei_generator.parser.gen.ZmeiLangParser import ZmeiLangParser


class CrudEditPageExtension(CrudCreatePageExtension):
    @classmethod
    def get_name(cls):
        return 'crud_edit'

    @property
    def crud_page(self):
        return 'edit'

    def get_form_init(self):
        return f"request.POST if request.method == 'POST' else None, request.FILES if request.method == 'POST' else None, instance={self.item_name}"

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
        return "theme/crud_edit.html"


class CrudEditPageExtensionParserListener(CrudBasePageExtensionParserListener):

    def enterAn_crud_edit(self, ctx:ZmeiLangParser.An_crud_editContext):
        self.extension_start(CrudEditPageExtension, ctx)

    def exitAn_crud_edit(self, ctx:ZmeiLangParser.An_crud_editContext):
        self.extension_end(CrudEditPageExtension, ctx)
