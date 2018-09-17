parser grammar ZmeiLangParser;

options { tokenVocab=ZmeiLangLexer; }

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

page_imports : PAGE_IMPORTS;
model_imports : NL* MODEL_IMPORTS NL*;


/**************************
 * Pages
 **************************/

page:
    PAGE_HDR_START
    page_base?
    page_name
    page_alias?
    (PAGE_HDR_SEPARATOR page_url (PAGE_HDR_SEPARATOR page_template)?)?
    PAGE_HDR_END

    page_field*

    annotation*

    page_code?

    annotation*

    page_element?

    NL*
    ;

page_base : PAGE_BASE ;
page_alias : PAGE_ALIAS_MARKER page_alias_name;

page_alias_name : PAGE_ALIAS_ID ;

page_element : xml_element ;

page_template : PAGE_HDR_PART;

page_url : PAGE_HDR_PART;

page_code :
    PAGE_CODE_BLOCK_START
    page_code_source
    PAGE_CODE_BLOCK_END
    ;

page_code_source : PAGE_CODE_BLOCK_CODE;

page_name: PAGE_NAME ;

page_field:
    page_field_name
    PAGE_FIELD_SEPARATOR
    page_field_code
    (NL+|EOF)
    ;

page_field_name : PAGE_FIELD ;

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
    COL_STR_EXPR
    (NL+|EOF)
    ;

col_header :
    COL_HDR_START
    col_base_name?
    col_name
    col_verbose_name?
    COL_HDR_SEPARATOR
    ;

col_verbose_name : COL_VNAME ;

col_base_name : COL_BASE;
col_name : COL_NAME;

col_field:
    col_modifier*
    col_field_name
    (COL_FIELD_SEPARATOR (col_field_def|col_field_expr))?
    col_field_vrebose_name?
    col_field_help_text?
    (NL+|EOF)
    ;

col_field_help_text : COL_FIELD_HELP ;

col_field_vrebose_name : COL_FIELD_VNAME ;

col_field_name : COL_FIELD ;

col_field_expr:
    col_field_expr_marker
    col_feild_expr_code
    PYTHON_LINE_END
    ;

col_feild_expr_code : PYTHON_LINE_CODE ;

col_field_expr_marker : COL_FIELD_CALCULATED ;

col_modifier: COL_MODIFIER__STR
             | COL_MODIFIER__LOC
             | COL_MODIFIER__UNQ
             | COL_MODIFIER__IDX
             | COL_MODIFIER__REQ
             | COL_MODIFIER__NNL
             ;

/**************************
 * Collections
 **************************/


annotation:
    ANNOTATION
    ANNOT_DESCR?
    annotation_block?
    NL*
    ;

annotation_block :
    ANNOT_BLOCK_START
    annotation_code
    ANNOT_BLOCK_END
    ;

annotation_code:
    ANNOT_BLOCK
    ;


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