from zmei_generator.parser.gen.ZmeiLangParser import ZmeiLangParser, ParseTreeWalker
from zmei_generator.parser.gen.ZmeiLangParserListener import ZmeiLangParserListener


class SymbolTable(object):

    def __init__(self) -> None:
        self.pages = {}
        self.models = {}

    def page_names(self):
        return list(self.pages.keys())

    def page_fields(self, page):
        return list(self.pages[page])

    def model_names(self):
        return list(self.models.keys())

    def model_fields(self, model):
        return list(self.models[model])

    def update_from_tree(self, tree):
        collector = SymbolCollectorListener(self)
        walker = ParseTreeWalker()
        walker.walk(collector, tree)


class SymbolCollectorListener(ZmeiLangParserListener):

    def __init__(self, symbols) -> None:
        super().__init__()

        self.symbols = symbols

        self._cur_page = None
        self._cur_model = None
        
    # Pages

    def enterPage_name(self, ctx: ZmeiLangParser.Page_nameContext):
        name = ctx.getText()

        self.symbols.pages[name] = []
        self._cur_page = name

    def enterPage_field_name(self, ctx:ZmeiLangParser.Page_field_nameContext):
        self.symbols.pages[self._cur_page].append(ctx.getText())

    # Models

    def enterCol_name(self, ctx:ZmeiLangParser.Col_nameContext):
        name = ctx.getText()

        self.symbols.models[name] = []
        self._cur_model = name

    def enterCol_field_name(self, ctx:ZmeiLangParser.Col_field_nameContext):
        self.symbols.models[self._cur_model].append(ctx.getText())



