
parser grammar ModelExtensionAdmin;

options { tokenVocab=ZmeiLangSimpleLexer; }

import Base;

an_admin:
    AN_ADMIN
    (BRACE_OPEN
    (
         an_admin_list
        |an_admin_read_only
        |an_admin_list_editable
        |an_admin_list_filter
        |an_admin_list_search
        |an_admin_fields
        |an_admin_tabs
        |an_admin_inlines
        |an_admin_css
        |an_admin_js
        |NL
        |COMA
    )*
    NL*
    BRACE_CLOSE)?
    NL*
    ;

an_admin_js: KW_JS COLON NL* an_admin_js_file_name (COMA NL* an_admin_js_file_name)*;
an_admin_css: KW_CSS COLON an_admin_css_file_name (COMA an_admin_css_file_name)*;
an_admin_css_file_name: STRING_DQ | STRING_SQ;
an_admin_js_file_name: STRING_DQ | STRING_SQ;

an_admin_inlines: KW_INLINE COLON an_admin_inline (COMA an_admin_inline)*;
an_admin_inline:
        inline_name
        (BRACE_OPEN
        (
             inline_type
            |inline_extension
            |inline_fields
            |NL
            |COMA
        )*
        BRACE_CLOSE)?;

inline_name: id_or_kw;
inline_type: KW_TYPE COLON inline_type_name;

inline_type_name : (KW_INLINE_TYPE_TABULAR | KW_INLINE_TYPE_STACKED | KW_INLINE_TYPE_POLYMORPHIC) ;
inline_extension: KW_EXTENSION COLON DIGIT;
inline_fields: KW_FIELDS COLON field_list_expr;

an_admin_tabs: KW_TABS COLON an_admin_tab (COMA an_admin_tab)*;

an_admin_tab: tab_name tab_verbose_name? BRACE_OPEN field_list_expr BRACE_CLOSE;

tab_name : id_or_kw;
tab_verbose_name : STRING_DQ | STRING_SQ;

an_admin_list: KW_LIST COLON field_list_expr NL*;
an_admin_read_only: KW_READ_ONLY COLON field_list_expr NL*;
an_admin_list_editable: KW_LIST_EDITABLE COLON field_list_expr NL*;
an_admin_list_filter: KW_LIST_FILTER COLON field_list_expr NL*;
an_admin_list_search: KW_LIST_SEARCH COLON field_list_expr NL*;
an_admin_fields: KW_FIELDS COLON field_list_expr NL*;
