

from zmei_generator.config.domain.collection_def import CollectionDef
from zmei_generator.config.domain.collection_set_def import CollectionSetDef
from zmei_generator.extras.model.api import ApiModelExtraParserListener
from zmei_generator.extras.model.order import OrderModelExtraParserListener
from zmei_generator.extras.model.rest import RestModelExtraParserListener
from zmei_generator.extras.model.sortable import SortableModelExtraParserListener
from zmei_generator.parser.gen.ZmeiLangParser import ZmeiLangParser
from zmei_generator.parser.utils import BaseListener
from zmei_generator.extras.model.tree import TreeModelExtraParserListener
from zmei_generator.extras.model.date_tree import DateTreeModelExtraParserListener
from zmei_generator.extras.model.mixin import MixinModelExtraParserListener
from zmei_generator.extras.model.m2m_changed import M2mChangedModelExtraParserListener
from zmei_generator.extras.model.post_delete import PostDeleteModelExtraParserListener
from zmei_generator.extras.model.pre_delete import PreDeleteModelExtraParserListener
from zmei_generator.extras.model.post_save import PostSaveModelExtraParserListener
from zmei_generator.extras.model.pre_save import PreSaveModelExtraParserListener
from zmei_generator.extras.model.clean import CleanModelExtraParserListener


class ModelExtraListener(
    TreeModelExtraParserListener,
    DateTreeModelExtraParserListener,
    MixinModelExtraParserListener,
    M2mChangedModelExtraParserListener,
    PostDeleteModelExtraParserListener,
    PreDeleteModelExtraParserListener,
    PostSaveModelExtraParserListener,
    PreSaveModelExtraParserListener,
    CleanModelExtraParserListener,
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



