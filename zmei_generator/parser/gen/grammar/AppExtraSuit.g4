
parser grammar AppExtensionSuit;

options { tokenVocab=ZmeiLangSimpleLexer; }

import Base;

an_suit:
    AN_SUIT
    (BRACE_OPEN
    an_suit_app_name
    BRACE_CLOSE)?
    ;
an_suit_app_name : STRING_DQ | STRING_SQ ;
