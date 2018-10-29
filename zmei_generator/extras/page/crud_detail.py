from zmei_generator.config.extras import PageExtra
from zmei_generator.extras.page.crud import BaseCrudSubpageExtra, CrudBasePageExtraParserListener
from zmei_generator.extras.page.crud_create import CrudCreatePageExtra
from zmei_generator.parser.gen.ZmeiLangParser import ZmeiLangParser
from zmei_generator.parser.utils import BaseListener


class CrudDetailPageExtra(BaseCrudSubpageExtra):
    @classmethod
    def get_name(cls):
        return 'crud_detail'

    @property
    def crud_page(self):
        return 'detail'


class CrudDetailPageExtraParserListener(CrudBasePageExtraParserListener):

    def enterAn_crud_detail(self, ctx: ZmeiLangParser.An_crud_detailContext):
        self.extra_start(CrudDetailPageExtra)

    def exitAn_crud_detail(self, ctx: ZmeiLangParser.An_crud_detailContext):
        self.extra_end(CrudDetailPageExtra)
