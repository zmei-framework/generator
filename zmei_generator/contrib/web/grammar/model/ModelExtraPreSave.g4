
parser grammar ModelExtensionPreSave;

options { tokenVocab=ZmeiLangSimpleLexer; }

import Base;

an_pre_save:
    AN_PRE_SAVE
    python_code
    ;
