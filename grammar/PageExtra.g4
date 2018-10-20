parser grammar PageExtra;

options { tokenVocab=ZmeiLangSimpleLexer; }

import
    PageExtraReact,
    PageExtraMarkdown,
    PageExtraAuth,
    PageExtraError,
    PageExtraPost,
    PageExtraHtml
    ;

page_annotation:
     an_html
    |an_react
    |an_post
    |an_error
    |an_auth
    |an_markdown
    |NL;
