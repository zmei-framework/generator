@tree
###################


@tree as you may assume, adds parent<->child relation to the model.
Functionality is based on django-mptt package.

Simple tree
==============

Simple example:

.. code-block:: col
    :caption: models.py

    #category
    --------
    name

    @tree

@admin also knows how to work with tree:

.. code-block:: col
    :caption: admin.py

    #category
    --------
    name

    @tree
    @admin

Polymorphic tree
============================

One special case is @tree, when model is polymorphic. Then special handling added to admin section:

.. code-block:: col
    :caption: admin.py

    #menu
    -------------
    =label
    url: << '#';
    kind: << self._meta.verbose_name;
    nofollow: bool
    new_window: bool

    @admin {list: nofollow, new_window, kind}
    @tree(+polymorphic_list)

    #menu~>placeholder /Placeholder link
    ----------------------
    @admin

    #menu~>root /Root element of menu
    ----------------------
    =ref /Reference name ?used in template
    @admin

    #menu~>route_link /Route based link
    ----------------------
    route_name
    url: << reverse(self.route_name) if self.route_name else '';

    @admin

    #menu~>external_link
    ----------------------
    link
    url: << self.link;

    @admin
