
Annotation types
======================

There are four annotations that can be applied to a page and a @crud annotation, creating subpages for CRUD automatically.

@crud_create
--------------

Shows an empty form to create a new model instance. Upon form submission it verifies whether everything is ok and creates the instance::

    [my_page: /]
    @crud_create(#cat)

    #cat
    --------
    name
    age: int

@crud_edit
--------------

Shows an edit form for an existing model instance. Upon form submission it verifies if everything is ok and updates the instance. The current model id is taken from url.pk::

    [my_page: /<pk>]
    @crud_edit(#cat)

    #cat
    --------
    name
    age: int

@crud_delete
--------------

Shows a confirmation form asking to delete a model instance. The instance is removed upon form submission. The current model id is taken from url.pk::

    [my_page: /<pk>]
    @crud_delete(#cat)

    #cat
    --------
    name
    age: int

@crud_detail
--------------

Shows details of a model instance. The current model id is taken from url.pk::

    [my_page: /<pk>]
    @crud_detail(#cat)

    #cat
    --------
    name
    age: int

@crud
---------
Automatically creates the four pages described above::

    [my_page: /mypage/]
    @crud(#cat)

    #cat
    --------
    name
    age: int

