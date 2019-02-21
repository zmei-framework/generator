
parser grammar ModelExtensionRest;

options { tokenVocab=ZmeiLangSimpleLexer; }

import Base;

an_rest:
    AN_REST
    (DOT an_rest_descriptor)?
    (BRACE_OPEN
    an_rest_config
    BRACE_CLOSE)?
    ;

an_rest_config:
    an_rest_main_part
    (
         an_rest_inline
        |NL
        |COMA
    )*
    ;

an_rest_main_part: (
         an_rest_fields
        |an_rest_i18n
        |an_rest_str
        |an_rest_auth
        |an_rest_query
        |an_rest_on_create
        |an_rest_filter_in
        |an_rest_filter_out
        |an_rest_read_only
        |an_rest_user_field
        |an_rest_annotate
        |NL
        |COMA
    )*;

an_rest_descriptor : id_or_kw;

an_rest_i18n: KW_I18N COLON BOOL NL*;
an_rest_str: COL_FIELD_TYPE_TEXT COLON BOOL NL*;

an_rest_query: KW_QUERY python_code NL*;

an_rest_on_create: KW_ON_CREATE COLON? python_code NL*;
an_rest_filter_in: KW_FILTER_IN COLON? python_code NL*;
an_rest_filter_out: KW_FILTER_OUT COLON? python_code NL*;

an_rest_read_only: KW_READ_ONLY COLON field_list_expr NL*;

an_rest_user_field: KW_USER_FIELD COLON id_or_kw NL*;
an_rest_fields: KW_FIELDS COLON field_list_expr an_rest_fields_write_mode? NL*;

an_rest_fields_write_mode : write_mode_expr;

an_rest_auth: KW_AUTH BRACE_OPEN an_rest_auth_type (COMA an_rest_auth_type)* BRACE_CLOSE;
an_rest_auth_type: an_rest_auth_type_name (COLON an_rest_auth_token_model | an_rest_auth_token_class)?;

an_rest_auth_type_name : (KW_AUTH_TYPE_BASIC|KW_AUTH_TYPE_SESSION|KW_AUTH_TYPE_TOKEN) ;
an_rest_auth_token_model: model_ref;
an_rest_auth_token_class: classname;


an_rest_annotate:
        KW_ANNOTATE COLON
        an_rest_annotate_count
        NL*;

an_rest_annotate_count: KW_COUNT an_rest_annotate_count_field (KW_AS an_rest_annotate_count_alias)?;
an_rest_annotate_count_field: id_or_kw;
an_rest_annotate_count_alias: id_or_kw;


an_rest_inline: KW_INLINE COLON (
                    an_rest_inline_decl
                   |COMA
                   |NL
                )+;
an_rest_inline_decl: an_rest_inline_name BRACE_OPEN an_rest_config BRACE_CLOSE;
an_rest_inline_name: id_or_kw;

