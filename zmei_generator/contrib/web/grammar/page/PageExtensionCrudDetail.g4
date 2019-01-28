
parser grammar PageExtensionCrudDetail;

options { tokenVocab=ZmeiLangSimpleLexer; }

import Base,
       PageExtensionCrud
       ;

an_crud_detail:
    AN_CRUD_DETAIL
    an_crud_params
    ;
