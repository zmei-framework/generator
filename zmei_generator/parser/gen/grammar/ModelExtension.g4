parser grammar ModelExtension;

options { tokenVocab=ZmeiLangSimpleLexer; }


import
    ModelExtensionAdmin,
    ModelExtensionApi,
    ModelExtensionRest,
    ModelExtensionOrder,
    ModelExtensionClean,
    ModelExtensionPreDelete,
    ModelExtensionTree,
    ModelExtensionMixin,
    ModelExtensionDateTree,
    ModelExtensionM2mChanged,
    ModelExtensionPostSave,
    ModelExtensionPreSave,
    ModelExtensionPostDelete,
    ModelExtensionSortable
    ;

model_annotation:
     an_admin
    |an_api
    |an_rest
    |an_order
    |an_clean
    |an_pre_delete
    |an_tree
    |an_mixin
    |an_date_tree
    |an_m2m_changed
    |an_post_save
    |an_pre_save
    |an_post_delete
    |an_sortable
    |NL;
