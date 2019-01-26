from zmei_generator.contrib.admin.extras.application.suit import SuitAppExtra
from zmei_generator.parser.gen.ZmeiLangParser import ZmeiLangParser
from zmei_generator.parser.utils import BaseListener


class SuitParserListener(BaseListener):

    def enterAn_suit(self, ctx: ZmeiLangParser.An_suitContext):
        suit = SuitAppExtra(self.application)
        self.application.extras.append(suit)
        self.application.suit = suit

    def enterAn_suit_app_name(self, ctx: ZmeiLangParser.An_suit_app_nameContext):
        self.application.suit.app_name = ctx.getText().strip('"\'')
