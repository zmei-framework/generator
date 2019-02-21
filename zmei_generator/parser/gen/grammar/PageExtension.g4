parser grammar PageExtension;

options { tokenVocab=ZmeiLangSimpleLexer; }

import
    PageExtensionStream,
    PageExtensionReact,
    PageExtensionHtml,
    PageExtensionMarkdown,
    PageExtensionCrudDelete,
    PageExtensionPost,
    PageExtensionAuth,
    PageExtensionCrudCreate,
    PageExtensionCrudEdit,
    PageExtensionCrud,
    PageExtensionCrudList,
    PageExtensionMenu,
    PageExtensionCrudDetail,
    PageExtensionPriorityMarker,
    PageExtensionGet,
    PageExtensionError,
    PageExtensionFlutter
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
    |an_flutter
    |NL;

