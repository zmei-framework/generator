from zmei_generator.config.domain.collection_def import CollectionDef
from zmei_generator.config.extras import Extra


class TreeExtra(Extra):

    def parse(self, extra, collection: CollectionDef):
        collection.tree = True

        if extra.extra_body.strip() == '+polymorphic_list':
            collection.tree_polymorphic_list = True


        collection.collection_set.add_deps([
            'django-mptt',
            'django-polymorphic-tree',
        ])
        collection.collection_set.add_apps([
            'mptt',
            'polymorphic_tree',
            'polymorphic',
        ])

