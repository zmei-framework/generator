
parser grammar PageExtraHtml;

options { tokenVocab=ZmeiLangSimpleLexer; }

import Base;

an_html:
    AN_HTML
    (DOT an_html_discriminator)?
    code_block
    ;

an_html_discriminator: id_or_kw;