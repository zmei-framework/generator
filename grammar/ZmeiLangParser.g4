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
    NL*
    (
        page_imports?
        page+
    )?
    NL*
    (
        model_imports?
        col+
    )?
    NL*
    EOF
    ;


page_imports : (page_import_statement)+;
model_imports : (model_import_statement)+;

page_import_statement : KW_FROM classname KW_IMPORT import_list NL+;
model_import_statement : KW_FROM classname KW_IMPORT import_list NL+;

import_list: id_or_kw (COMA id_or_kw)*;



