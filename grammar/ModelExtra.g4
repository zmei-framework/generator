parser grammar ModelExtra;

options { tokenVocab=ZmeiLangSimpleLexer; }

import
    ModelExtraSortable,
    ModelExtraOrder,
    ModelExtraRest,
    ModelExtraApi,
    ModelExtraAdmin
    ;

model_annotation:
     an_admin
    |an_api
    |an_rest
    |an_order
    |an_sortable
    |NL;
