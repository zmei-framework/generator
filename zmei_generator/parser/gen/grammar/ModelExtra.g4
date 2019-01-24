parser grammar ModelExtra;

options { tokenVocab=ZmeiLangSimpleLexer; }


import
    ModelExtraAdmin,
    ModelExtraApi,
    ModelExtraRest,
    ModelExtraOrder,
    ModelExtraClean,
    ModelExtraPreDelete,
    ModelExtraTree,
    ModelExtraMixin,
    ModelExtraDateTree,
    ModelExtraM2mChanged,
    ModelExtraPostSave,
    ModelExtraPreSave,
    ModelExtraPostDelete,
    ModelExtraSortable
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
