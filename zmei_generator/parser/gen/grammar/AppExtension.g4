parser grammar AppExtension;

options { tokenVocab=ZmeiLangSimpleLexer; }

import
    AppExtensionSuit,
    AppExtensionCelery,
    AppExtensionChannels,
    AppExtensionDocker,
    AppExtensionFiler,
    AppExtensionGitlab,
    AppExtensionFile,
    AppExtensionTheme,
    AppExtensionLangs
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
