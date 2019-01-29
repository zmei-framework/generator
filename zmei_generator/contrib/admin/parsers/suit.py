from zmei_generator.contrib.admin.extensions.application.suit import SuitAppExtension
from zmei_generator.parser.gen.ZmeiLangParser import ZmeiLangParser
from zmei_generator.parser.utils import BaseListener


class SuitParserListener(BaseListener):

    def enterAn_suit(self, ctx: ZmeiLangParser.An_suitContext):
        suit = SuitAppExtension(self.application)
        self.application.extensions.append(suit)
        self.application.register_extension(suit)

    def enterAn_suit_app_name(self, ctx: ZmeiLangParser.An_suit_app_nameContext):
        self.application[SuitAppExtension].app_name = ctx.getText().strip('"\'')
