import pkg_resources

from zmei_generator.domain.application_def import ApplicationDef
from zmei_generator.domain.page_def import PageDef
from zmei_generator.parser.gen.ZmeiLangParser import ZmeiLangParser
from zmei_generator.parser.utils import BaseListener

parsers = []
for entry_point in pkg_resources.iter_entry_points('zmei.parser.stage3'):
    parsers += entry_point.load()

parsers.append(BaseListener)


class PageExtensionListener(*parsers):

    def __init__(self, application: ApplicationDef) -> None:
        super().__init__(application)

        self.page = None  # type: PageDef
        self.parent = None
        self.extend_name = False
        self.last_crud_descriptor = None
        self.page_stack = []
        self.last_crud_descriptor_stack = []

    def enterPage(self, ctx: ZmeiLangParser.PageContext):
        self.page = PageDef(self.application)

    def enterPage_name(self, ctx: ZmeiLangParser.Page_nameContext):
        name = ctx.getText()
        if self.parent and self.extend_name:
            name = f'{self.parent}_{name}'
        self.page = self.application.pages[name]

    def enterPage_base(self, ctx: ZmeiLangParser.Page_baseContext):
        self.extend_name = ctx.getText()[-2] == '~'
        self.parent = ctx.getText()[:-2]

    def exitPage(self, ctx: ZmeiLangParser.PageContext):
        self.page = None
        self.parent = None
        self.extend_name = None

    # crud special

    def enterAn_crud(self, ctx: ZmeiLangParser.An_crudContext):
        self.last_crud_descriptor_stack.append(self.last_crud_descriptor)
        if ctx.an_crud_params().an_crud_descriptor():
            self.last_crud_descriptor = ctx.an_crud_params().an_crud_descriptor().getText()
        else:
            self.last_crud_descriptor = None

    enterAn_crud_create = enterAn_crud
    enterAn_crud_delete = enterAn_crud
    enterAn_crud_detail = enterAn_crud
    enterAn_crud_edit = enterAn_crud

    def exitAn_crud(self, ctx: ZmeiLangParser.An_crudContext):
        self.last_crud_descriptor = self.last_crud_descriptor_stack.pop()

    exitAn_crud_create = enterAn_crud
    exitAn_crud_delete = enterAn_crud
    exitAn_crud_detail = enterAn_crud
    exitAn_crud_edit = enterAn_crud

    def enterAn_crud_page_override(self, ctx: ZmeiLangParser.An_crud_page_overrideContext):
        page = self.page
        self.page_stack.append(self.page)

        crud_name = ctx.an_crud_view_name().getText()

        if self.last_crud_descriptor:
            name_suffix = f'_{self.last_crud_descriptor}'
        else:
            name_suffix = ''

        crud_page_name = f"{page.name}{name_suffix}_{crud_name}"

        self.page = page.application.pages[crud_page_name]

    def exitAn_crud_page_override(self, ctx: ZmeiLangParser.An_crud_page_overrideContext):
        self.page = self.page_stack.pop()





