@admin
##########

Admin annotation generates Django admin class and register into the settings.

Defaults
==============

By default all fields are editable and list will show no fields::

    #boo
    ----------
    abc
    cda

    @admin


List
========

You can specify what fields to use using :ref:`FieldList` syntax::

    #boo
    ----------
    abc
    cda

    @admin(list: *)


Fields
========

Which fields to show in new and edit views? (:ref:`FieldList` syntax)::

    #boo
    ----------
    abc
    cda

    @admin(fields: *)


Read-only fields
================

You can specify what fields are non-editable (:ref:`FieldList` syntax)::

    #boo
    ----------
    abc
    cda

    @admin(read_only: *)


List editable
================

Fields maybe edited inline right in a list view (:ref:`FieldList` syntax)::

    #boo
    ----------
    abc
    cda

    @admin(list_editable: *)


List filter
================

Show filters on top of admin list (:ref:`FieldList` syntax)::

    #boo
    ----------
    abc
    cda

    @admin(list_filter: *)

List search
================

Show search field and perform search by fields given (:ref:`FieldList` syntax)::

    #boo
    ----------
    abc
    cda

    @admin(list_search: *)


Polymorphic admin
=======================

Inheritance for admin is handled transparently::

    #data_source
    --------------
    name

    @admin

    #data_source->db_data_source
    -------------------
    database
    server

    @admin

    #data_source->file_data_source
    -------------------
    source: file

    @admin

In this case django-polymorphic models and admin-side are generated automatically,
so when creating new "data_source" in admin, you will get an option, which type of model do you want to create.


Inlines
=====================

Simple inline
^^^^^^^^^^^^^^^^

You can have inlines::

    #foo
    -------
    a
    b

    @admin(
        inline: lala
    )

    #bar
    --------
    rel: one(#foo -> lala)
    c
    d


Configure details
^^^^^^^^^^^^^^^^^^^^^

Some useful configuration options::

    #foo
    -------
    a
    b

    @admin(
        inline: lala(
            type: stacked
            extra: 300
            fields: *, ^c
        )
    )

    #bar
    --------
    rel: one(#foo -> lala)
    c
    d

Type: stacked (form under another), tabular (as a table), polymorphic (see later)
extra: amount of empty lines
Fields: fields to show (:ref:`FieldList` syntax)

Polymorphic inline
^^^^^^^^^^^^^^^^^^^

Inlines can refer to polymorphic models::

    #server
    ----------------
    name

    @admin(
        inline: data_sources(type: polymorphic)
    )

    #data_source
    --------------
    server: one(#server -> data_sources)
    name

    @admin

    #data_source->db_data_source
    -------------------
    database
    server

    @admin

    #data_source->file_data_source
    -------------------
    source: file

    @admin

Custom css & js in admin
===========================

As easy as::

    #foo
    -------
    a

    @admin(
        css: "foo.css", "another/boo.css"
        js:
            "foo.js",
            "another/boo.js"
    )

Translatable fields in admin
===============================

Admin-side can be auto-configured to use django-modeltranslations package::

    @langs(en)

    #boo
    ----------
    $abc
    cda

    @admin

Django-suit tabs
=====================

Single tab
^^^^^^^^^^^^^^

Admin can show tabs on edit/new view::

    @suit

    #boo
    ----------
    a
    b
    c

    @admin(
        tabs: foo(*)
    )

In this example we show one tab with name "foo" that contains all fields (:ref:`FieldList` syntax)


Multiple tabs
^^^^^^^^^^^^^^

We can also show several tabs::

    @suit

    #boo
    ----------
    a
    b
    c

    @admin(
        tabs: one(a), two(b,c)
    )

Tab "one" will show "a" field and tab "two" will show fields "b", "c".


General tab
^^^^^^^^^^^^^^

If some fields are not in tabs, tab "general" is created automatically::

    @suit

    #boo
    ----------
    a
    b
    c

    @admin(
        tabs: one(a)
    )

Tab "one" will show "a" field and tab "general" will show fields "b", "c".

To prevent this, you can specify "fields:" explicitly::

    @suit

    #boo
    ----------
    a
    b
    c

    @admin(
        tabs: one(a)
        fields: a
    )


Tab "one" will show "a" field and no other tabs are displayed.

Another example::

    @suit

    #boo
    ----------
    a
    b
    c

    @admin(
        tabs: one(a)
        fields: *, ^b
    )

Tab "one" will show "a" field and tab "general" will show "b" field


All but some...
^^^^^^^^^^^^^^^^^^^

Field will be displayed only in tab where it was last mentioned::

    @suit

    #boo
    ----------
    a
    b
    c
    d

    @admin(
        tabs: foo(*), lolo(b, d)
    )

Tab "foo" will show "a", "c" fields and tab "lolo" will show "b", "d" fields

Verbose name
^^^^^^^^^^^^^^^

By default tab gets label by capitalising it's name, but you can define it explicitly::

    @suit

    #boo
    ----------
    a
    b
    c

    @admin(
        tabs: foo "My tab"(*)
    )

Tab "foo" with label "My tab" will show fields "a", "b", "c"

Complex example
^^^^^^^^^^^^^^^^^^

Car example::

    @suit

    #car
    -------
    nr
    mark
    model
    weight: int
    crashed: bool(true)
    painted: bool

    @admin(
        tabs: main(*), options(crashed, painted)
        fields: *, ^weight
    )

Tab "main" will show "nr", "mark", "model" fields, tab "options" will show "crashed", "painted" fields.


Inlines
^^^^^^^^^

Inlines also can be used in tabs::

    @suit

    #foo
    -------
    a
    b

    @admin(
        inline: lala(
            type: stacked
            extra: 300
            fields: *, ^c
        )
        tabs: main(*), other(lala)
    )

    #bar
    --------
    rel: one(#foo -> lala)
    c
    d
