
parser grammar AppExtensionCelery;

options { tokenVocab=ZmeiLangSimpleLexer; }

import Base;

an_celery:
    AN_CELERY
    (BRACE_OPEN
    BRACE_CLOSE)?
    ;
