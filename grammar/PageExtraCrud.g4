
parser grammar PageExtraCrud;

options { tokenVocab=ZmeiLangSimpleLexer; }

import Base;

an_crud:
    AN_CRUD
    an_crud_params
    ;

an_crud_params:
    BRACE_OPEN
    an_crud_target_model
    BRACE_CLOSE
    ;

an_crud_target_model:
    HASH id_or_kw;
