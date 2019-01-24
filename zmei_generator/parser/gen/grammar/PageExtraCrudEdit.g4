
parser grammar PageExtraCrudEdit;

options { tokenVocab=ZmeiLangSimpleLexer; }

import Base,
       PageExtraCrud
       ;

an_crud_edit:
    AN_CRUD_EDIT
    an_crud_params
    ;
