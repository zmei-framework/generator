
parser grammar PageExtraAuth;

options { tokenVocab=ZmeiLangSimpleLexer; }

import Base;

an_auth:
    AN_AUTH
    (code_block)?
    ;
