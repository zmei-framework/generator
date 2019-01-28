
parser grammar AppExtensionFile;

options { tokenVocab=ZmeiLangSimpleLexer; }

import Base;

an_file:
    AN_FILE
    an_file_name
    python_code
    ;


an_file_name:
    STRING_DQ | STRING_DQ
    ;