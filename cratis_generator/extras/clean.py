from cratis_generator.config.domain import CollectionDef
from cratis_generator.config.extras import Extra


class CleanExtra(Extra):

    @classmethod
    def get_name(cls):
        return 'clean'

    def parse(self, extra, collection: CollectionDef):
        collection.validators.append(extra.extra_body)


