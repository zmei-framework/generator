
parser grammar ModelExtensionApi;

options { tokenVocab=ZmeiLangSimpleLexer; }

import Base;

an_api:
    AN_API
    (BRACE_OPEN
    (
         an_api_all
        |an_api_name (COMA an_api_name)*
    )
    BRACE_CLOSE)?
    ;

an_api_all: STAR;
an_api_name : id_or_kw;
