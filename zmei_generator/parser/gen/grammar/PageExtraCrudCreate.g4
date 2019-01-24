
parser grammar PageExtraCrudCreate;

options { tokenVocab=ZmeiLangSimpleLexer; }

import Base,
       PageExtraCrud
       ;

an_crud_create:
    AN_CRUD_CREATE
    an_crud_params
    ;
