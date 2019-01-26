@tree
###################


@tree, as you may assume, adds a parent<->child relationship to the model. 
The functionality is based on the django-mptt package

Simple tree
==============

A Simple example::

    #category
    --------
    name

    @tree

@admin also knows how to work with tree::

    #category
    --------
    name

    @tree
    @admin

Polymorphic tree
============================

Consider the particular case of @tree when the model is polymorphic. If so, special handling is added to the admin section::

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
