Overview
####################

Models are cornerstone of Genius generator. Genius automates all routine
work with Django's models.

Here is example of simple model::

    #cat
    --------
    name
    age: int

Header
-----------

"#cat" is header part of model.

"#" is marker, that tells Genius that it's model starting.
"cat" is model name. Model name can not contain space characters. Name
should be lower-case.

Model names, examples:

- my_fancy_model
- dog
- block1

Header also may include verbose name::

    #cat: Kitty
    --------
    name
    age: int

And verbose name for plural::

    #cat: Kitty/Kitties
    --------
    name
    age: int

Another thing that may be placed in header is parent name::

    #animal->cat
    --------
    name
    age: int

See :ref:`Inheritance` section for details.

Fields
----------

"name" and "age" are fields. Each field is defined on a new line. Grouping fields with empty lines between them
on a new line is also ok, and highly adviced::

    #cat
    --------
    name
    age: int

    owner_name
    owner_phone

Syntax fo field is::

    [modifiers] field_name: field_type

field_type is optional and is "text(100)" by default.

You can read more about field types in :ref:`FiledTypes` section.


Field modifiers
^^^^^^^^^^^^^^^^^^^^

Field may be prefixed with modifiers, ex required modifier::

    #cat
    --------
    *name
    *age: int

    owner_name
    owner_phone

It means name and age fields are required.

.. note::
    There are several field modifiers to change a field behavior:

    **$**
        Make field localaizable. Any type of field could be localized, including relations.
        `django-modeltranslation <https://github.com/deschler/django-modeltranslation>`_ is used.

    **=**
        Value of this field is used when object is printed (__str__() method)

    **&**
        Unique index is created on a field

    **!**
        Index is created for this a field

    **\***
        Required field (not blank). Field do not allow empty value when submitted through django forms.

    **~**
        Not null. Adds "not null" constraint on database level.


Help message
^^^^^^^^^^^^^^^^^^^^

Help message is a easy way to add comments to model fields. This message will be shown on
forms as a "help message", usually a small text on the right side of the name::

    #cat
    --------
    *name
    *age: int

    owner_name
    *owner_phone ?phone is required if the cat is get lost

Verbose name
^^^^^^^^^^^^^^^^^^^^

Field name may not contain spaces, so it is useful sometimes, to provide descriptive human-readable name::

    #sauna_heater
    ----------------
    power: int /Maximum power ?kw
    room_size: int /Sauna room size (min - max)


Extras
----------

Extras is super-powers in Genius models. They ad different abilities to models, like @admin generates admin panel and
@rest adds automatic rest api::

    #page
    -------------
    =*$title
    ~$slug: slug(title)
    $url

    cover_image: image
    cover_image_by: longtext

    $text: html
    $aside: longtext

    top_menu_only: bool

    template: text(?, choices: <glob:"templates/{page*.html}">)

    @admin {
        list: title, slug, url, top_menu_only
        tabs:
            general(title, slug, url),
            text(text, aside),
            cover(cover_image, cover_image_by, top_menu_only)
    }
    @tree
    @mixin(pages.mixins.PageDeepUrl)


Read more about extras in :ref:`ModelExtras` section.




