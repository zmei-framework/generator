
parser grammar PageExtraGet;

options { tokenVocab=ZmeiLangSimpleLexer; }

import Base;

an_get:
    AN_GET
    code_block?
    ;