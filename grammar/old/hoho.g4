grammar hoho;

@header {
package ee.negative.zmei.lang.intellij.parser;
}

/*
 * Parser Rules
 */
col_file: NEWLINE? pages* collections* NEWLINE* EOF;

collections : collection+;


/*
 * Pages
 */
pages: page+ ;
page: page_header NEWLINE page_field*;

page_header : '[' page_name ']' ;
page_name : ID ;

page_field: ID field_expr;

field_expr : PYTHON_EXPRESSION NEWLINE;


/*
 * Collection
 */
collection : col_header col_fields;

col_fields : col_field+ ;

col_header  : COLLECTION_HEADER_START collection_name NEWLINE COLLECTION_HEADER_SEPARATOR NEWLINE;

collection_name: ID;
col_field: col_field_name field_definition? NEWLINE;

field_definition : COLON field_type;

field_type : TYPE_NAME ;
col_field_name : ID ;


/*
 * Lexer Rules
 */


COLON : ':' ;

TYPE_NAME: 'text'
         | 'int'
         ;

COLLECTION_HEADER_START: '#' ;
COLLECTION_HEADER_SEPARATOR: '-' '-'+ ;


ID : [a-zA-Z_] [a-zA-Z_0-9]+ ;

fragment NUMBER     : [0-9]+ ;

NEWLINE             : ('\r'? '\n' | '\r')+ ;

PYTHON_EXPRESSION : COLON ~[\r\n]+;

WHITESPACE : ' ' -> channel(HIDDEN) ;

/** "catch all" rule for any char not matche in a token rule of your
*  grammar. Lexers in Intellij must return all tokens good and bad.
*  There must be a token to cover all characters, which makes sense, for
*  an IDE. The parser however should not see these bad tokens because
*  it just confuses the issue. Hence, the hidden channel.
*/
ERRCHAR
    :	.	-> channel(HIDDEN)
    ;