@pre_* @post_*
###########

There is entire collection of extras that add signal handlers:

@pre_save
    Executes code before model save
@post_save
    Executes code after model save
@pre_delete
    Executes code before model delete
@post_delete
    Executes code after model delete
@m2m_changed
    Executes code when many() relation has been changed

.. note::

    See `Django Siganl documentation <https://docs.djangoproject.com/en/2.0/ref/signals/>`_ to see what arguments
    are available inside handler code.

Example:

.. code-block:: col
    :caption: models.py

    #cat
    -----------------
    name

    @post_save<<
        print("Meow!")
    >>
