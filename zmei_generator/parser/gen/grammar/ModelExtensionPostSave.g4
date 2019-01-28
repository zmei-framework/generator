
parser grammar ModelExtensionPostSave;

options { tokenVocab=ZmeiLangSimpleLexer; }

import Base;

an_post_save:
    AN_POST_SAVE
    python_code
    ;
