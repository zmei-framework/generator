
parser grammar PageExtraCrud;

options { tokenVocab=ZmeiLangSimpleLexer; }

import Base;

an_crud:
    AN_CRUD
    an_crud_params
    ;

an_crud_params:
    BRACE_OPEN
    NL*
    an_crud_target_model

    (
         an_crud_theme
        |an_crud_skip
        |NL
        |COMA
    )*
    NL*

    BRACE_CLOSE
    ;

an_crud_target_model:
    HASH id_or_kw;

an_crud_theme:
    KW_THEME COLON id_or_kw;

an_crud_skip:
    KW_SKIP COLON an_crud_skip_values;

an_crud_skip_values:
    an_crud_view_name (COMA an_crud_view_name)*;

an_crud_view_name:
     KW_DELETE
    |KW_LIST
    |KW_CREATE
    |KW_EDIT
    |KW_DETAIL
    ;