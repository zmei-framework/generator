parser grammar ModelExtra;

options { tokenVocab=ZmeiLangSimpleLexer; }

import
    ModelExtraSortable,
    ModelExtraOrder,
    ModelExtraRest,
    ModelExtraApi,
    ModelExtraClean,
    ModelExtraPreSave,
    ModelExtraPostSave,
    ModelExtraPreDelete,
    ModelExtraPostDelete,
    ModelExtraM2mChanged,
    ModelExtraMixin,
    ModelExtraAdmin
    ;

model_annotation:
     an_admin
    |an_mixin
    |an_m2m_changed
    |an_post_delete
    |an_pre_delete
    |an_post_save
    |an_pre_save
    |an_clean
    |an_api
    |an_rest
    |an_order
    |an_sortable
    |NL;
