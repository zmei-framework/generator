parser grammar ZmeiLangParser;

options { tokenVocab=ZmeiLangSimpleLexer; }

import Base,
       CsExtra,
       Model,
       Page
       ;



col_file:
    NL*
    cs_annotation*
    page_imports?
    NL*
    page*
    model_imports?
    col*
    NL*
    EOF
    ;



page_imports : KW_IMPORT import_source;
model_imports : KW_IMPORT import_source;

import_source : code_block;

