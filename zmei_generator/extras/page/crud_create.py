from zmei_generator.extras.page.crud import BaseCrudSubpageExtra
from zmei_generator.extras.page.crud_parser import CrudBasePageExtraParserListener
from zmei_generator.parser.gen.ZmeiLangParser import ZmeiLangParser


class CrudCreatePageExtra(BaseCrudSubpageExtra):
    @classmethod
    def get_name(cls):
        return 'crud_create'

    @property
    def crud_page(self):
        return 'create'


class CrudCreatePageExtraParserListener(CrudBasePageExtraParserListener):

    def enterAn_crud_create(self, ctx: ZmeiLangParser.An_crud_createContext):
        self.extra_start(CrudCreatePageExtra, ctx)

    def exitAn_crud_create(self, ctx: ZmeiLangParser.An_crud_createContext):
        self.extra_end(CrudCreatePageExtra, ctx)

