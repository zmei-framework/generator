
from zmei_generator.domain.extensions import ModelExtension
from zmei_generator.parser.gen.ZmeiLangParser import ZmeiLangParser
from zmei_generator.parser.utils import BaseListener

class DateTreeModelExtension(ModelExtension):
    def get_name(cls):
        return 'date_tree'
    

class DateTreeModelExtensionParserListener(BaseListener):

    def enterAn_date_tree(self, ctx: ZmeiLangParser.An_date_treeContext):
        self.application.extensions.append(
            DateTreeModelExtension(self.model)
        )

    def enterAn_date_tree_field(self, ctx: ZmeiLangParser.An_date_tree_fieldContext):
        self.model.date_hierarchy = ctx.getText()





