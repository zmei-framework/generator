lexer grammar ZmeiLangSimpleLexer;

AN_ADMIN: '@admin';
AN_SUIT: '@suit';
AN_CELERY: '@celery';
AN_STREAM: '@stream';
AN_CHANNELS: '@channels';
AN_DOCKER: '@docker';
AN_API: '@api';
AN_REST: '@rest';
AN_FILER: '@filer';
AN_GITLAB: '@gitlab';
AN_REACT: '@react';
AN_REACT_CLIENT: '@react_client';
AN_REACT_SERVER: '@react_server';
AN_THEME: '@theme';
AN_PRIORITY: '@@';
AN_FILE: '@file';
AN_GET: '@get';
AN_MENU: '@menu';
AN_CRUD: '@crud';
AN_CRUD_DETAIL: '@crud_detail';
AN_CRUD_LIST: '@crud_list';
AN_CRUD_DELETE: '@crud_delete';
AN_CRUD_EDIT: '@crud_edit';
AN_CRUD_CREATE: '@crud_create';
AN_POST: '@post';
AN_ERROR: '@error';
AN_AUTH: '@auth';
AN_MARKDOWN: '@markdown';
AN_HTML: '@html';
AN_TREE: '@tree';
AN_DATE_TREE: '@date_tree';
AN_MIXIN: '@mixin';
AN_M2M_CHANGED: '@m2m_changed';
AN_POST_DELETE: '@post_delete';
AN_PRE_DELETE: '@pre_delete';
AN_POST_SAVE: '@post_save';
AN_PRE_SAVE: '@pre_save';
AN_CLEAN: '@clean';
AN_ORDER: '@order';
AN_SORTABLE: '@sortable';
AN_LANGS: '@langs';
AN_FLUTTER: '@flutter';
KW_AUTH_TYPE_BASIC: 'basic';
KW_AUTH_TYPE_SESSION: 'session';
KW_AUTH_TYPE_TOKEN: 'token';
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
KW_THEME: 'theme';
KW_INSTALL: 'install';
KW_HEADER: 'header';
KW_SERVICES: 'services';
KW_SELENIUM_PYTEST: 'selenium_pytest';
KW_CHILD: 'child';
KW_FILTER_OUT: 'filter_out';
KW_FILTER_IN: 'filter_in';
KW_PAGE: 'page';
KW_LINK_SUFFIX: 'link_suffix';
KW_URL_PREFIX: 'url_prefix';
KW_CAN_EDIT: 'can_edit';
KW_OBJECT_EXPR: 'object_expr';
KW_BLOCK: 'block';
KW_ITEM_NAME: 'item_name';
KW_PK_PARAM: 'pk_param';
KW_LIST_FIELDS: 'list_fields';
KW_DELETE: 'delete';
KW_EDIT: 'edit';
KW_CREATE: 'create';
KW_DETAIL: 'detail';
KW_SKIP: 'skip';
KW_FROM: 'from';
KW_POLY_LIST: '+polymorphic_list';
KW_CSS: 'css';
KW_JS: 'js';
KW_INLINE_TYPE_TABULAR: 'tabular';
KW_INLINE_TYPE_STACKED: 'stacked';
KW_INLINE_TYPE_POLYMORPHIC: 'polymorphic';
KW_INLINE: 'inline';
KW_TYPE: 'type';
KW_USER_FIELD: 'user_field';
KW_ANNOTATE: 'annotate';
KW_ON_CREATE: 'on_create';
KW_QUERY: 'query';
KW_AUTH: 'auth';
KW_COUNT: 'count';
KW_I18N: 'i18n';
KW_EXTENSION: 'extension';
KW_TABS: 'tabs';
KW_LIST: 'list';
KW_READ_ONLY: 'read_only';
KW_LIST_EDITABLE: 'list_editable';
KW_LIST_FILTER: 'list_filter';
KW_LIST_SEARCH: 'list_search';
KW_FIELDS: 'fields';
KW_IMPORT: 'import';
KW_AS: 'as';

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

