
Themes
===============

Crud generates very flexible template structure, that can be easily customised.

For this code ...::

    [gb: /gb]
    @crud(#guestbook)


    #article
    ------------
    title
    text: html /Html text ? just text

    @admin(list: *)


    #guestbook
    ------------
    name
    email
    message: text

...  template layout looks like this:

.. image:: img/crud.png

Also note, that "default" is a theme name. You can change theme name for crud::


    [gb: /gb]
    @crud(#guestbook, theme: another)

    #guestbook
    ------------
    name
    email
    message: text

