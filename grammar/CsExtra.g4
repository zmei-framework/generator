parser grammar CsExtra;

options { tokenVocab=ZmeiLangSimpleLexer; }

import
    CsExtraFiler,
    CsExtraLangs,
    CsExtraCelery,
    CsExtraChannels,
    CsExtraFile,
    CsExtraSuit
    ;

cs_annotation:
     an_suit
    |an_file
    |an_channels
    |an_celery
    |an_langs
    |NL;
