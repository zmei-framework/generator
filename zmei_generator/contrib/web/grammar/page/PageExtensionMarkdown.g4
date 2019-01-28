
parser grammar PageExtensionMarkdown;

options { tokenVocab=ZmeiLangSimpleLexer; }

import Base;

an_markdown:
    AN_MARKDOWN
    (DOT an_markdown_descriptor)?
    code_block
    ;

an_markdown_descriptor: id_or_kw;
