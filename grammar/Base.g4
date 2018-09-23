parser grammar Base;

options { tokenVocab=ZmeiLangSimpleLexer; }

/**
 * Allow keywords to be used as ID
 */
id_or_kw: ID
   |BOOL
   |KW_CSS
   |KW_JS
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

field_list_expr:
    DOT? STAR (COMA EXCLUDE field_list_expr_field)*
    | id_or_kw (COMA EXCLUDE? field_list_expr_field)*
    ;

field_list_expr_field : STAR? id_or_kw STAR? ;


code_block:
    CODE_BLOCK_START
    (CODE_BLOCK_LINE)*
    CODE_BLOCK_END
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

