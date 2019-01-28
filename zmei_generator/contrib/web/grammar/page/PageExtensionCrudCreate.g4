
parser grammar PageExtensionCrudCreate;

options { tokenVocab=ZmeiLangSimpleLexer; }

import Base,
       PageExtensionCrud
       ;

an_crud_create:
    AN_CRUD_CREATE
    an_crud_params
    ;
