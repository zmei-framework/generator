
.. _60sec_1:

Django application in 60 seconds
===================================

.. post:: Nov 24, 2018
   :category: Tutorial
   :tags: intro, 60sec
   :author: Alex Rudakov

In this small tutorial, we will learn how to create a very simple useless application, but it already can show the power of Zmei.

This is the first article in "Django in 60 seconds" series.

* :ref:`60sec_1`
* :ref:`60sec_2`
* :ref:`60sec_3`

Our app will manage cats list. Just for fun :)

Preparation
-----------------

First make sure you have installed generator. Documentation is here: :ref:`Installation`

Also create a virtual-environment for your project: https://docs.python-guide.org/dev/virtualenvs/

I will create a virtualenv using virtualenvwrapper::

    $ mkvirtualenv cats
    $ pip install zmei-cli

Col file
-----------

Create cats.col file::

    [index: /]
    @crud(#cat)

    #cat
    -----------
    =name
    age: int


Magic!
----------

Start zmei::

    $ zmei gen up

Out::

    Up!
    --------------------------------------------
    Generating ...
    --------------------------------------------
     +    /Users/aleksandrrudakov/dev/tmp3/app/templates/base.html
     +    /Users/aleksandrrudakov/dev/tmp3/cats/templates/cats/index_create.html
     +    /Users/aleksandrrudakov/dev/tmp3/app/wsgi.py
     +    /Users/aleksandrrudakov/dev/tmp3/cats/templates/cats/index_detail.html
     +    /Users/aleksandrrudakov/dev/tmp3/cats/urls.py
     +    /Users/aleksandrrudakov/dev/tmp3/cats/templates/cats/index_edit.html
     +    /Users/aleksandrrudakov/dev/tmp3/app/templates/crud/default/detail.html
     +    /Users/aleksandrrudakov/dev/tmp3/app/templates/crud/default/delete.html
     +    /Users/aleksandrrudakov/dev/tmp3/cats/__init__.py
     +    /Users/aleksandrrudakov/dev/tmp3/cats/templates/cats/index.html
     +    /Users/aleksandrrudakov/dev/tmp3/cats/views.py
     +    /Users/aleksandrrudakov/dev/tmp3/app/templates/crud/default/edit.html
     +    /Users/aleksandrrudakov/dev/tmp3/requirements.txt
     +    /Users/aleksandrrudakov/dev/tmp3/app/_urls.py
     +    /Users/aleksandrrudakov/dev/tmp3/cats/templates/cats/index_delete.html
     +    /Users/aleksandrrudakov/dev/tmp3/_requirements.txt
     +    /Users/aleksandrrudakov/dev/tmp3/cats/templates/cats/base.html
     +    /Users/aleksandrrudakov/dev/tmp3/app/templates/crud/default/list.html
     +    /Users/aleksandrrudakov/dev/tmp3/manage.py
     +    /Users/aleksandrrudakov/dev/tmp3/app/urls.py
     +    /Users/aleksandrrudakov/dev/tmp3/app/settings.py
     +    /Users/aleksandrrudakov/dev/tmp3/app/__init__.py
     +    /Users/aleksandrrudakov/dev/tmp3/cats/models.py
     +    /Users/aleksandrrudakov/dev/tmp3/app/_settings.py
     +    /Users/aleksandrrudakov/dev/tmp3/app/templates/crud/default/create.html
    >  Installing pip dependencies...
    Requirement already satisfied: django>2 in /Users/aleksandrrudakov/.virtualenvs/gen/lib/python3.6/site-packages (from -r _requirements.txt (line 3)) (2.1.2)
    Requirement already satisfied: wheel in /Users/aleksandrrudakov/.virtualenvs/gen/lib/python3.6/site-packages (from -r _requirements.txt (line 4)) (0.32.2)
    Requirement already satisfied: zmei-utils==0.1.12 in /Users/aleksandrrudakov/dev/zmei (from -r _requirements.txt (line 5)) (0.1.12)
    Requirement already satisfied: pytz in /Users/aleksandrrudakov/.virtualenvs/gen/lib/python3.6/site-packages (from django>2->-r _requirements.txt (line 3)) (2018.6)
    Requirement already satisfied: djangorestframework in /Users/aleksandrrudakov/.virtualenvs/gen/lib/python3.6/site-packages (from zmei-utils==0.1.12->-r _requirements.txt (line 5)) (3.9.0)
    >  Migrating database
    Migrations for 'cats':
      cats/migrations/0001_initial.py
        - Create model Cat
    Operations to perform:
      Apply all migrations: admin, auth, cats, contenttypes, sessions
    Running migrations:
      Applying contenttypes.0001_initial... OK
      Applying auth.0001_initial... OK
      Applying admin.0001_initial... OK
      Applying admin.0002_logentry_remove_auto_add... OK
      Applying admin.0003_logentry_add_action_flag_choices... OK
      Applying contenttypes.0002_remove_content_type_name... OK
      Applying auth.0002_alter_permission_name_max_length... OK
      Applying auth.0003_alter_user_email_max_length... OK
      Applying auth.0004_alter_user_username_opts... OK
      Applying auth.0005_alter_user_last_login_null... OK
      Applying auth.0006_require_contenttypes_0002... OK
      Applying auth.0007_alter_validators_add_error_messages... OK
      Applying auth.0008_alter_user_username_max_length... OK
      Applying auth.0009_alter_user_last_name_max_length... OK
      Applying cats.0001_initial... OK
      Applying sessions.0001_initial... OK
    >  Starting django
    python manage.py runserver 127.0.0.1:8000
    >  Watching for changes...
    Performing system checks...

    System check identified no issues (0 silenced).
    November 20, 2018 - 23:22:26
    Django version 2.1.2, using settings 'app.settings'
    Starting development server at http://127.0.0.1:8000/
    Quit the server with CONTROL-C.


Results
-----------

Go to "http://127.0.0.1:8000/" to see results.

.. note::

    The result of the generation is a usual Django app, so you can run it with "python manage.py runserver" as well.

.. raw:: html

    <iframe width="660" height="415" src="https://www.youtube.com/embed/WLwYC-rspK4" frameborder="0" allow="accelerometer; autoplay; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>


Deploy it
-----------

The result is a usual Django application so you can deploy it for example on https://www.pythonanywhere.com/ as any usual Django application.


... to be continued
-----------------------

Next time we will add the Django administration panel and REST API to our cat manager application. Stay tuned … ;)