
parser grammar ModelExtensionSortable;

options { tokenVocab=ZmeiLangSimpleLexer; }

import Base;

an_sortable:
    AN_SORTABLE
    BRACE_OPEN
    an_sortable_field_name
    BRACE_CLOSE
    ;

an_sortable_field_name : id_or_kw ;
