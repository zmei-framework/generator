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

page_base : ID RELATED;
page_alias : KW_AS page_alias_name;

page_alias_name : ID ;

page_element : xml_element ;

page_template : CLASSNAME | TEMPLATE_NAME | INLINE_CODE_BLOCK;

page_url : (ID|URL_SEGMENTS);

page_code: code_block;

page_name: ID;

page_field:
    page_field_name
    ASSIGN
    page_field_code
    (NL+|EOF)
    ;

page_field_name : ID ;

page_field_code : PYTHON_LINE_CODE ;


/**************************
 * Collections
 **************************/

col:
    col_header
    col_str_expr?
    col_field*
    annotation*
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

verbose_name_part : (ID | STRING_DQ | STRING_SQ) ;

col_base_name : ID (RELATED | RELATED_EXTEND);
col_name : ID;

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

string_or_quoted : (ID+ | STRING_DQ | STRING_SQ) ;

col_field_help_text : QUESTION_MARK string_or_quoted;

col_field_vrebose_name : SLASH string_or_quoted;

col_field_name : ID ;


col_modifier: EQUALS
             | DOLLAR
             | AMP
             | EXCLAM
             | STAR
             | APPROX
             ;

/**************************
 * Collections
 **************************/


annotation:
    ANNOTATION
    annotation_descr?
    annotation_code?
    NL*
    ;

annotation_descr : (DOT ID) ;

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