
from zmei_generator.domain.extensions import ModelExtension
from zmei_generator.parser.gen.ZmeiLangParser import ZmeiLangParser
from zmei_generator.parser.utils import BaseListener


class OrderModelExtension(ModelExtension):
    pass

class OrderModelExtensionParserListener(BaseListener):

    def enterAn_order(self, ctx: ZmeiLangParser.An_orderContext):
        self.application.extensions.append(
            OrderModelExtension(self.model)
        )
        self.model.sortable = False

    def enterAn_order_fields(self, ctx: ZmeiLangParser.An_order_fieldsContext):
        self.model.sortable_field = [x.strip() for x in ctx.getText().strip().split(',')]


