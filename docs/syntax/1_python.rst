
.. _PythonCode:

Python expression
===================

Python expression may contain any valid python code.

One line python expression
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Syntax::

    := [rest of line is python code]
    @= [rest of line is python code]


One line of code that is valid python expression::

    := "foo {}".format(3 + 3)

Example::

    [index: /]
    msg := "hello"

    #foo
    ---------
    myfield := 3 + 3
    mystaticfield @= 3 + 3


Multiline python code
^^^^^^^^^^^^^^^^^^^^^^^^^

Syntax::

    { [any python code here] }

Example::

    [boo] {
        mydict = {"foo": 123}
        print(mydict["foo"])
    }
