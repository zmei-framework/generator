lexer grammar ZmeiLangLexer;

//import unicode;

tokens {ANNOTATION, ANNOT_BLOCK, NL}
fragment ID : [a-zA-Z_] [a-zA-Z_0-9]*;
fragment ERR: .;
//fragment UWORD: Unicode_Letter+;
//fragment USENTENCE: Unicode_Letter+;

COMMENT_LINE: '//' .*? (NL|EOF) -> channel(HIDDEN);
COMMENT_BLOCK: '/*' .*? '*/' -> channel(HIDDEN);

NL : ('\r'? '\n' | '\r') -> channel(HIDDEN);
WS : ' ' -> channel(HIDDEN);

PAGE_IMPORTS: .*? '%%' -> mode(GENERAL);
//DOCUMENT_START: NL -> channel(HIDDEN), mode(GENERAL);

ANNOTATION: '@' ID -> pushMode(ANNOT);

PAGE_HDR_START : NL* '[' -> mode(PAGE_HDR);
COL_HDR_START : NL* '#' -> mode(COL_HDR);

ERRCHAR:	ERR;

mode GENERAL;
GENERAL_COMMENT_LINE: COMMENT_LINE -> type(COMMENT_LINE), channel(HIDDEN);
GENERAL_COMMENT_BLOCK: COMMENT_BLOCK -> type(COMMENT_BLOCK), channel(HIDDEN);

GENERAL_NL : NL -> type(NL), channel(HIDDEN);
GENERAL_WS : WS -> type(WS), channel(HIDDEN);

MODEL_IMPORTS: '%%' .*? '%%';

GENERAL_ANNOTATION: '@' ID -> type(ANNOTATION), pushMode(ANNOT);

GENERAL_PAGE_HDR_START : '['
    -> type(PAGE_HDR_START), mode(PAGE_HDR);
GENERAL_COL_HDR_START : '#'
    -> type(COL_HDR_START), mode(COL_HDR);


GENERAL_ERRCHAR:	ERR;


/*********************
 * Collections
 *********************/

/** Collection header **/
mode COL_HDR;

COL_HDR_WS: WS+ -> type(WS), channel(HIDDEN);

fragment COL_HDR_ANY_TEXT: ~[\n/]+;

COL_BASE: ID WS* '->';
COL_NAME: ID;
COL_VNAME: ':' COL_HDR_ANY_TEXT ('/' COL_HDR_ANY_TEXT)?;

COL_HDR_SEPARATOR: NL '-' '-'* (NL|EOF) -> mode(COL);
COL_HDR_ERRCHAR:	ERR;

/** Collection body **/
mode COL;
COL_COMMENT_LINE: COMMENT_LINE -> type(COMMENT_LINE), channel(HIDDEN);
COL_COMMENT_BLOCK: COMMENT_BLOCK -> type(COMMENT_BLOCK), channel(HIDDEN);

COL_WS: WS+ -> type(WS), channel(HIDDEN);
COL_NL: NL+ -> type(NL);

COL_STR_EXPR: '=' '"' .*? '"';

COL_MODIFIER__STR: '=';
COL_MODIFIER__LOC: '$';
COL_MODIFIER__UNQ: '&';
COL_MODIFIER__IDX: '!';
COL_MODIFIER__REQ: '*';
COL_MODIFIER__NNL: '~';

COL_FIELD: ID;

COL_ANNOT: '@' ID -> type(ANNOTATION), pushMode(ANNOT);

COL_FIELD_HELP: '?' ~('/'|'\n')+;
COL_FIELD_VNAME: '/' ~('?'|'\n')+;

COL_FIELD_SEPARATOR: ':' -> pushMode(FIELD_DECL);

COL__PAGE_HDR_START : '[' -> type(PAGE_HDR_START), mode(PAGE_HDR);
COL__COL_HDR_START : '#' -> type(COL_HDR_START), mode(COL_HDR);

COL_ERRCHAR:	ERR;

/** Collection field **/

mode FIELD_DECL;
FIELD_DECL_COMMENT_LINE: COMMENT_LINE -> type(COMMENT_LINE), channel(HIDDEN);
FIELD_DECL_COMMENT_BLOCK: COMMENT_BLOCK -> type(COMMENT_BLOCK), channel(HIDDEN);

COL_FIELD_DECL_WS: WS+ -> type(WS), channel(HIDDEN);

COL_FIELD_CALCULATED: ('<<'|'<@') -> pushMode(PYTHON_EXPR);

COL_FIELD_TYPE: 'text'
              | 'longtext'
              | 'html'
              | 'slug'
              | 'int'
              | 'float'
              | 'decimal'
              | 'bool'
              | 'date'
              | 'datetime'
              | 'create_time'
              | 'update_time'
              | 'file'
              | 'folder'
              | 'image'
              | 'one'
              | 'many'
              ;

COL_FIELD_ARGS: '(' .*? ')';

FIELD_DECL__COL_FIELD_HELP: COL_FIELD_HELP -> type(COL_FIELD_HELP);
FIELD_DECL__COL_FIELD_VNAME: COL_FIELD_VNAME -> type(COL_FIELD_VNAME);

FIELD_DECL_EOF: EOF -> type(EOF), popMode;
FIELD_DECL_NL: NL -> type(NL), popMode;
FIELD_DECL_ERRCHAR:	ERR;


/*********************
 * Pages
 *********************/

/** Page header **/
mode PAGE_HDR;

PAGE_BASE: ID '->';
PAGE_NAME: ID -> mode(PAGE_HDR_PARTS);
PAGE_HDR_WS : ' ' -> channel(HIDDEN);
PAGE_HDR_ERRCHAR:	ERR;

mode PAGE_HDR_PARTS;
PAGE_HDR_SEPARATOR: ':';
PAGE_HDR_PART: ~[:\]]+;
PAGE_HDR_END: ']' (NL+|EOF) -> mode(PAGE);
PAGE_HDR_PARTS_WS : ' ' -> channel(HIDDEN);
PAGE_HDR_PARTS_ERRCHAR:	.	-> channel(HIDDEN);


/** Page body **/
mode PAGE;
PAGE_COMMENT_LINE: COMMENT_LINE -> type(COMMENT_LINE), channel(HIDDEN);
PAGE_COMMENT_BLOCK: COMMENT_BLOCK -> type(COMMENT_BLOCK), channel(HIDDEN);

PAGE_WS: WS+ -> type(WS), channel(HIDDEN);
PAGE_NL: NL+ -> type(NL);

PAGE_FIELD: ID;
PAGE_FIELD_SEPARATOR: ':' WS* -> pushMode(PYTHON_LINE);

XML_OPEN:   '<' -> pushMode(XML), pushMode(XML_INSIDE) ;

PAGE__PAGE_HDR_START : '[' -> type(PAGE_HDR_START), mode(PAGE_HDR);
PAGE__COL_HDR_START : '#' -> type(COL_HDR_START), mode(COL_HDR);

PAGE_MODEL_IMPORTS: '%%' .*? '%%' -> type(MODEL_IMPORTS);
PAGE_CODE_BLOCK_START: '{' NL* -> pushMode(PAGE_CODE_BLOCK);

PAGE_ANNOT: '@' ID -> type(ANNOTATION), pushMode(ANNOT);
PAGE_ERRCHAR:	ERR;


mode PAGE_CODE_BLOCK;
PAGE_CODE_BLOCK_END: '}' -> popMode;
PAGE_CODE_BLOCK_CODE: (~'}')+;
PAGE_CODE_BLOCK_ERRCHAR:	ERR;

/*********************
 * Reusable modes
 *********************/

/** Python rest of line **/
mode PYTHON_LINE;
PYTHON_LINE_CODE: (~'\n')+ -> popMode;
PYTHON_LINE_ERRCHAR:	ERR;


mode PYTHON_EXPR;
PYTHON_LINE_END: ';' -> popMode;
PYTHON_EXPR_CODE: (~[;\n])+ -> type(PYTHON_LINE_CODE);
PYTHON_EXPR_ERRCHAR:	ERR;


/** Annotation block **/
mode ANNOT;
ANNOT_COMMENT_LINE: COMMENT_LINE -> type(COMMENT_LINE), channel(HIDDEN);
ANNOT_COMMENT_BLOCK: COMMENT_BLOCK -> type(COMMENT_BLOCK), channel(HIDDEN);

ANNOT_DESCR: '.' ID;
ANNOT_WS: WS -> type(WS), channel(HIDDEN);
ANNOT_BLOCK_START: '{' -> pushMode(ANB_CURLY);

ANNOT_EOF: EOF -> type(EOF), popMode;
ANNOT_NL: NL -> type(NL), popMode;

ANNOT_ERRCHAR:	ERR;

mode ANB_CURLY;
ANNOT_BLOCK_END: '}' -> popMode;
ANNOT_BLOCK: (~'}')+;


/*********************
 * Xml
 *********************/

mode XML;

XML_SEA_WS      :   (' '|'\t')+ -> type(WS), channel(HIDDEN);
XML_SEA_NL      :   ('\r'? '\n' | '\r')+ -> type(NL), channel(HIDDEN);

XML_PAGE_HDR_START : '['
    -> type(PAGE_HDR_START), mode(PAGE_HDR);
XML_COL_HDR_START : '#'
    -> type(COL_HDR_START), mode(COL_HDR);
XML_MODEL_IMPORTS : '%%' .*? '%%' -> type(MODEL_IMPORTS), mode(GENERAL);


XML_EntityRef   :   '&' XML_Name ';' ;
XML_CharRef     :   '&#' XML_DIGIT+ ';'
            |   '&#x' XML_HEXDIGIT+ ';'
            ;

XML_TAG_OPEN    :   '<'                 -> type(XML_OPEN), pushMode(XML_INSIDE) ;
XML_TEXT        :   ~[<&[#%]+ ;        // match any 16 bit char other than < and &

XML_ERRCHAR     :	ERR;

mode XML_INSIDE;


XML_CLOSE       :   WS* '>'                     -> popMode ;
XML_SPECIAL_CLOSE:  '?>'                    -> popMode ; // close <?xml...?>
XML_SLASH_CLOSE :   '/>'                    -> popMode ;
XML_SLASH       :   '/' ;
XML_EQUALS      :   '=' ;
XML_REACT_ATTR      :   '{' ~[<}]*? '}';
XML_STRING      :   '"' ~[<"]*? '"'
                |   '\'' ~[<']*? '\''
                ;

XML_CmpName     :   XML_CmpNameStartChar XML_NameChar* ;
XML_Name        :   XML_NameStartChar XML_NameChar* ;
XML_XmlSpaceWS  :   [ \t]    -> type(WS), channel(HIDDEN) ;
XML_XmlSpaceNL  :   [\r\n]   -> type(NL), channel(HIDDEN) ;

XML_INSIDE_ERRCHAR     :	ERR;

fragment
XML_HEXDIGIT    :   [a-fA-F0-9] ;

fragment
XML_DIGIT       :   [0-9] ;

fragment
XML_NameChar    :   XML_NameStartChar
                |   '-' | '_' | '.' | XML_DIGIT
                |   '\u00B7'
                |   '\u0300'..'\u036F'
                |   '\u203F'..'\u2040'
                ;

fragment
XML_CmpNameStartChar
                :   [A-Z]
                |   '\u2070'..'\u218F'
                |   '\u2C00'..'\u2FEF'
                |   '\u3001'..'\uD7FF'
                |   '\uF900'..'\uFDCF'
                |   '\uFDF0'..'\uFFFD'
                ;

fragment
XML_NameStartChar
                :   [:a-zA-Z]
                |   '\u2070'..'\u218F'
                |   '\u2C00'..'\u2FEF'
                |   '\u3001'..'\uD7FF'
                |   '\uF900'..'\uFDCF'
                |   '\uFDF0'..'\uFFFD'
                ;





