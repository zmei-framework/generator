
Main concepts
==================

.. note::

    In this section we show ways how you can work with @crud annotation, through same options work
    for all @crud_xxx annotations.

External models
------------------

You can use either Zmei model reference in crud or any external model::

    [boo: /lala]
    @crud(#foo)

    foo: /lala]
    @crud(some.Article, fields: title, text)

Note, that for external models you must specify fields as generator knows nothing about model fields.

Several CRUDs
---------------

You cannot use two CRUDs on page as they will have same name::

    // Parser will complain here
    [boo: /lala]
    @crud(#foo)
    @crud(#boo)

To make this possible, you need to give a name (descriptor) to the crud annotation::

    [boo: /lala]
    @crud(#foo)
    @crud.foo(#boo)

Descriptors are supported by all @crud_xxx annotations.

Different annotations can be used without descriptors::

    [boo: /lala]
    @crud(#foo)
    @crud_create(#boo)


CRUD with variables
---------------------

CRUD do not prevent you from using usual variables, and do other things as inheritance::

    [some_another_page->boo: /mycrud]
    lala := 123

    @crud(#foo)

Skipping views
------------------

By default @crud generates for pages: list (page itself) and subpages: detail, edit, create, delete. You can skip
any of those, if you don't need them::

    [boo: /mycrud]
    @crud(#foo, skip: delete, edit)

    #foo
    ------
    a
    b
    c



Fields
---------------------

You can sepcify field set to use::

    [boo: /mycrud]
    @crud(#foo, fields: *, ^b)

    #foo
    ------
    a
    b
    c

"fields:" use :ref:`FieldList` syntax.

List fields
---------------------

You can what fields to use on a list page::

    [boo: /mycrud]
    @crud(#foo, list_fields: *, ^b)

    #foo
    ------
    a
    b
    c

"list_fields:" use :ref:`FieldList` syntax.

Pk parameter name
-------------------

Crud generate subpage and adds urls like "/foo/<pk>/edit" for those subpages. You can customise name of this parameter::

    [boo: /mycrud]
    @crud(#foo, pk_param: foo)

    #foo
    ------
    a
    b
    c

Item name
-----------

"item_name" is name of object that is passed to template on detail and edit pages::

    [boo: /mycrud]
    @{extension_type_name}(#foo, item_name: foo)

    #foo
    ------
    a
    b
    c

Block name
--------------

Block name is name of the block where CRUD's html will be inserted.

Usual template for crud page looks like::

    {% extends 'data/gb.html' %}

    {% block content %}
    {% include 'crud/default/detail.html' with crud=crud.crud_gb_detail %}
    {% endblock %}

By specify block name::

    [boo: /mycrud]
    @crud(#foo, block: foo)

    #foo
    ------
    a
    b
    c

And you get::

    {% extends 'data/gb.html' %}

    {% block foo %}
    {% include 'crud/default/detail.html' with crud=crud.crud_gb_detail %}
    {% endblock %}


Object expression
--------------------

Object expression is useful if you already have object for crud inside context.
For example form for editing current user's name, may look like this::

    [profile_edit: /profile]
    @crud_edit(auth.User,
        object_expr := request.user
        fields: first_name, last_name
    )

"object_expr" use python code one-line syntax(:ref:`PythonCode`).


Edit restrictions
------------------------

For sure you will not allow anyone to edit your objects.
To restrict access you can use "can_edit" expression::

    [boo: /mycrud]
    @crud(#foo,
        can_edit := request.user.is_active and (request.user.is_staff or request.user.is_superuser)
    )

    #foo
    ------
    a
    b
    c

"can_edit" use python code one-line syntax(:ref:`PythonCode`).

"can_edit" is applied to edit, delete and create pages, as well it hides all the editing links.


Url prefix
--------------

You can prefix subpages with url_prefix::

    [boo: /mycrud]
    @crud(#foo,
        url_prefix: "this/is/custom/prefix/"
    )

    #foo
    ------
    a
    b
    c

Link suffix
--------------

Add some parameters to all the links::

    [boo: /mycrud]
    @crud(#foo,
        link_suffix: "category=url.category"
    )

    #foo
    ------
    a
    b
    c

Database query filter
------------------------

Sometimes you may need extension filtering::

    [boo: /mycrud]
    @crud(#foo{active=request.GET.get('active') == '1')

    #foo
    ------
    a
    b
    c

Filter use python code one-line syntax(:ref:`PythonCode`).

Success url
------------------

Crud allows to specify "on success" behavior::

    [boo: /mycrud]
    @crud(#foo
        => {{reverse_lazy('some_url', kwargs={{'param1': self.object.pk}})}}
    )

    #foo
    ------
    a
    b
    c

"Success url" use python code one-line syntax(:ref:`PythonCode`).

