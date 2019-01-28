parser grammar ModelExtension;

options { tokenVocab=ZmeiLangSimpleLexer; }


import
    // {EXTENSION_IMPORTS}
    ;

model_annotation:
    // {EXTENSION_ANNOT}
    |NL;
