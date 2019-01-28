
parser grammar AppExtensionLangs;

options { tokenVocab=ZmeiLangSimpleLexer; }

import Base;

an_langs:
    AN_LANGS
    BRACE_OPEN
    an_langs_list
    BRACE_CLOSE
    ;

an_langs_list: ID (COMA ID)*;