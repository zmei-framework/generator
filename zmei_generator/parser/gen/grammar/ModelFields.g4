parser grammar ModelFields;

options { tokenVocab=ZmeiLangSimpleLexer; }

import Base;

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
             | field_image
             | field_file
             | field_filer_file
             | field_filer_folder
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

field_file: COL_FIELD_TYPE_FILE;
field_filer_file: COL_FIELD_TYPE_FILER_FILE;
field_filer_folder: COL_FIELD_TYPE_FILER_FOLDER;

// Text

field_text:
            COL_FIELD_TYPE_TEXT
            (BRACE_OPEN
            field_text_size
            (COMA field_text_choices)?
            BRACE_CLOSE)?;

field_text_size : (DIGIT | QUESTION_MARK);

field_text_choices:
            COL_FIELD_CHOICES EQUALS
            field_text_choice (COMA field_text_choice)*;

field_text_choice: field_text_choice_key? field_text_choice_val;

field_text_choice_val : (id_or_kw | STRING_DQ | STRING_SQ) ;

field_text_choice_key : id_or_kw COLON;

// Int

field_int:
            COL_FIELD_TYPE_INT
            (BRACE_OPEN field_int_choices BRACE_CLOSE)?
            ;

field_int_choices:
            COL_FIELD_CHOICES EQUALS
            field_int_choice (COMA field_int_choice)*;

field_int_choice: field_int_choice_key? field_int_choice_val;

field_int_choice_val : (id_or_kw | STRING_DQ | STRING_SQ) ;

field_int_choice_key : DIGIT COLON;

// Slug

field_slug:
            COL_FIELD_TYPE_SLUG
            BRACE_OPEN
            field_slug_ref_field
            BRACE_CLOSE;

field_slug_ref_field: field_slug_ref_field_id (COMA field_slug_ref_field_id)*;
field_slug_ref_field_id: id_or_kw;

// Bool
field_bool:
            COL_FIELD_TYPE_BOOL
            (BRACE_OPEN field_bool_default BRACE_CLOSE)?;

field_bool_default: BOOL;

// Image

field_image:
            filer_image_type
            (BRACE_OPEN field_image_sizes  BRACE_CLOSE)?;

filer_image_type : (COL_FIELD_TYPE_IMAGE|COL_FIELD_TYPE_FILER_IMAGE|COL_FIELD_TYPE_FILER_IMAGE_FOLDER) ;

field_image_sizes: field_image_size (COMA field_image_size)*;
field_image_size: field_image_size_name field_image_size_dimensions field_image_filters;

field_image_size_dimensions : SIZE2D;

field_image_size_name : id_or_kw EQUALS;

field_image_filters: field_image_filter*;
field_image_filter : PIPE id_or_kw;

// Relation

field_relation:
            field_relation_type
            BRACE_OPEN
            field_relation_cascade_marker?
            (field_relation_target_ref | field_relation_target_class)
            field_relation_related_name?
            BRACE_CLOSE;

field_relation_type : COL_FIELD_TYPE_ONE | COL_FIELD_TYPE_ONE2ONE | COL_FIELD_TYPE_MANY;

field_relation_cascade_marker: APPROX | EXCLAM;
field_relation_target_ref: model_ref;
field_relation_target_class: classname;
field_relation_related_name: DASH GT id_or_kw;
