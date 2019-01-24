
parser grammar PageExtraCrudList;

options { tokenVocab=ZmeiLangSimpleLexer; }

import Base,
       PageExtraCrud
       ;

an_crud_list:
    AN_CRUD_LIST
    an_crud_params
    ;
