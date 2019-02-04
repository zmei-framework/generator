from django.conf.locale import LANG_INFO

from zmei_generator.domain.application_def import ApplicationDef
from zmei_generator.domain.extensions import ApplicationExtension
from zmei_generator.parser.errors import ValidationError
from zmei_generator.parser.gen.ZmeiLangParser import ZmeiLangParser
from zmei_generator.parser.utils import BaseListener


class LangsAppExtension(ApplicationExtension):

    def __init__(self, application):
        super().__init__(application)

        self.langs = None

    def get_name(cls):
        return 'langs'

    def get_required_deps(self):
        return ['django-modeltranslation==0.13-beta1']

    def get_required_apps(self):
        return ['modeltranslation']

    @classmethod
    def write_settings(cls, apps, f):
        _langs = {}
        for app in apps.values():
            if not app.supports(LangsAppExtension):
                continue
            for code in app[LangsAppExtension].langs:
                try:
                    name = LANG_INFO[code]['name_local'].capitalize()
                    _langs[code] = name
                except KeyError:
                    raise ValidationError(0,0, f'Unknown language {code}. Available options are: {", ".join(LANG_INFO.keys())}')

        if len(_langs) == 0:
            _langs = {'en': 'English'}

        langs = tuple([(code, name) for code, name in _langs.items()])

        f.write('\n# LANGUAGE SETTINGS')
        f.write('\nLANGUAGES = {}'.format(repr(langs)))
        f.write('\nMAIN_LANGUAGE = {}\n'.format(repr(langs[0][0])))
        f.write('\nMIDDLEWARE += ["django.middleware.locale.LocaleMiddleware"]')
        f.write("\nLOCALE_PATHS = [os.path.join(BASE_DIR, 'locale')]")


class LangsAppExtensionParserListener(BaseListener):

    def __init__(self, application: ApplicationDef) -> None:
        super().__init__(application)

        self.langs_extension = None

    def enterAn_langs(self, ctx: ZmeiLangParser.An_langsContext):
        self.langs_extension = LangsAppExtension(self.application)
        self.application.extensions.append(self.langs_extension)
        self.application.register_extension(self.langs_extension)

    def exitAn_langs(self, ctx: ZmeiLangParser.An_langsContext):
        self.langs_extension = None

    def enterAn_langs_list(self, ctx: ZmeiLangParser.An_langs_listContext):
        self.langs_extension.langs = [x.strip() for x in ctx.getText().split(',')]



