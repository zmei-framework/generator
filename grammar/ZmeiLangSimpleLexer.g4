lexer grammar ZmeiLangSimpleLexer;

// Annotation types
AN_MIXIN: '@mixin';
AN_M2M_CHANGED: '@m2m_changed';
AN_POST_DELETE: '@post_delete';
AN_PRE_DELETE: '@pre_delete';
AN_POST_SAVE: '@post_save';
AN_PRE_SAVE: '@pre_save';
AN_CLEAN: '@clean';
AN_API: '@api';
AN_REST: '@rest';
AN_ORDER: '@order';
AN_SORTABLE: '@sortable';
AN_LANGS: '@langs';
AN_FILER: '@filer';
AN_ADMIN: '@admin';
AN_SUIT: '@suit';

WRITE_MODE: 'r' | 'rw' | 'w';
BOOL: 'true' | 'false';

KW_EDITABLE: 'change_link';
KW_CSS: 'css';
KW_JS: 'js';
KW_INLINE_TYPE: 'tabular' | 'stacked' | 'polymorphic';
KW_AUTH_TYPE: 'basic' | 'session' | 'token';
KW_INLINE: 'inline';
KW_TYPE: 'type';
KW_USER_FIELD: 'user_field';
KW_ANNOTATE: 'annotate';
KW_ON_CREATE: 'on_create';
KW_QUERY: 'query';
KW_AUTH: 'auth';
KW_COUNT: 'count';
KW_I18N: 'i18n';
KW_EXTRA: 'extra';
KW_TABS: 'tabs';
KW_LIST: 'list';
KW_READ_ONLY: 'read_only';
KW_LIST_EDITABLE: 'list_editable';
KW_LIST_FILTER: 'list_filter';
KW_LIST_SEARCH: 'list_search';
KW_FIELDS: 'fields';


KW_IMPORT: 'import';
KW_AS: 'as';

COL_FIELD_TYPE_LONGTEXT: 'text';
COL_FIELD_TYPE_HTML: 'html';
COL_FIELD_TYPE_HTML_MEDIA: 'html_media';
COL_FIELD_TYPE_FLOAT: 'float';
COL_FIELD_TYPE_DECIMAL: 'decimal';
COL_FIELD_TYPE_DATE: 'date';
COL_FIELD_TYPE_DATETIME: 'datetime';
COL_FIELD_TYPE_CREATE_TIME: 'create_time';
COL_FIELD_TYPE_UPDATE_TIME: 'update_time';

COL_FIELD_TYPE_IMAGE: 'image';
COL_FIELD_TYPE_FILE: 'file';


COL_FIELD_TYPE_FILER_IMAGE: 'filer_image';
COL_FIELD_TYPE_FILER_FILE: 'filer_file';
COL_FIELD_TYPE_FILER_FOLDER: 'filer_folder';
COL_FIELD_TYPE_FILER_IMAGE_FOLDER: 'filer_image_folder';

COL_FIELD_TYPE_TEXT: 'str';
COL_FIELD_TYPE_INT: 'int';
COL_FIELD_TYPE_SLUG: 'slug';
COL_FIELD_TYPE_BOOL: 'bool';

COL_FIELD_TYPE_ONE: 'one';
COL_FIELD_TYPE_ONE2ONE: 'one2one';
COL_FIELD_TYPE_MANY: 'many';

COL_FIELD_CHOICES: 'choices';


fragment ERR: .;

NL : ('\r'? '\n' | '\r');


ID : [a-zA-Z_] [a-zA-Z_0-9]*;

DIGIT: [1-9][0-9]*;

CLASSNAME: ID ('.' ID)+;

SIZE2D: DIGIT 'x' DIGIT;

FILTER: '|' ID;


COLON: ':';
EXCLUDE: '^';
BRACE_OPEN: '(';
BRACE_CLOSE: ')';
SQ_BRACE_OPEN: '[';
SQ_BRACE_CLOSE: ']';
QUESTION_MARK: '?';
COMA: ',';
DOT: '.';

STRING_DQ: '"' (~[\r\n"] | '\\\\' | '\\"')* '"';
STRING_SQ: '\'' (~[\r\n'] | '\\\\' | '\\\'')* '\'';

//FIELD: ID WS* COLON;
FIELD_VNAME: '=>';
RELATED: '->';
RELATED_EXTEND: '~>';

REF_SIGN: '#';
ANNOTATION: '@' ID;
LINE_SEPARATOR: NL '-'+;

fragment URL_PART: [a-zA-Z\-0-9]+;
fragment URL_PARAM: '<' .*? '>';
fragment URL_SEGMENT: (URL_PART|URL_PARAM)+;

URL_SEGMENTS:  '/' URL_SEGMENT ('/' URL_SEGMENT)* '/'?;
TEMPLATE_NAME: [a-zA-Z\-_0-9/<>.]+ '.html';

COMMENT_LINE: '//' REST_OF_LINE -> channel(HIDDEN);

fragment REST_OF_LINE : .*? (NL|EOF) ;
COMMENT_BLOCK: '/*' .*? '*/' -> channel(HIDDEN);

SLASH: '/';
EQUALS: '=';
DOLLAR: '$';
AMP: '&';
EXCLAM: '!';
STAR: '*';
APPROX: '~';


WS : ' ' -> channel(HIDDEN);

COL_FIELD_CALCULATED: ('<<'|'<@') -> pushMode(PYTHON_EXPR);

ASSIGN: ':=' WS* -> pushMode(PYTHON_LINE);
ASSIGN_STATIC: '@=' WS* -> pushMode(PYTHON_LINE);

CODE_BLOCK_START: '{' -> pushMode(CODE_BLOCK);

XML_OPEN:   '<' -> pushMode(XML), pushMode(XML_INSIDE) ;

//mode CODE_LINE;
//CODE_LINE_CONTENT: ~'}'+;
//CODE_LINE_END: '}' -> popMode;

ERRCHAR: ERR;

mode CODE_BLOCK;
PYTHON_CODE: (~'}')+;
CODE_BLOCK_END: '}' -> popMode;
CODE_BLOCK_ERRCHAR:	ERR;

/** Python rest of line **/
mode PYTHON_LINE;
PYTHON_LINE_NL: '\n' -> type(NL), popMode;
PYTHON_LINE_CODE: (~'\n')+ -> type(PYTHON_CODE), popMode;
PYTHON_LINE_ERRCHAR:	ERR;


mode PYTHON_EXPR;
PYTHON_LINE_END: ';' -> popMode;
PYTHON_EXPR_CODE: (~[;\n])+ -> type(PYTHON_CODE);
PYTHON_EXPR_ERRCHAR:	ERR;


/*********************
 * Xml
 *********************/

mode XML;

XML_SEA_WS      :   (' '|'\t')+ -> type(WS), channel(HIDDEN);
XML_SEA_NL      :   ('\r'? '\n' | '\r')+ -> type(NL), channel(HIDDEN);

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


