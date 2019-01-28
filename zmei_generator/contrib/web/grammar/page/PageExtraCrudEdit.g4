
parser grammar PageExtensionCrudEdit;

options { tokenVocab=ZmeiLangSimpleLexer; }

import Base,
       PageExtensionCrud
       ;

an_crud_edit:
    AN_CRUD_EDIT
    an_crud_params
    ;
