parser grammar CsExtra;

options { tokenVocab=ZmeiLangSimpleLexer; }

import
    CsExtraSuit,
    CsExtraCelery,
    CsExtraChannels,
    CsExtraDocker,
    CsExtraFiler,
    CsExtraGitlab,
    CsExtraFile,
    CsExtraTheme,
    CsExtraLangs
    ;

cs_annotation:
     an_suit
    |an_celery
    |an_channels
    |an_docker
    |an_filer
    |an_gitlab
    |an_file
    |an_theme
    |an_langs
    |NL;
