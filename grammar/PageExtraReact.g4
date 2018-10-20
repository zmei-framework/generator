
parser grammar PageExtraReact;

options { tokenVocab=ZmeiLangSimpleLexer; }

import Base;

an_react:
    AN_REACT
    (DOT an_react_discriminator)?
    code_block
    ;

an_react_discriminator: id_or_kw;