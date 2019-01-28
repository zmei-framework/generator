
parser grammar AppExtensionTheme;

options { tokenVocab=ZmeiLangSimpleLexer; }

import Base;

an_theme:
    AN_THEME
    BRACE_OPEN
    an_theme_name

    (COMA KW_INSTALL EQUALS an_theme_install)?
    BRACE_CLOSE
    ;


an_theme_install:
    BOOL
    ;

an_theme_name:
      id_or_kw
    | STRING_DQ
    | STRING_SQ
    ;
