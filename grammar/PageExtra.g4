parser grammar PageExtra;

options { tokenVocab=ZmeiLangSimpleLexer; }

import
    PageExtraReact,
    PageExtraMarkdown,
    PageExtraAuth,
    PageExtraHtml
    ;

page_annotation:
     an_html
    |an_react
    |an_auth
    |an_markdown
    |NL;
