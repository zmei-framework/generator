
parser grammar PageExtraPost;

options { tokenVocab=ZmeiLangSimpleLexer; }

import Base;

an_post:
    AN_POST
    code_block?
    ;
