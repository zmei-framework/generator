from zmei_generator.contrib.drf.extras.model.api import ApiModelExtraParserListener
from zmei_generator.contrib.drf.extras.model.rest import RestModelExtraParserListener
from zmei_generator.contrib.web.extras.model.clean import CleanModelExtraParserListener
from zmei_generator.contrib.web.extras.model.date_tree import DateTreeModelExtraParserListener
from zmei_generator.contrib.web.extras.model.m2m_changed import M2mChangedModelExtraParserListener
from zmei_generator.contrib.web.extras.model.mixin import MixinModelExtraParserListener
from zmei_generator.contrib.web.extras.model.order import OrderModelExtraParserListener
from zmei_generator.contrib.web.extras.model.post_delete import PostDeleteModelExtraParserListener
from zmei_generator.contrib.web.extras.model.post_save import PostSaveModelExtraParserListener
from zmei_generator.contrib.web.extras.model.pre_delete import PreDeleteModelExtraParserListener
from zmei_generator.contrib.web.extras.model.pre_save import PreSaveModelExtraParserListener
from zmei_generator.contrib.web.extras.model.sortable import SortableModelExtraParserListener
from zmei_generator.contrib.web.extras.model.tree import TreeModelExtraParserListener

parsers = [
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
]