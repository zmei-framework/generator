
parser grammar PageExtraReact;

options { tokenVocab=ZmeiLangSimpleLexer; }

import Base;

an_react:
    AN_REACT
    code_block
    ;
