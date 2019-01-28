
parser grammar ModelExtensionPostDelete;

options { tokenVocab=ZmeiLangSimpleLexer; }

import Base;

an_post_delete:
    AN_POST_DELETE
    python_code
    ;
