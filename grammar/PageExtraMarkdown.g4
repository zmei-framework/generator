
parser grammar PageExtraMarkdown;

options { tokenVocab=ZmeiLangSimpleLexer; }

import Base;

an_markdown:
    AN_MARKDOWN
    (DOT an_markdown_discriminator)?
    code_block
    ;

an_markdown_discriminator: id_or_kw;
