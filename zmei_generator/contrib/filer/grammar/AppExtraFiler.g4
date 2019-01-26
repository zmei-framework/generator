
parser grammar AppExtraFiler;

options { tokenVocab=ZmeiLangSimpleLexer; }

import Base;

an_filer:
    AN_FILER
    (BRACE_OPEN
    BRACE_CLOSE)?
    ;
