
parser grammar PageExtraReact;

options { tokenVocab=ZmeiLangSimpleLexer; }

import Base;

an_react:
    AN_REACT
    (DOT an_react_descriptor)?
    code_block
    ;

an_react_descriptor: id_or_kw;