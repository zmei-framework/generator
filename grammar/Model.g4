parser grammar Model;

options { tokenVocab=ZmeiLangSimpleLexer; }

import
    Base,
    ModelFields,
    ModelExtra
    ;

/**************************
 * Collections
 **************************/

col:
    col_header
    col_str_expr?
    col_field*
    model_annotation*
    ;


col_str_expr :
    EQUALS (STRING_DQ | STRING_SQ)
    (NL+|EOF)
    ;

col_header :
    REF_SIGN
    col_base_name?
    col_name
    col_verbose_name?
    LINE_SEPARATOR
    NL
    ;

col_verbose_name : COLON verbose_name_part (SLASH verbose_name_part)?;

verbose_name_part : (id_or_kw | STRING_DQ | STRING_SQ) ;

col_base_name : id_or_kw (RELATED | RELATED_EXTEND);
col_name : id_or_kw;

col_field:
    col_modifier*
    col_field_name
    (
        (COLON col_field_def) |
        col_field_expr
    )?
    col_field_vrebose_name?
    col_field_help_text?
    (NL+|EOF)
    ;

col_field_expr :
        col_field_expr_marker
        col_feild_expr_code
        ;

col_field_expr_marker : ASSIGN | ASSIGN_STATIC;

col_feild_expr_code : PYTHON_LINE_CODE ;

string_or_quoted : (id_or_kw+ | STRING_DQ | STRING_SQ) ;

col_field_help_text : QUESTION_MARK string_or_quoted;

col_field_vrebose_name : SLASH string_or_quoted;

col_field_name : id_or_kw ;


col_modifier: EQUALS
             | DOLLAR
             | AMP
             | EXCLAM
             | STAR
             | APPROX
             ;
