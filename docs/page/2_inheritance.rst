.. _PageParent:

Page inheritance
###################

Basics
=========

Pages can extend each other::

    [base]
    foo:= 123

    [base->index: /]
    boo:= 321

If one page extends another, it means that all the variables from the parent page will be accessible through the child page.

.. note::

    Generated templates will also extend each other, repeating view hierarchy.


Urls are also subject to inheritance::

    [foo: /lala/]

    [foot->cat: ./cat/<pk>]

Url of cat page will be "/lala/cat/<pk>".
Without dots, urls are not inherited.


Multilevel inheritance
=======================

There is no restriction on inheritance deepness::

    [level0]

    [level0->level1]

    [level1->level2]

    [level2->level3]

    [level3->level4]

    [level4->level5]

    [level5->level6]

    [level6->level7]

Hide variable from children
=============================

Sometimes it is useful to hide some variables from the child page, but keep the hierarchy::

    [projects: /projects/]
    _projects:= Project.objects.all()
    foo:= 123

    [projects->project: /projects/<pk>]
    project:= Project.objects.get(pk=url.pk) @or_404

The "projects" variable will be accessible only in "projects" view, but not in "project".
This allows you to not execute "Project.objects.all()" query in children views.

Access data from parent
=========================

The parent page’s data is not available in local scope, but can be accessed through a "data" object::

    [base]
    foo:= 123

    [base->index: /]
    boo:= 321 + data.foo
