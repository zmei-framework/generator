parser grammar FieldsParser;

options { tokenVocab=ZmeiLangLexer; }


col_field_def: field_longtext
             | field_html_media
             | field_html
             | field_float
             | field_decimal
             | field_date
             | field_datetime
             | field_create_time
             | field_update_time
             | field_text
             | field_int
             | field_slug
             | field_bool
             | field_relation

             | field_image_file
             | field_image
             | field_filer_image
             | field_filer_file
             | field_file
             | field_simple_file
             | field_folder
             | field_image_folder
             ;



field_longtext: COL_FIELD_TYPE_LONGTEXT;
field_html: COL_FIELD_TYPE_HTML;
field_html_media: COL_FIELD_TYPE_HTML_MEDIA;
field_float: COL_FIELD_TYPE_FLOAT;
field_decimal: COL_FIELD_TYPE_DECIMAL;
field_date: COL_FIELD_TYPE_DATE;
field_datetime: COL_FIELD_TYPE_DATETIME;
field_create_time: COL_FIELD_TYPE_CREATE_TIME;
field_update_time: COL_FIELD_TYPE_UPDATE_TIME;

field_image_file: COL_FIELD_TYPE_IMAGE_FILE;
field_filer_image: COL_FIELD_TYPE_FILER_IMAGE;
field_filer_file: COL_FIELD_TYPE_FILER_FILE;
field_file: COL_FIELD_TYPE_FILE;
field_simple_file: COL_FIELD_TYPE_SIMPLE_FILE;
field_folder: COL_FIELD_TYPE_FOLDER;
field_image_folder: COL_FIELD_TYPE_IMAGE_FOLDER;

// Text

field_text:
            COL_FIELD_TYPE_TEXT
            (FIELD_START
            field_text_size
            (FILED_COMA field_text_choices)?
            FIELD_END)?;

field_text_size : (FILED_DIGIT | FIELD_QUSETION_MARK);

field_text_choices:
            FILED_ARG_CHOICES
            field_text_choice (FILED_COMA field_text_choice)*;

field_text_choice: field_text_choice_key? field_text_choice_val;

field_text_choice_val : (FIELD_QUOTED | FILED_LITERAL) ;

field_text_choice_key : FILED_KEY_STR ;

// Int

field_int:
            COL_FIELD_TYPE_INT
            (FIELD_START field_int_choices FIELD_END)?
            ;

field_int_choices:
            FILED_ARG_CHOICES
            field_int_choice (FILED_COMA field_int_choice)*;

field_int_choice: field_int_choice_key? field_int_choice_val;

field_int_choice_val : (FIELD_QUOTED | FILED_LITERAL) ;

field_int_choice_key : FILED_KEY_NUM ;

// Slug

field_slug:
            COL_FIELD_TYPE_SLUG
            FIELD_START
            field_slug_ref_field
            FIELD_END;

field_slug_ref_field: field_slug_ref_field_id (FILED_COMA field_slug_ref_field_id)*;
field_slug_ref_field_id: FILED_LITERAL;

// Bool

field_bool:
            COL_FIELD_TYPE_BOOL
            (FIELD_START field_bool_default FIELD_END)?;

field_bool_default: FIELD_BOOL;

// Image

field_image:
            COL_FIELD_TYPE_IMAGE
            (FIELD_START field_image_sizes field_image_filters* FIELD_END)?;

field_image_sizes: field_image_size (FILED_COMA field_image_size)*;
field_image_size: FILED_ARG_ANY FIELD_SIZE;
field_image_filters: FILED_FILTER;

// Relation

field_relation:
            field_relation_type
            FIELD_START
            (field_relation_target_ref | field_relation_target_class)
            field_relation_related_name?
            FIELD_END;

field_relation_type : COL_FIELD_TYPE_ONE | COL_FIELD_TYPE_ONE2ONE | COL_FIELD_TYPE_MANY;

field_relation_target_ref: FILED_REF;
field_relation_target_class: FILED_CLASS;
field_relation_related_name: FILED_RELATED_NAME;
