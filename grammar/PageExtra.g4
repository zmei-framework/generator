parser grammar PageExtra;

options { tokenVocab=ZmeiLangSimpleLexer; }

import
    PageExtraReact,
    PageExtraHtml
    ;

page_annotation:
     an_html
    |an_react
    |NL;
