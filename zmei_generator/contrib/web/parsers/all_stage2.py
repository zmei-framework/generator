from zmei_generator.contrib.drf.extensions.model.api import ApiModelExtensionParserListener
from zmei_generator.contrib.drf.extensions.model.rest import RestModelExtensionParserListener
from zmei_generator.contrib.web.extensions.model.clean import CleanModelExtensionParserListener
from zmei_generator.contrib.web.extensions.model.date_tree import DateTreeModelExtensionParserListener
from zmei_generator.contrib.web.extensions.model.m2m_changed import M2mChangedModelExtensionParserListener
from zmei_generator.contrib.web.extensions.model.mixin import MixinModelExtensionParserListener
from zmei_generator.contrib.web.extensions.model.order import OrderModelExtensionParserListener
from zmei_generator.contrib.web.extensions.model.post_delete import PostDeleteModelExtensionParserListener
from zmei_generator.contrib.web.extensions.model.post_save import PostSaveModelExtensionParserListener
from zmei_generator.contrib.web.extensions.model.pre_delete import PreDeleteModelExtensionParserListener
from zmei_generator.contrib.web.extensions.model.pre_save import PreSaveModelExtensionParserListener
from zmei_generator.contrib.web.extensions.model.sortable import SortableModelExtensionParserListener
from zmei_generator.contrib.web.extensions.model.tree import TreeModelExtensionParserListener

parsers = [
    TreeModelExtensionParserListener,
    DateTreeModelExtensionParserListener,
    MixinModelExtensionParserListener,
    M2mChangedModelExtensionParserListener,
    PostDeleteModelExtensionParserListener,
    PreDeleteModelExtensionParserListener,
    PostSaveModelExtensionParserListener,
    PreSaveModelExtensionParserListener,
    CleanModelExtensionParserListener,
    ApiModelExtensionParserListener,
    RestModelExtensionParserListener,
    OrderModelExtensionParserListener,
    SortableModelExtensionParserListener,
]