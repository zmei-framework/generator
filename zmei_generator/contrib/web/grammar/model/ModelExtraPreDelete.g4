
parser grammar ModelExtensionPreDelete;

options { tokenVocab=ZmeiLangSimpleLexer; }

import Base;

an_pre_delete:
    AN_PRE_DELETE
    python_code
    ;
