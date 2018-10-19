parser grammar Page;

options { tokenVocab=ZmeiLangSimpleLexer; }

import Base,
       PageExtra
       ;

/**************************
 * Pages
 **************************/

page:
    page_header
    NL*

    page_field*

    page_code?

    NL*
    page_annotation*
    NL*
    ;

page_code: python_code;

page_header : SQ_BRACE_OPEN
    page_base?
    page_name
    page_alias?
    (COLON page_url? (COLON page_template)?)?
    SQ_BRACE_CLOSE
    NL? ;

page_base : id_or_kw DASH GT;
page_alias : KW_AS page_alias_name;

page_alias_name : id_or_kw ;

page_template : template_name | python_code;

template_name : file_name_part (SLASH file_name_part)*;

file_name_part : (id_or_kw | DIGIT | DASH | UNDERSCORE | DOT)+ ;

page_url : url_segments;

url_part: (id_or_kw
           |DASH
           |DIGIT
           )+;

url_param: LT id_or_kw GT;

url_segment: (url_part|url_param);

url_segments : SLASH | (SLASH url_segment)+ SLASH?;

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

page_field_code : PYTHON_CODE;
