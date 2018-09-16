from abc import abstractmethod

from zmei_generator.config.domain.collection_def import CollectionDef
from zmei_generator.config.extras import Extra


class DbSignalExtra(Extra):

    @abstractmethod
    def get_signal(self):
        pass

    def parse(self, extra, collection: CollectionDef):
        source = extra.extra_body.strip()

        collection.signal_handlers.append((self.get_signal(), source))


class PreSaveExtra(DbSignalExtra):

    @classmethod
    def get_name(cls):
        return 'pre_save'

    def get_signal(self):
        return ['django.db.models.signals', 'pre_save']


class PostSaveExtra(DbSignalExtra):

    @classmethod
    def get_name(cls):
        return 'post_save'

    def get_signal(self):
        return ['django.db.models.signals', 'post_save']


class PreDeleteExtra(DbSignalExtra):

    @classmethod
    def get_name(cls):
        return 'pre_delete'

    def get_signal(self):
        return ['django.db.models.signals', 'pre_delete']


class PostDeleteExtra(DbSignalExtra):

    @classmethod
    def get_name(cls):
        return 'post_delete'

    def get_signal(self):
        return ['django.db.models.signals', 'post_delete']


class M2mChangedExtra(DbSignalExtra):

    @classmethod
    def get_name(cls):
        return 'm2m_changed'

    def get_signal(self):
        return ['django.db.models.signals', 'm2m_changed']





