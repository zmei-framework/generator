
from zmei_generator.config.domain.collection_set_extra import CollectionSetExtra
from zmei_generator.parser.gen.ZmeiLangParser import ZmeiLangParser
from zmei_generator.parser.utils import BaseListener

class ThemeCsExtra(CollectionSetExtra):
    def get_name(cls):
        return 'theme'
    

class ThemeCsExtraParserListener(BaseListener):

    def enterAn_theme(self, ctx: ZmeiLangParser.An_themeContext):
        self.collection_set.extras.append(
            ThemeCsExtra(self.collection_set)
        )

    def enterAn_theme_name(self, ctx: ZmeiLangParser.An_theme_nameContext):
        self.collection_set.theme = ctx.getText().strip("'\" ")

    def enterAn_theme_install(self, ctx: ZmeiLangParser.An_theme_installContext):
        self.collection_set.theme_install = ctx.getText() == 'true'





