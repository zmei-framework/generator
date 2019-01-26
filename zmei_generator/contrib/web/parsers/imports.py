from zmei_generator.domain.application_def import ApplicationDef
from zmei_generator.parser.gen.ZmeiLangParser import ZmeiLangParser
from zmei_generator.parser.utils import BaseListener


class ImportsParserListener(BaseListener):
    def __init__(self, application: ApplicationDef) -> None:
        super().__init__(application)

        self.import_from = None
        self.import_list = []

    def enterImport_statement(self, ctx: ZmeiLangParser.Import_statementContext):
        self.import_from = None
        self.import_list = []

    def enterImport_source(self, ctx: ZmeiLangParser.Import_sourceContext):
        self.import_from = ctx.getText()

    def enterImport_item(self, ctx: ZmeiLangParser.Import_itemContext):
        if ctx.import_item_all():
            name = '*'
        else:
            name = ctx.import_item_name().getText()
            if ctx.import_item_alias():
                name += ' as ' + ctx.import_item_alias().getText()
        self.import_list.append(name)

    def exitPage_import_statement(self, ctx: ZmeiLangParser.Page_import_statementContext):
        self.application.page_imports.add(self.import_from, *self.import_list)

    def exitModel_import_statement(self, ctx: ZmeiLangParser.Model_import_statementContext):
        self.application.model_imports.add(self.import_from, *self.import_list)
