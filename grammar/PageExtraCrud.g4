
parser grammar PageExtraCrud;

options { tokenVocab=ZmeiLangSimpleLexer; }

import Base;

an_crud:
    AN_CRUD
    an_crud_params
    ;

an_crud_params:
    BRACE_OPEN
    NL*
    an_crud_target_model
    (
         an_crud_theme
        |an_crud_skip
        |an_crud_fields
        |an_crud_list_fields
        |NL
        |COMA
    )*
    NL*

    BRACE_CLOSE
    ;

// model

an_crud_target_model:
    (HASH id_or_kw) | classname;

// theme

an_crud_theme:
    KW_THEME COLON id_or_kw;

// skip

an_crud_skip:
    KW_SKIP COLON an_crud_skip_values;

an_crud_skip_values:
    an_crud_view_name (COMA an_crud_view_name)*;

an_crud_view_name:
     KW_DELETE
    |KW_LIST
    |KW_CREATE
    |KW_EDIT
    |KW_DETAIL
    ;


// fields

an_crud_fields:
    KW_FIELDS COLON an_crud_fields_expr;

an_crud_fields_expr: an_crud_field (COMA an_crud_field)*;
an_crud_field: an_crud_field_spec an_crud_field_filter?;
an_crud_field_spec: STAR | (EXCLUDE? id_or_kw);
an_crud_field_filter: code_block;

// list fields

an_crud_list_fields:
    KW_LIST_FIELDS COLON an_crud_list_fields_expr;

an_crud_list_fields_expr: an_crud_list_field (COMA an_crud_list_field)*;
an_crud_list_field: an_crud_list_field_spec;
an_crud_list_field_spec: STAR | (EXCLUDE? id_or_kw);
