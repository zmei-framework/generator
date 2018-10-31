from zmei_generator.config.extras import PageExtra
from zmei_generator.extras.page.crud import BaseCrudSubpageExtra, CrudBasePageExtraParserListener
from zmei_generator.parser.gen.ZmeiLangParser import ZmeiLangParser
from zmei_generator.parser.utils import BaseListener


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
