from zmei_generator.config.domain.collection_set_extra import CollectionSetExtra
from zmei_generator.parser.gen.ZmeiLangParser import ZmeiLangParser
from zmei_generator.parser.utils import BaseListener


class FilerCsExtra(CollectionSetExtra):

    @classmethod
    def get_name(cls):
        return 'filer'

    def get_required_deps(self):
        return ['git+git://github.com/nephila/django-filer@feature/django-2.0#egg=django-filer']

    def get_required_apps(self):
        return [
            'easy_thumbnails',
            'filer',
            'mptt',
        ]

    @classmethod
    def write_settings(cls, apps, f):
        f.write('\nTHUMBNAIL_HIGH_RESOLUTION = True\n')

    def post_process(self):
        if self.collection_set.suit:
            self.collection_set.suit.menu = [
                {'label': 'Files & folders', 'app': 'filer'}
            ] + self.collection_set.suit.menu


class FilerCsExtraParserListener(BaseListener):

    def enterAn_filer(self, ctx: ZmeiLangParser.An_filerContext):
        self.collection_set.filer = FilerCsExtra(self.collection_set)

        self.collection_set.extras.append(
            self.collection_set.filer
        )
