

.. _tutor_i18n:

Full i18n of Django application (urls, models, templates, code)
================================================================

.. post:: Dec 1, 2018
   :category: Tutorial
   :tags: i18n, models, video
   :author: Alex Rudakov

This tutorial we see how to generate proper multilanguage configuration for
Django application, including:

* Template text translation
* Strings in python code translation
* Model fields translation
* Model field labels translation
* Url translation

And all of this with just a few commands.

Preparation
--------------

Django uses gettext for i18n. You should figure out how to set it up on your system.
For me (macos) it was::

    brew install gettext
    brew link gettext --force


Video with explanations
---------

Below is a text version of same tutorial. You can use it as a copy-paste source.

.. note::

    All the small troubles you will see on video (to_string translation, menu not working etc ...) are fixed. See above.

.. raw:: html

    <iframe width="660" height="415" src="https://www.youtube.com/embed/79byxRYdzgk" frameborder="0" allow="accelerometer; autoplay; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>


Starting point
------------------

For experiments I pick this col file::

    @suit

    [index: /]
    @markdown {
        # My library
    }
    @crud.books(
        #book
        list_fields: *, ^description
    )
    @crud.shelves(#shelf)

    #shelf: Shelf/Shelves
    ---------
    ="Shelf nr {me.number} at {me.location}"
    location
    number: int

    @admin

    #book: Book/Books
    --------
    =title
    description: html
    year: int
    author
    shelf: one(#shelf -> books)

    @admin

This is home a simple home library manager application.

Interesting things are:

* "Shelf/Shelves" - verbose name of a model and a plural form
* "one(#shelf -> books)" - relation
* ="Shelf nr {me.number} at {me.location}" - to string method

Otherwise, it's all concepts that we covered in previous tutorials.

@langs annotation
--------------------

Add lang annotation to specify that application is subject of i18n::

    @suit

    @langs(en, ru, et)

    [index: /]
    @markdown {
        # My library
    }
    @crud.books(
        #book
        list_fields: *, ^description
    )
    @crud.shelves(#shelf)

    #shelf: Shelf/Shelves
    ---------
    ="Shelf nr {me.number} at {me.location}"
    location
    number: int

    @admin

    #book: Book/Books
    --------
    =title
    description: html
    year: int
    author
    shelf: one(#shelf -> books)

    @admin

Translating model fields
------------------------

Field translations are using django-modeltranslations. Add "$" to the beginning of field name to activate::


    @suit

    @langs(en, ru, et)

    [index: /]
    @markdown {
        # My library
    }
    @crud.books(
        #book
        list_fields: *, ^description
    )
    @crud.shelves(#shelf)

    #shelf: Shelf/Shelves
    ---------
    ="Shelf nr {me.number} at {me.location}"
    $location
    number: int

    @admin

    #book: Book/Books
    --------
    =$title
    $description: html
    year: int
    author
    shelf: one(#shelf -> books)

    @admin

Url i18n
-----------

Just add "$" in the beginning of url pattern::


    @suit

    @langs(en, ru, et)

    [index: $/]
    @markdown {
        # My library
    }
    @crud.books(
        #book
        list_fields: *, ^description
    )
    @crud.shelves(#shelf)

    #shelf: Shelf/Shelves
    ---------
    ="Shelf nr {me.number} at {me.location}"
    $location
    number: int

    @admin

    #book: Book/Books
    --------
    =$title
    $description: html
    year: int
    author
    shelf: one(#shelf -> books)

    @admin

Language switcher
-------------------

It's not the best way to implement this, but add a menu::

    @suit

    @langs(en, ru, et)

    [index: $/]
    @menu.main(
        "Русский": "/ru/",
        "Eesti": "/et/",
        "English": "/en/"
    )
    @markdown {
        # My library
    }
    @crud.books(
        #book
        list_fields: *, ^description
    )
    @crud.shelves(#shelf)

    #shelf: Shelf/Shelves
    ---------
    ="Shelf nr {me.number} at {me.location}"
    $location
    number: int

    @admin

    #book: Book/Books
    --------
    =$title
    $description: html
    year: int
    author
    shelf: one(#shelf -> books)

    @admin

Generate translations
-------------------------

Collect messages::

    $ python manage.py makemessages --all

Translate all messages in locale/[lang_name]/LC_LOCALE/*.po

Compile messages::

    $ python manage.py compilemessages


That's it. The application is fully translated

