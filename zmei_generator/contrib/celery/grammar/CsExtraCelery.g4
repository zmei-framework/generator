
parser grammar CsExtraCelery;

options { tokenVocab=ZmeiLangSimpleLexer; }

import Base;

an_celery:
    AN_CELERY
    (BRACE_OPEN
    BRACE_CLOSE)?
    ;
