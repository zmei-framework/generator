
from zmei_generator.config.extras import ModelExtra
from zmei_generator.parser.gen.ZmeiLangParser import ZmeiLangParser
from zmei_generator.parser.utils import BaseListener


class OrderModelExtra(ModelExtra):
    pass

class OrderModelExtraParserListener(BaseListener):

    def enterAn_order(self, ctx: ZmeiLangParser.An_orderContext):
        self.collection_set.extras.append(
            OrderModelExtra(self.model)
        )
        self.model.sortable = False

    def enterAn_order_fields(self, ctx: ZmeiLangParser.An_order_fieldsContext):
        self.model.sortable_field = [x.strip() for x in ctx.getText().strip().split(',')]


