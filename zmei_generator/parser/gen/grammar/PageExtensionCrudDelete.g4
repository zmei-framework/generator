
parser grammar PageExtensionCrudDelete;

options { tokenVocab=ZmeiLangSimpleLexer; }

import Base,
       PageExtensionCrud
       ;

an_crud_delete:
    AN_CRUD_DELETE
    an_crud_params
    ;
