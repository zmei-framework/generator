from zmei_generator.config.domain.collection_set_extra import CollectionSetExtra


class SuitCsExtra(CollectionSetExtra):

    @classmethod
    def get_name(cls):
        return 'suit'

    def get_required_apps(self):
        return ['suit']

    def get_required_deps(self):
        return ['django-suit']








