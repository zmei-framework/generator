
parser grammar CsExtraChannels;

options { tokenVocab=ZmeiLangSimpleLexer; }

import Base;

an_channels:
    AN_CHANNELS
    (BRACE_OPEN
    BRACE_CLOSE)?
    ;
