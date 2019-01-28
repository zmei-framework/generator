
parser grammar PageExtensionError;

options { tokenVocab=ZmeiLangSimpleLexer; }

import Base;

an_error:
    AN_ERROR
    BRACE_OPEN
    an_error_code
    BRACE_CLOSE
    ;

an_error_code: DIGIT;
