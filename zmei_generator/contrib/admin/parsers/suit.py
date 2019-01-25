from zmei_generator.contrib.admin.extras.collection_set.suit import SuitCsExtra
from zmei_generator.parser.gen.ZmeiLangParser import ZmeiLangParser
from zmei_generator.parser.utils import BaseListener


class SuitParserListener(BaseListener):

    def enterAn_suit(self, ctx: ZmeiLangParser.An_suitContext):
        suit = SuitCsExtra(self.collection_set)
        self.collection_set.extras.append(suit)
        self.collection_set.suit = suit

    def enterAn_suit_app_name(self, ctx: ZmeiLangParser.An_suit_app_nameContext):
        self.collection_set.suit.app_name = ctx.getText().strip('"\'')
