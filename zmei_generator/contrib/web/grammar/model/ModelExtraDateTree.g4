
parser grammar ModelExtensionDateTree;

options { tokenVocab=ZmeiLangSimpleLexer; }

import Base;

an_date_tree:
    AN_DATE_TREE
    (BRACE_OPEN
    an_date_tree_field
    BRACE_CLOSE)
    ;

an_date_tree_field : id_or_kw ;
