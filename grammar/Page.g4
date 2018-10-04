parser grammar Page;

options { tokenVocab=ZmeiLangSimpleLexer; }

import Base;

/**************************
 * Pages
 **************************/

page:
    page_header
    NL*

//    (page_code_line|NL)*

    page_field*

    page_element?

    NL*
    ;

page_header : SQ_BRACE_OPEN
    page_base?
    page_name
    page_alias?
    (COLON page_url? (COLON page_template)?)?
    SQ_BRACE_CLOSE
    NL ;

page_base : id_or_kw RELATED;
page_alias : KW_AS page_alias_name;

page_alias_name : id_or_kw ;

page_element : xml_element ;

page_template : CLASSNAME | TEMPLATE_NAME | INLINE_CODE_BLOCK;

page_url : (id_or_kw|URL_SEGMENTS|SLASH);

//page_code_line: CODE_LINE page_code_line_source NL;
//page_code_line_source : PYTHON_LINE_CODE ;

page_name: id_or_kw;

page_field:
    page_field_name
    ASSIGN
    page_field_code
    (NL+|EOF)
    ;


page_field_name : id_or_kw ;

page_field_code : PYTHON_LINE_CODE ;
