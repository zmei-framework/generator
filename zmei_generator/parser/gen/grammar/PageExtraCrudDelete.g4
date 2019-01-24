
parser grammar PageExtraCrudDelete;

options { tokenVocab=ZmeiLangSimpleLexer; }

import Base,
       PageExtraCrud
       ;

an_crud_delete:
    AN_CRUD_DELETE
    an_crud_params
    ;
