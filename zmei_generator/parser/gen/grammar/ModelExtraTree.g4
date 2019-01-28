
parser grammar ModelExtensionTree;

options { tokenVocab=ZmeiLangSimpleLexer; }

import Base;

an_tree:
    AN_TREE
    (BRACE_OPEN
    an_tree_poly
    BRACE_CLOSE)?
    ;

an_tree_poly: KW_POLY_LIST;
