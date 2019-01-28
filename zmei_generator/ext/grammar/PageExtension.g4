parser grammar PageExtension;

options { tokenVocab=ZmeiLangSimpleLexer; }

import
    // {EXTENSION_IMPORTS}
    ;

page_annotation:
    // {EXTENSION_ANNOT}
    |NL;

