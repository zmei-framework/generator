lexer grammar ZmeiLangSimpleLexer;

// {TOKENS}
// {KEYWORDS}

WRITE_MODE: 'r' | 'rw' | 'w';
BOOL: 'true' | 'false';


fragment ERR: .;

NL : ('\r'? '\n' | '\r');


ID : [a-zA-Z_] [a-zA-Z_0-9]*;

DIGIT: [1-9][0-9]*;

SIZE2D: DIGIT 'x' DIGIT;


LT: '<';
GT: '>';
COLON: ':';
EXCLUDE: '^';
BRACE_OPEN: '(';
BRACE_CLOSE: ')';
SQ_BRACE_OPEN: '[';
SQ_BRACE_CLOSE: ']';
QUESTION_MARK: '?';
UNDERSCORE: '_';
DASH: '-';
COMA: ',';
DOT: '.';
HASH: '#';
SLASH: '/';
EQUALS: '=';
DOLLAR: '$';
AMP: '&';
EXCLAM: '!';
STAR: '*';
APPROX: '~';
PIPE: '|';


STRING_DQ: '"' (~[\r\n"] | '\\\\' | '\\"')* '"';
STRING_SQ: '\'' (~[\r\n'] | '\\\\' | '\\\'')* '\'';

COMMENT_LINE: '//' REST_OF_LINE -> channel(HIDDEN);

fragment REST_OF_LINE : .*? (NL|EOF) ;
COMMENT_BLOCK: '/*' .*? '*/' -> channel(HIDDEN);


UNICODE         :   '\u2070'..'\u218F'
                |   '\u2C00'..'\u2FEF'
                |   '\u3001'..'\uD7FF'
                |   '\uF900'..'\uFDCF'
                |   '\uFDF0'..'\uFFFD'
                |   '\u00B7'
                |   '\u0300'..'\u036F'
                |   '\u203F'..'\u2040'
                ;


WS : ' ' -> channel(HIDDEN);

COL_FIELD_CALCULATED: ('<<'|'<@') -> pushMode(PYTHON_EXPR);

ASSIGN: ':=' WS* -> pushMode(PYTHON_LINE);
ASSIGN_STATIC: '@=' WS* -> pushMode(PYTHON_LINE);

CODE_BLOCK: '{' ( CODE_BLOCK | ~[{}] )* '}' ;

ERRCHAR: ERR;
//
//mode CODE_BLOCK;
//PYTHON_CODE: ~[{}]+;
//CODE_BLOCK_CODE_BLOCK_START: '{' -> more, pushMode(CODE_BLOCK);
//CODE_BLOCK_END: '}' -> popMode;
//CODE_BLOCK_ERRCHAR:	ERR;

/** Python rest of line **/
mode PYTHON_LINE;
PYTHON_LINE_NL: '\n' -> type(NL), popMode;
PYTHON_CODE: (~'\n')+ -> popMode;
PYTHON_LINE_ERRCHAR:	ERR;


mode PYTHON_EXPR;
PYTHON_LINE_END: ';' -> popMode;
PYTHON_EXPR_CODE: (~[;\n])+ -> type(PYTHON_CODE);
PYTHON_EXPR_ERRCHAR:	ERR;

