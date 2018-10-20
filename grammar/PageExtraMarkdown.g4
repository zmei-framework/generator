
parser grammar PageExtraMarkdown;

options { tokenVocab=ZmeiLangSimpleLexer; }

import Base;

an_markdown:
    AN_MARKDOWN
    code_block
    ;
