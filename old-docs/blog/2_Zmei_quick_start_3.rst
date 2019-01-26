
.. _60sec_3:

Deploy Django application to a public url in 60 seconds
=======================================================

.. post:: Nov 30, 2018
   :category: Tutorial
   :tags: intro, deploy, 60sec
   :author: Alex Rudakov

This is the last article from "Django in 60 seconds" series.

* :ref:`60sec_1`
* :ref:`60sec_2`
* :ref:`60sec_3`

In the previous article, we created a simple Django application, added rest and admin panel.
Now it is time to deploy the application.

.. note::

    We assume you have linux or macosx, otherwise, you may need to adapt commands to your system.


Check zmei version
--------------------

Check zmei is updated and contains deployment feature::

    $ pip install -U zmei-cli


Deploy application
--------------------

Deploy is easy::

    $ zmei deploy

    ...
    Deploy done!
    Your application is up at http://543e268a-f42e-11e8-a58d-8c85905e31e2.genius-apps.com/


At the end of the deployment process you will see public url of the application. Go to that url to see your app is working already!


Create admin user
--------------------

Zmei creates a "micro virtual machine" that contains nginx + uwsgi + mysql + redis + celery and ssh as well.

Let's use ssh to create admin user::

    $ zmei ssh

And when you are in::

    $ python manage.py createsuperuser

With this username, you can go to /admin/ part of your application.

Mine is here: http://543e268a-f42e-11e8-a58d-8c85905e31e2.genius-apps.com/admin/
Username "alex", password "123123".

API
---------
And don't forget we have also public api: http://543e268a-f42e-11e8-a58d-8c85905e31e2.genius-apps.com/api/

.. raw:: html

    <iframe width="660" height="415" src="https://www.youtube.com/embed/6HxbInMEeYQ" frameborder="0" allow="accelerometer; autoplay; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>


Conclusion
-----------------------

That was a very small part of what actually Zmei generator is capable of. Next article soon ... Stay tuned ;)

P.S. Zmei Apps are in early beta, please don't use it for production. But feel free to have fun with it, write feedback.
After beta, there will be one application free, and others $3/month (not sure yet).
