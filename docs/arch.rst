.. _Installation:

Installation
====================

First, go to https://zmei-framework.com and create new account.

Install package
-------------------

Install zmei-gen from repository::

    $ pip install zmei-cli

Make sure zmei is working::

    $ zmei
    Usage: zmei [OPTIONS] COMMAND [ARGS]...

    Options:
      --help  Show this message and exit.

    Commands:
      app     Application management
      deploy  Deploy
      gen
      key     Ssh key management
      login   Deploy to hyper.sh
      logout  Deploy to hyper.sh
      ssh     Ssh into deployed application

Log in with Zmei apps account
-------------------------------

Create a new Zmei account at https://zmei-framework.com/auth/registration/

Login using zmei command::

    $ zmei login


Update package
------------------

Update zmei-cli from repository::

    $ pip install -U zmei-cli

Delete package
------------------

Update zmei-cli from repository::

    $ pip uninstall zmei-cli


