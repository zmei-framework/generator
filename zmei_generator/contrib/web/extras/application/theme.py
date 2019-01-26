
from zmei_generator.domain.application_extra import ApplicationExtra
from zmei_generator.parser.gen.ZmeiLangParser import ZmeiLangParser
from zmei_generator.parser.utils import BaseListener

class ThemeAppExtra(ApplicationExtra):
    def get_name(cls):
        return 'theme'
    

class ThemeAppExtraParserListener(BaseListener):

    def enterAn_theme(self, ctx: ZmeiLangParser.An_themeContext):
        self.application.extras.append(
            ThemeAppExtra(self.application)
        )

    def enterAn_theme_name(self, ctx: ZmeiLangParser.An_theme_nameContext):
        self.application.theme = ctx.getText().strip("'\" ")

    def enterAn_theme_install(self, ctx: ZmeiLangParser.An_theme_installContext):
        self.application.theme_install = ctx.getText() == 'true'





