parser grammar Base;

options { tokenVocab=ZmeiLangSimpleLexer; }

/**
 * Allow keywords to be used as ID
 */
id_or_kw: ID
   |BOOL
   |WRITE_MODE
   // {KEYWORDS}
   ;

classname: id_or_kw (DOT id_or_kw)*;
model_ref: HASH (id_or_kw DOT)? id_or_kw;

field_list_expr:
    DOT? STAR (COMA EXCLUDE field_list_expr_field)*
    | id_or_kw (COMA EXCLUDE? field_list_expr_field)*
    ;

field_list_expr_field : STAR? id_or_kw STAR? ;


write_mode_expr : SQ_BRACE_OPEN WRITE_MODE SQ_BRACE_CLOSE;

python_code:
     code_block
    |code_line
    ;

code_line:
    ASSIGN
    PYTHON_CODE
    NL;

code_block:
    CODE_BLOCK
    ;
