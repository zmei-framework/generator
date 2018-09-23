parser grammar ZmeiLangParser;

options { tokenVocab=ZmeiLangSimpleLexer; }

import FieldsParser;

col_file:
    page_imports?
    NL*
    annotation*
    page*
    model_imports?
    col*
    NL*
    EOF
    ;

page_imports : KW_IMPORT import_source;
model_imports : KW_IMPORT import_source;

import_source : code_block;


code_block:
    CODE_BLOCK_START
    (CODE_BLOCK_LINE)*
    CODE_BLOCK_END
    ;

//code_line:
//    CODE_LINE_START
//    CODE_LINE_CONTENT
//    CODE_LINE_END
//    ;


/**************************
 * Pages
 **************************/

page:
    SQ_BRACE_OPEN
    page_base?
    page_name
    page_alias?
    (COLON page_url? (COLON page_template)?)?
    SQ_BRACE_CLOSE
    NL

    page_field*

    annotation*

    page_code?

    annotation*

    page_element?

    NL*
    ;

page_base : id_or_kw RELATED;
page_alias : KW_AS page_alias_name;

page_alias_name : id_or_kw ;

page_element : xml_element ;

page_template : CLASSNAME | TEMPLATE_NAME | INLINE_CODE_BLOCK;

page_url : (id_or_kw|URL_SEGMENTS);

page_code: code_block;

page_name: id_or_kw;

page_field:
    page_field_name
    ASSIGN
    page_field_code
    (NL+|EOF)
    ;

page_field_name : id_or_kw ;

page_field_code : PYTHON_LINE_CODE ;


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

/**************************
 * Model Annotations
 **************************/

model_annotation:
    an_admin;


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
        |an_admin_inlines
        |NL
        |COMA
    )*
    an_admin_tabs?
    NL*
    BRACE_CLOSE)?
    NL*
    ;

an_admin_inlines: KW_INLINE COLON an_admin_inline (COMA an_admin_inline)*;
an_admin_inline:
        inline_name
        (BRACE_OPEN
        (
             inline_type
            |inline_extra
            |inline_fields
            |NL
            |COMA
        )*
        BRACE_CLOSE)?;

inline_name: id_or_kw;
inline_type: KW_TYPE COLON KW_INLINE_TYPE;
inline_extra: KW_EXTRA COLON DIGIT;
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

field_list_expr:
    DOT? STAR (COMA EXCLUDE field_list_expr_field)*
    | id_or_kw (COMA EXCLUDE? field_list_expr_field)*
    ;

field_list_expr_field : STAR? id_or_kw STAR? ;

annotation:
    ANNOTATION
    annotation_descr?
    annotation_code?
    NL*
    ;


annotation_descr : (DOT id_or_kw) ;

//annotation_block :
//    ANNOT_BLOCK_START
//    annotation_code
//    ANNOT_BLOCK_END
//    ;

annotation_code: code_block;


/**************************
 * ReactComponents
 **************************/



xml_content     :   xml_chardata?
                ((xml_element | xml_reference) xml_chardata?)* ;

xml_element     :   XML_OPEN xml_name xml_attribute* XML_CLOSE xml_content XML_OPEN XML_SLASH xml_name_end XML_CLOSE
                |   XML_OPEN xml_name xml_attribute* XML_SLASH_CLOSE;

xml_name    :   xml_component_name | xml_tag_name
            ;

xml_name_end    :   xml_component_name | xml_tag_name
            ;

xml_tag_name : XML_Name ;

xml_component_name : XML_CmpName ;


xml_reference   :   XML_EntityRef | XML_CharRef ;

xml_attribute   :   XML_Name XML_EQUALS (XML_STRING|XML_REACT_ATTR) ; // Our STRING is AttValue in spec

/** ``All text that is not markup constitutes the character data of
 *  the document.''
 */
xml_chardata    :   XML_TEXT | WS | NL ;

xml_misc        :   WS | NL ;


/**
 * Allow keywords to be used as ID
 */
id_or_kw: ID
   |BOOL
   |KW_INLINE_TYPE
   |KW_INLINE
   |KW_TYPE
   |KW_EXTRA
   |KW_TABS
   |KW_LIST
   |KW_READ_ONLY
   |KW_LIST_EDITABLE
   |KW_LIST_FILTER
   |KW_LIST_SEARCH
   |KW_FIELDS
   |KW_IMPORT
   |KW_AS
   |COL_FIELD_TYPE_LONGTEXT
   |COL_FIELD_TYPE_HTML
   |COL_FIELD_TYPE_HTML_MEDIA
   |COL_FIELD_TYPE_FLOAT
   |COL_FIELD_TYPE_DECIMAL
   |COL_FIELD_TYPE_DATE
   |COL_FIELD_TYPE_DATETIME
   |COL_FIELD_TYPE_CREATE_TIME
   |COL_FIELD_TYPE_UPDATE_TIME
   |COL_FIELD_TYPE_IMAGE_FILE
   |COL_FIELD_TYPE_IMAGE
   |COL_FIELD_TYPE_FILER_IMAGE
   |COL_FIELD_TYPE_FILER_FILE
   |COL_FIELD_TYPE_FILE
   |COL_FIELD_TYPE_SIMPLE_FILE
   |COL_FIELD_TYPE_FOLDER
   |COL_FIELD_TYPE_IMAGE_FOLDER
   |COL_FIELD_TYPE_TEXT
   |COL_FIELD_TYPE_INT
   |COL_FIELD_TYPE_SLUG
   |COL_FIELD_TYPE_BOOL
   |COL_FIELD_TYPE_ONE
   |COL_FIELD_TYPE_ONE2ONE
   |COL_FIELD_TYPE_MANY
   |COL_FIELD_CHOICES
   ;