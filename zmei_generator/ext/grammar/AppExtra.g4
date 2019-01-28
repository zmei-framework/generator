parser grammar AppExtension;

options { tokenVocab=ZmeiLangSimpleLexer; }

import
    // {EXTENSION_IMPORTS}
    ;

cs_annotation:
    // {EXTENSION_ANNOT}
    |NL;
