parser grammar CsExtra;

options { tokenVocab=ZmeiLangSimpleLexer; }

import
    CsExtraFiler,
    CsExtraLangs,
    CsExtraCelery,
    CsExtraChannels,
    CsExtraSuit
    ;

cs_annotation:
     an_suit
    |an_channels
    |an_celery
    |an_langs
    |NL;
