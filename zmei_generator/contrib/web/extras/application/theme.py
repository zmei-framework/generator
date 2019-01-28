
from zmei_generator.domain.extensions import ApplicationExtension
from zmei_generator.generator.utils import ThemeConfig
from zmei_generator.parser.gen.ZmeiLangParser import ZmeiLangParser
from zmei_generator.parser.utils import BaseListener

class ThemeAppExtension(ApplicationExtension):
    def get_name(cls):
        return 'theme'
    

class ThemeAppExtensionParserListener(BaseListener):

    def enterAn_theme(self, ctx: ZmeiLangParser.An_themeContext):
        self.application.extensions.append(
            ThemeAppExtension(self.application)
        )

    def enterAn_theme_name(self, ctx: ZmeiLangParser.An_theme_nameContext):
        self.application.theme = ctx.getText().strip("'\" ")
        # TODO: that's baaad. We need make theming some normal way.
        ThemeConfig.theme = self.application.theme

    def enterAn_theme_install(self, ctx: ZmeiLangParser.An_theme_installContext):
        self.application.theme_install = ctx.getText() == 'true'





