from zmei_generator.domain.extras import Extra


class CollectionSetExtra(Extra):

    def __init__(self, collection_set):
        super().__init__()

        self.collection_set = collection_set



