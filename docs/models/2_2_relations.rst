

Relations
----------

Relations are used to link related models with each other. Generator supports currently
basic types of relations, but they allow to express almost any kind of relation.

.. note::

    Obsense of some more complex relation types are caused by need to prevent complex situation
    with automatic migrations. Through they may appear in future.

Common syntax
^^^^^^^^^^^^^^^^

Syntax is following::

    type(target -> related_name)

**type** is one of: one, many

**target** is either model reference started with #, or full classname

**related_name** is optional, and represents what will be back reference on oposite side of relation.
If not specified, related_name is not created

one
^^^^^^

Foreign key relation::

    #project
    --------
    name


    #task
    --------
    project: one(#project)


Related name can be specified::

    project: one(#project -> tasks)


many
^^^^^^^

Many2Many relation::

    #cat
    ------
    name


    #man
    ------
    cats: many(#cat)
