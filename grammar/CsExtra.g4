parser grammar CsExtra;

options { tokenVocab=ZmeiLangSimpleLexer; }

import
    CsExtraFiler,
    CsExtraLangs,
    CsExtraSuit
    ;

cs_annotation:
     an_suit
    |an_langs
    |an_filer
    |NL
    ;
