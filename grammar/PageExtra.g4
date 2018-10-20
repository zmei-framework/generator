parser grammar PageExtra;

options { tokenVocab=ZmeiLangSimpleLexer; }

import
    PageExtraReact,
    PageExtraMarkdown,
    PageExtraHtml
    ;

page_annotation:
     an_html
    |an_react
    |an_markdown
    |NL;
