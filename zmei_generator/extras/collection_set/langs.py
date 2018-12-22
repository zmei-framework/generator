from django.conf.locale import LANG_INFO

from zmei_generator.config.domain.collection_set_def import CollectionSetDef
from zmei_generator.config.domain.collection_set_extra import CollectionSetExtra
from zmei_generator.parser.gen.ZmeiLangParser import ZmeiLangParser
from zmei_generator.parser.utils import BaseListener


class LangsCsExtra(CollectionSetExtra):

    def __init__(self, collection_set):
        super().__init__(collection_set)

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
        for cs in apps.values():
            if not cs.langs:
                continue
            for code in cs.langs.langs:
                name = LANG_INFO[code]['name_local'].capitalize()
                _langs[code] = name

        if len(_langs) == 0:
            _langs = {'en': 'English'}

        langs = tuple([(code, name) for code, name in _langs.items()])

        f.write('\n# LANGUAGE SETTINGS')
        f.write('\nLANGUAGES = {}'.format(repr(langs)))
        f.write('\nMAIN_LANGUAGE = {}\n'.format(repr(langs[0][0])))
        f.write('\nMIDDLEWARE += ["django.middleware.locale.LocaleMiddleware"]')
        f.write("\nLOCALE_PATHS = [os.path.join(BASE_DIR, 'locale')]")


class LangsCsExtraParserListener(BaseListener):

    def __init__(self, collection_set: CollectionSetDef) -> None:
        super().__init__(collection_set)

        self.langs_extra = None

    def enterAn_langs(self, ctx: ZmeiLangParser.An_langsContext):
        self.langs_extra = LangsCsExtra(self.collection_set)
        self.collection_set.extras.append(self.langs_extra)
        self.collection_set.langs = self.langs_extra

    def exitAn_langs(self, ctx: ZmeiLangParser.An_langsContext):
        self.langs_extra = None

    def enterAn_langs_list(self, ctx: ZmeiLangParser.An_langs_listContext):
        self.langs_extra.langs = [x.strip() for x in ctx.getText().split(',')]



