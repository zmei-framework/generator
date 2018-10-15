from zmei_generator.config.domain.collection_def import CollectionDef
from zmei_generator.config.extras import Extra


class CleanExtra(Extra):

    def parse(self, extra, collection: CollectionDef):
        collection.validators.append(extra.extra_body)


