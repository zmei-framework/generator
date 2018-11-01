from zmei_generator.extras.page.crud import BaseCrudSubpageExtra
from zmei_generator.extras.page.crud_parser import CrudBasePageExtraParserListener
from zmei_generator.parser.gen.ZmeiLangParser import ZmeiLangParser


class CrudDeletePageExtra(BaseCrudSubpageExtra):
    @classmethod
    def get_name(cls):
        return 'crud_delete'

    @property
    def crud_page(self):
        return 'delete'


class CrudDeletePageExtraParserListener(CrudBasePageExtraParserListener):

    def enterAn_crud_delete(self, ctx:ZmeiLangParser.An_crud_deleteContext):
        self.extra_start(CrudDeletePageExtra, ctx)

    def exitAn_crud_delete(self, ctx:ZmeiLangParser.An_crud_deleteContext):
        self.extra_end(CrudDeletePageExtra, ctx)
