from zmei_generator.contrib.web.extensions.page.crud import BaseCrudSubpageExtension
from zmei_generator.contrib.web.extensions.page.crud_parser import CrudBasePageExtensionParserListener
from zmei_generator.parser.gen.ZmeiLangParser import ZmeiLangParser


class CrudListPageExtension(BaseCrudSubpageExtension):
    @classmethod
    def get_name(cls):
        return 'crud_list'

    @property
    def crud_page(self):
        return 'list'


class CrudListPageExtensionParserListener(CrudBasePageExtensionParserListener):

    def enterAn_crud_list(self, ctx:ZmeiLangParser.An_crud_listContext):
        self.extension_start(CrudListPageExtension, ctx)
        self.crud.skip = ['detail', 'create', 'edit', 'delete']

    def exitAn_crud_list(self, ctx:ZmeiLangParser.An_crud_listContext):
        self.extension_end(CrudListPageExtension, ctx)
