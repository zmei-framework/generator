
parser grammar PageExtensionCrudList;

options { tokenVocab=ZmeiLangSimpleLexer; }

import Base,
       PageExtensionCrud
       ;

an_crud_list:
    AN_CRUD_LIST
    an_crud_params
    ;
