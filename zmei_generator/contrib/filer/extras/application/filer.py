from zmei_generator.domain.application_extra import ApplicationExtra
from zmei_generator.parser.gen.ZmeiLangParser import ZmeiLangParser
from zmei_generator.parser.utils import BaseListener


class FilerAppExtra(ApplicationExtra):

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
        if self.application.suit:
            self.application.suit.menu = [
                {'label': 'Files & folders', 'app': 'filer'}
            ] + self.application.suit.menu


class FilerAppExtraParserListener(BaseListener):

    def enterAn_filer(self, ctx: ZmeiLangParser.An_filerContext):
        self.application.filer = FilerAppExtra(self.application)

        self.application.extras.append(
            self.application.filer
        )
