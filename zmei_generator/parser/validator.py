from zmei_generator.parser.errors import PageParentValidationError
from zmei_generator.parser.gen.ZmeiLangParser import ZmeiLangParser, ParseTreeWalker
from zmei_generator.parser.gen.ZmeiLangParserListener import ZmeiLangParserListener


class ValidationListener(ZmeiLangParserListener):

    def __init__(self, symbols) -> None:
        super().__init__()

        self.symbols = symbols

        self.errors = []

        self.suit = False

    # Pages

    def enterPage_base(self, ctx: ZmeiLangParser.Page_baseContext):
        name = ctx.getText()[:-2]

        if name not in self.symbols.pages:
            self.errors.append(PageParentValidationError(ctx.id_or_kw()[0].start, name))


def validate(tree, symbols):
    validator = ValidationListener(symbols)
    walker = ParseTreeWalker()
    walker.walk(validator, tree)

    return validator.errors

