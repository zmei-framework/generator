

from zmei_generator.config.domain.collection_def import CollectionDef
from zmei_generator.config.domain.collection_set_def import CollectionSetDef
from zmei_generator.extras.model.api import ApiModelExtraParserListener
from zmei_generator.extras.model.order import OrderModelExtraParserListener
from zmei_generator.extras.model.rest import RestModelExtraParserListener
from zmei_generator.extras.model.sortable import SortableModelExtraParserListener
from zmei_generator.parser.gen.ZmeiLangParser import ZmeiLangParser
from zmei_generator.parser.utils import BaseListener


class ModelExtraListener(
    ApiModelExtraParserListener,
    RestModelExtraParserListener,
    OrderModelExtraParserListener,
    SortableModelExtraParserListener,
    BaseListener
):

    def __init__(self, collection_set: CollectionSetDef) -> None:
        super().__init__(collection_set)

        self.model = None  # type: CollectionDef
        self.model_extend_name = None  # type: CollectionDef
        self.model_base_name = None  # type: CollectionDef

    def enterCol_name(self, ctx: ZmeiLangParser.Col_nameContext):
        ref = ctx.getText().strip()

        if self.model_extend_name:
            ref = '{}_{}'.format(self.model_base_name, ref)

        self.model = self.collection_set.collections[ref]

    def enterCol_base_name(self, ctx: ZmeiLangParser.Col_base_nameContext):
        base = ctx.getText()

        self.model_extend_name = base[-2:] == '~>'
        if self.model_extend_name:
            self.model_base_name = base[:-2].strip()

    def exitCol_name(self, ctx: ZmeiLangParser.Col_nameContext):
        self.model_extend_name = None  # type: CollectionDef
        self.model_base_name = None  # type: CollectionDef



