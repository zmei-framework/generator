
parser grammar PageExtensionStream;

options { tokenVocab=ZmeiLangSimpleLexer; }

import Base;

an_stream:
    AN_STREAM
    (BRACE_OPEN
    (an_stream_model|NL)+
    BRACE_CLOSE)
    ;
    
// model

an_stream_model:
    an_stream_target_model
    an_stream_target_filter?
    an_stream_field_list?
    COMA?
    NL?
    ;

an_stream_target_model:
    model_ref | classname;

// filter

an_stream_target_filter:
    code_block;

an_stream_field_list:
    EQUALS GT
    (STAR | (
        an_stream_field_name
        (COMA an_stream_field_name)*
    ))
    ;

an_stream_field_name:
    id_or_kw
    ;
