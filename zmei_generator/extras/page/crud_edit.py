from zmei_generator.extras.page.crud import BaseCrudSubpageExtra
from zmei_generator.extras.page.crud_parser import CrudBasePageExtraParserListener
from zmei_generator.parser.gen.ZmeiLangParser import ZmeiLangParser


class CrudEditPageExtra(BaseCrudSubpageExtra):
    @classmethod
    def get_name(cls):
        return 'crud_edit'

    @property
    def crud_page(self):
        return 'edit'


class CrudEditPageExtraParserListener(CrudBasePageExtraParserListener):

    def enterAn_crud_edit(self, ctx:ZmeiLangParser.An_crud_editContext):
        self.extra_start(CrudEditPageExtra, ctx)

    def exitAn_crud_edit(self, ctx:ZmeiLangParser.An_crud_editContext):
        self.extra_end(CrudEditPageExtra, ctx)
