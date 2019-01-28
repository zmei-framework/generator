
parser grammar ModelExtensionClean;

options { tokenVocab=ZmeiLangSimpleLexer; }

import Base;

an_clean:
    AN_CLEAN
    python_code
    ;
