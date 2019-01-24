
parser grammar PageExtraCrudDetail;

options { tokenVocab=ZmeiLangSimpleLexer; }

import Base,
       PageExtraCrud
       ;

an_crud_detail:
    AN_CRUD_DETAIL
    an_crud_params
    ;
