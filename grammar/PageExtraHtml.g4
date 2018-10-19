
parser grammar PageExtraHtml;

options { tokenVocab=ZmeiLangSimpleLexer; }

import Base;

an_html:
    AN_HTML
    code_block
    ;
