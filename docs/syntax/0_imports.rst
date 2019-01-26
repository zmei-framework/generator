
.. _Imports:

Code imports
=================

It is possible to reference external python code by importing from other modules.

Page imports
^^^^^^^^^^^^^^^^^^^^^

Page imports should be defined before  first page declaration.

Syntax::

    from [source.package.name] import [coma, separated, object, names]

Example::

    from mycompany.myutils import send_sms
    from datetime import timedelta

    [my_page: /] {
        send_sms("+372xxxxxx", "Hey!")
    }

    [another_page: /another/]
    foo: timedelta(days=3)



Model imports
^^^^^^^^^^^^^^^^^^^^^

Model imports should be defined after last page declaration (if any) and before first model declaration

Syntax::

    from [source.package.name] import [coma, separated, object, names]

Example::

    from mycompany.myutils import calc

    #foo
    ---------
    title
    lala := calc(self, 321)


Pages imports + models imports
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

You can have model imports and page imports in one file::

    from mycompany.myutils import send_sms
    from datetime import timedelta

    [my_page: /] {
        send_sms("+372xxxxxx", "Hey!")
    }

    [another_page: /another/]
    foo: timedelta(days=3)

    from mycompany.myutils import calc

    #foo
    ---------
    title
    lala := calc(self, 321)


models.py will get only model imports, and views.py will get only page imports.

