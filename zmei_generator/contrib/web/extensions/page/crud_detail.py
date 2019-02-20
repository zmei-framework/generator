from zmei_generator.domain.page_expression import PageExpression
from zmei_generator.contrib.web.extensions.page.block import InlineTemplatePageBlock
from zmei_generator.contrib.web.extensions.page.crud import BaseCrudSubpageExtension
from zmei_generator.contrib.web.extensions.page.crud_parser import CrudBasePageExtensionParserListener
from zmei_generator.parser.gen.ZmeiLangParser import ZmeiLangParser


class CrudDetailPageExtension(BaseCrudSubpageExtension):
    @classmethod
    def get_name(cls):
        return 'crud_detail'

    @property
    def crud_page(self):
        return 'detail'

    def build_pages(self, base_page):

        items = {}
        items[self.item_name] = PageExpression(
            self.item_name, self.object_expr, base_page)

        if self.append:
            items.update(base_page.page_items)
            base_page.page_items = items
        else:
            base_page.page_items.update(items)

        base_page.add_block(
            self.block_name,

            InlineTemplatePageBlock(f"theme/crud_detail.html", {
                'page': base_page,
                'crud': self,
            }, ref=f"{self.get_name()}{self.name_suffix}"),

            append=self.append
        )


class CrudDetailPageExtensionParserListener(CrudBasePageExtensionParserListener):

    def enterAn_crud_detail(self, ctx: ZmeiLangParser.An_crud_detailContext):
        self.extension_start(CrudDetailPageExtension, ctx)

    def exitAn_crud_detail(self, ctx: ZmeiLangParser.An_crud_detailContext):
        self.extension_end(CrudDetailPageExtension, ctx)
