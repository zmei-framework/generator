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


class CrudDetailPageExtraParserListener(CrudBasePageExtraParserListener):

    def enterAn_crud_detail(self, ctx: ZmeiLangParser.An_crud_detailContext):
        self.extra_start(CrudDetailPageExtra, ctx)

    def exitAn_crud_detail(self, ctx: ZmeiLangParser.An_crud_detailContext):
        self.extra_end(CrudDetailPageExtra, ctx)
