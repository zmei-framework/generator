
parser grammar PageExtensionMenu;

options { tokenVocab=ZmeiLangSimpleLexer; }

import Base;

an_menu:
    AN_MENU
    DOT an_menu_descriptor
    BRACE_OPEN
    NL*
    an_menu_item+
    NL*
    BRACE_CLOSE
    ;

an_menu_descriptor: id_or_kw;

an_menu_item:
    COMA?
    NL*
    an_menu_item_args?

    an_menu_label
    (
        an_menu_item_code
       |an_menu_target
    )
    NL*
    ;

an_menu_target : COLON
        (
             an_menu_item_page
            |an_menu_item_url
        ) ;

an_menu_item_code:
    code_line
    ;

an_menu_item_args:
    SQ_BRACE_OPEN
    an_menu_item_arg (COMA an_menu_item_arg)*
    SQ_BRACE_CLOSE
    ;

an_menu_item_arg:
    an_menu_item_arg_key
    EQUALS
    an_menu_item_arg_val
    ;

an_menu_item_arg_key:
    id_or_kw
    ;

an_menu_item_arg_val:
     STRING_DQ
    |STRING_SQ
    |id_or_kw
    ;

an_menu_item_url:
     STRING_DQ
    |STRING_SQ
    ;

an_menu_item_page:
    KW_PAGE
    BRACE_OPEN
    an_menu_item_page_ref
    BRACE_CLOSE
    ;

an_menu_item_page_ref : (id_or_kw DOT)? id_or_kw;

an_menu_label:
     STRING_DQ
    |STRING_SQ
    |id_or_kw
    ;