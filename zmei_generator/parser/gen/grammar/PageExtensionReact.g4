
parser grammar PageExtensionReact;

options { tokenVocab=ZmeiLangSimpleLexer; }

import Base;

an_react:
    (an_react_type)
    (DOT an_react_descriptor)?
    (BRACE_OPEN
    an_react_child?
    BRACE_CLOSE)?
    ;

an_react_type : AN_REACT|AN_REACT_CLIENT|AN_REACT_SERVER ;

an_react_descriptor: id_or_kw;

an_react_child:
    KW_CHILD COLON BOOL;