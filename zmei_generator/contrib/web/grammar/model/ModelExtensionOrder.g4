
parser grammar ModelExtensionOrder;

options { tokenVocab=ZmeiLangSimpleLexer; }

import Base;

an_order:
    AN_ORDER
    BRACE_OPEN
    an_order_fields
    BRACE_CLOSE
    ;

an_order_fields : id_or_kw (COMA id_or_kw)* ;
