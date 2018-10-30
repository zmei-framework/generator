
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
