
parser grammar ModelExtraMixin;

options { tokenVocab=ZmeiLangSimpleLexer; }

import Base;

an_mixin:
    AN_MIXIN
    (BRACE_OPEN
    classname
    BRACE_CLOSE)
    ;
