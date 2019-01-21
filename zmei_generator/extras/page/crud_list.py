from zmei_generator.extras.page.crud import BaseCrudSubpageExtra
from zmei_generator.extras.page.crud_create import CrudCreatePageExtra
from zmei_generator.extras.page.crud_parser import CrudBasePageExtraParserListener
from zmei_generator.parser.gen.ZmeiLangParser import ZmeiLangParser


class CrudListPageExtra(BaseCrudSubpageExtra):
    @classmethod
    def get_name(cls):
        return 'crud_list'

    @property
    def crud_page(self):
        return 'list'


class CrudListPageExtraParserListener(CrudBasePageExtraParserListener):

    def enterAn_crud_list(self, ctx:ZmeiLangParser.An_crud_listContext):
        self.extra_start(CrudListPageExtra, ctx)
        self.crud.skip = ['detail', 'create', 'edit', 'delete']

    def exitAn_crud_list(self, ctx:ZmeiLangParser.An_crud_listContext):
        self.extra_end(CrudListPageExtra, ctx)
