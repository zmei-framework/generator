from zmei_generator.config.domain.page_expression import PageExpression
from zmei_generator.extras.page.block import InlineTemplatePageBlock
from zmei_generator.extras.page.crud import BaseCrudSubpageExtra
from zmei_generator.extras.page.crud_parser import CrudBasePageExtraParserListener
from zmei_generator.parser.gen.ZmeiLangParser import ZmeiLangParser


class CrudDetailPageExtra(BaseCrudSubpageExtra):
    @classmethod
    def get_name(cls):
        return 'crud_detail'

    @property
    def crud_page(self):
        return 'detail'

    def build_pages(self, base_page):
        base_page.add_crud(self.descriptor, self)

        base_page.page_items[self.item_name] = PageExpression(
            self.item_name, self.object_expr, base_page)

        base_page.add_block(
            self.block_name,

            InlineTemplatePageBlock(f"theme/crud_detail.html", {
                'page': base_page,
                'crud': self,
            }),

            sorting=100
        )


class CrudDetailPageExtraParserListener(CrudBasePageExtraParserListener):

    def enterAn_crud_detail(self, ctx: ZmeiLangParser.An_crud_detailContext):
        self.extra_start(CrudDetailPageExtra, ctx)

    def exitAn_crud_detail(self, ctx: ZmeiLangParser.An_crud_detailContext):
        self.extra_end(CrudDetailPageExtra, ctx)
