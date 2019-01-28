parser grammar ZmeiLangParser;

options { tokenVocab=ZmeiLangSimpleLexer; }

import Base,
       AppExtension,
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

page_import_statement: import_statement;
model_import_statement: import_statement;

import_statement: (KW_FROM import_source)? KW_IMPORT import_list NL+;

import_source: DOT? classname;
import_list: import_item (COMA import_item)*;

import_item: (import_item_name (KW_AS import_item_alias)?) | import_item_all;
import_item_name: classname;
import_item_alias: id_or_kw;
import_item_all: STAR;
