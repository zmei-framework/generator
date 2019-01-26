parser grammar AppExtra;

options { tokenVocab=ZmeiLangSimpleLexer; }

import
    AppExtraSuit,
    AppExtraCelery,
    AppExtraChannels,
    AppExtraDocker,
    AppExtraFiler,
    AppExtraGitlab,
    AppExtraFile,
    AppExtraTheme,
    AppExtraLangs
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
