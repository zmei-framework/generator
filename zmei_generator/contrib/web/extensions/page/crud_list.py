from zmei_generator.domain.page_expression import PageExpression
from zmei_generator.contrib.web.extensions.page.block import InlineTemplatePageBlock
from zmei_generator.contrib.web.extensions.page.crud import BaseCrudSubpageExtension
from zmei_generator.contrib.web.extensions.page.crud_parser import CrudBasePageExtensionParserListener
from zmei_generator.parser.gen.ZmeiLangParser import ZmeiLangParser


def build_list_page(crud, base_page):
    base_page.template_libs.append('i18n')

    base_page.page_items[crud.items_name] = PageExpression(
        crud.items_name, f"{crud.model_cls}.objects{crud.formatted_query}", base_page)

    base_page.page_items[crud.can_edit_item] = PageExpression(
        crud.can_edit_item, crud.can_edit, base_page)

    base_page.add_block(
        crud.block_name,

        InlineTemplatePageBlock(f"theme/crud_list_{crud.list_type}.html", {
            'page': base_page,
            'crud': crud,
        }, ref=f"{crud.get_name()}{crud.name_suffix}")
    )

class CrudListPageExtension(BaseCrudSubpageExtension):
    @classmethod
    def get_name(cls):
        return 'crud_list'

    @property
    def crud_page(self):
        return 'list'

    def build_pages(self, base_page):
        build_list_page(self, base_page)


class CrudListPageExtensionParserListener(CrudBasePageExtensionParserListener):

    def enterAn_crud_list(self, ctx:ZmeiLangParser.An_crud_listContext):
        self.extension_start(CrudListPageExtension, ctx)
        self.crud.skip = ['detail', 'create', 'edit', 'delete']

    def exitAn_crud_list(self, ctx:ZmeiLangParser.An_crud_listContext):
        self.extension_end(CrudListPageExtension, ctx)
