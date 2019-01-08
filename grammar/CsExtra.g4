parser grammar CsExtra;

options { tokenVocab=ZmeiLangSimpleLexer; }

import
    CsExtraFiler,
    CsExtraLangs,
    CsExtraCelery,
    CsExtraChannels,
    CsExtraFile,
    CsExtraDocker,
    CsExtraGitlab,
    CsExtraSuit
    ;

cs_annotation:
     an_suit
    |an_gitlab
    |an_docker
    |an_file
    |an_channels
    |an_celery
    |an_langs
    |NL;
