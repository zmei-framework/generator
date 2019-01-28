
parser grammar ModelExtensionMixin;

options { tokenVocab=ZmeiLangSimpleLexer; }

import Base;

an_mixin:
    AN_MIXIN
    (BRACE_OPEN
    classname
    BRACE_CLOSE)
    ;
