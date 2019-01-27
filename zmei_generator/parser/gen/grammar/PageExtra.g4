parser grammar PageExtra;

options { tokenVocab=ZmeiLangSimpleLexer; }

import
    PageExtraStream,
    PageExtraReact,
    PageExtraHtml,
    PageExtraMarkdown,
    PageExtraCrudDelete,
    PageExtraPost,
    PageExtraAuth,
    PageExtraCrudCreate,
    PageExtraCrudEdit,
    PageExtraCrud,
    PageExtraCrudList,
    PageExtraMenu,
    PageExtraCrudDetail,
    PageExtraPriorityMarker,
    PageExtraGet,
    PageExtraError
    ;

page_annotation:
     an_stream
    |an_react
    |an_html
    |an_markdown
    |an_crud_delete
    |an_post
    |an_auth
    |an_crud_create
    |an_crud_edit
    |an_crud
    |an_crud_list
    |an_menu
    |an_crud_detail
    |an_priority_marker
    |an_get
    |an_error
    |NL;

