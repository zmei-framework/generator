
What is .col file?
==================

Col file is input for generator. Each col file result into one Django application.
Every Django project consists of one or several applications, same you
can create several .col file.

.. note::
    Every col file produces one Django application.

For example two col files:

.. image:: img/two-files.png
    :width: 400px

Produce following structure:

.. image:: img/structure1.png


Generator produces "app" application. That contains common application code like settings,
urls, wsgi, etc...

And two applications "cats", "dogs", that contain application-specific code.
