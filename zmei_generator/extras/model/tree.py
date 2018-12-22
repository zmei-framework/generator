
from zmei_generator.config.extras import ModelExtra
from zmei_generator.parser.gen.ZmeiLangParser import ZmeiLangParser
from zmei_generator.parser.utils import BaseListener

class TreeModelExtra(ModelExtra):
    def get_required_deps(self):
        return ['django-mptt']

    def get_name(cls):
        return 'tree'
    

class TreeModelExtraParserListener(BaseListener):

    def enterAn_tree(self, ctx: ZmeiLangParser.An_treeContext):
        self.collection_set.extras.append(
            TreeModelExtra(self.model)
        )

        self.model.tree = True

        self.collection_set.add_deps([
            'django-mptt',
            'django-polymorphic-tree',
        ])
        self.collection_set.add_apps([
            'mptt',
            'polymorphic_tree',
            'polymorphic',
        ])

    def enterAn_tree_poly(self, ctx: ZmeiLangParser.An_tree_polyContext):
        self.model.tree_polymorphic_list = True



