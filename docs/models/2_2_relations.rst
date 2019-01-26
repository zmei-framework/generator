

Relationships
----------------

Relationships are used to link related models to each other. The generator currently supports basic types of relationships, but they allow almost any kind of relationship to be expressed.

.. note::

    The absence of some more complex relationship types is caused by the need to prevent a complicated situation with  automatic migrations. However, they may be added in the future.

Common syntax
^^^^^^^^^^^^^^^^

The syntax is as follows::

    type(target -> related_name)

**type** is one of: one, many

**target** is either a model reference that starts with #, or a full classname

**related_name** is optional, and denotes what will be the backreference on the opposite side of the relationship. related_name will not be created if it has not been specified

one
^^^^^^

A foreign key relationship::

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

A Many2Many relationship::

    #cat
    ------
    name


    #man
    ------
    cats: many(#cat)
