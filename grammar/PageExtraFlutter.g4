
parser grammar PageExtraFlutter;

options { tokenVocab=ZmeiLangSimpleLexer; }

import Base;

an_flutter:
    AN_FLUTTER
    (BRACE_OPEN
    BRACE_CLOSE)?
    ;
