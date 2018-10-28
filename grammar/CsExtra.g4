parser grammar CsExtra;

options { tokenVocab=ZmeiLangSimpleLexer; }

import
    CsExtraFiler,
    CsExtraLangs,
    CsExtraCelery,
    CsExtraSuit
    ;

cs_annotation:
     an_suit
    |an_celery
    |an_langs
    |NL;
