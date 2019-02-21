
parser grammar PageExtensionFlutter;

options { tokenVocab=ZmeiLangSimpleLexer; }

import Base;

an_flutter:
    AN_FLUTTER
    (BRACE_OPEN
    an_flutter_child?
    BRACE_CLOSE)?
    ;
an_flutter_child:
    KW_CHILD COLON BOOL;