from zmei_generator.config.domain.collection_set_extra import CollectionSetExtra
from zmei_generator.generator.utils import generate_file
from zmei_generator.parser.gen.ZmeiLangParser import ZmeiLangParser
from zmei_generator.parser.utils import BaseListener


class CeleryCsExtra(CollectionSetExtra):
    def get_name(cls):
        return 'celery'

    def get_required_deps(self):
        return [
            'celery'
        ]

    @classmethod
    def generate(cls, apps, target_path):
        generate_file(target_path, 'app/celery.py', template_name='celery.py.tpl')
        generate_file(target_path, 'app/__init__.py', template_name='celery_init.py.tpl')


class CeleryCsExtraParserListener(BaseListener):

    def enterAn_celery(self, ctx: ZmeiLangParser.An_celeryContext):
        self.collection_set.extras.append(
            CeleryCsExtra(self.collection_set)
        )
