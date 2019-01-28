
parser grammar AppExtensionDocker;

options { tokenVocab=ZmeiLangSimpleLexer; }

import Base;

an_docker:
    AN_DOCKER
    (BRACE_OPEN
    BRACE_CLOSE)?
    ;
