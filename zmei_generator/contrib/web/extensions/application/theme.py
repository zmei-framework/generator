from zmei_generator.domain.application_def import ApplicationDef
from zmei_generator.domain.extensions import ApplicationExtension
from zmei_generator.generator.utils import ThemeConfig
from zmei_generator.parser.gen.ZmeiLangParser import ZmeiLangParser
from zmei_generator.parser.utils import BaseListener


class ThemeAppExtension(ApplicationExtension):
    def __init__(self, application):
        super().__init__(application)

        self.theme = None
        self.theme_install = False

    def get_name(cls):
        return 'theme'

    def post_process(self):
        super().post_process()

        ThemeConfig.theme = self.theme


class ThemeAppExtensionParserListener(BaseListener):
    def __init__(self, application: ApplicationDef) -> None:
        super().__init__(application)
        self.theme_extension = None

    def enterAn_theme(self, ctx: ZmeiLangParser.An_themeContext):
        extension = ThemeAppExtension(self.application)
        self.application.extensions.append(
            extension
        )
        self.theme_extension = extension
        self.application.register_extension(extension)

    def enterAn_theme_name(self, ctx: ZmeiLangParser.An_theme_nameContext):
        self.theme_extension.theme = ctx.getText().strip("'\" ")

    def enterAn_theme_install(self, ctx: ZmeiLangParser.An_theme_installContext):
        self.theme_extension.theme_install = ctx.getText() == 'true'





