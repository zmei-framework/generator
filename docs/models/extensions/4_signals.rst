@pre_* @post_*
#################

There is an entire collection of annotations that add signal handlers:

@pre_save
    Executes code before model save
@post_save
    Executes code after model save
@pre_delete
    Executes code before model delete
@post_delete
    Executes code after model delete
@m2m_changed
    Executes code when the many() relationship has been changed

.. note::

    See `Django Siganl documentation <https://docs.djangoproject.com/en/2.0/ref/signals/>`_ to see what arguments
    are available inside the handler code.

Example::

    #cat
    -----------------
    name

    @post_save {
        print("Meow!")
    }

It is python multiline block expression (:ref:`PythonCode`).
You can also use :ref:`Imports` to use external code in expression.