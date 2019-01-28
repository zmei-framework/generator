
parser grammar PageExtensionHtml;

options { tokenVocab=ZmeiLangSimpleLexer; }

import Base;

an_html:
    AN_HTML
    (DOT an_html_descriptor)?
    code_block
    ;

an_html_descriptor: id_or_kw;