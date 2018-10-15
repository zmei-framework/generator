
from zmei_generator.config.extras import ModelExtra
from zmei_generator.parser.gen.ZmeiLangParser import ZmeiLangParser
from zmei_generator.parser.utils import BaseListener

class DateTreeModelExtra(ModelExtra):
    def get_name(cls):
        return 'date_tree'
    

class DateTreeModelExtraParserListener(BaseListener):

    def enterAn_date_tree(self, ctx: ZmeiLangParser.An_date_treeContext):
        self.collection_set.extras.append(
            DateTreeModelExtra(self.model)
        )

    def enterAn_date_tree_field(self, ctx: ZmeiLangParser.An_date_tree_fieldContext):
        self.model.date_hierarchy = ctx.getText()





