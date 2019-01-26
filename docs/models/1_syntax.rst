Overview
####################

Models are the cornerstone of the Zmei generator. Zmei automates all routine
work with Django’s models.

Here is an example of simple model::

    #cat
    --------
    name
    age: int

Header
-----------

"#cat" is the header part of the model.

"#" is a marker that tells Zmei that it’s starting a model.
"cat" is is the model name. The model name cannot contain spaces.
The name should be written in lower-case letters.

Examples of model names:

- my_fancy_model
- dog
- block1

The header may also include a verbose name::

    #cat: Kitty
    --------
    name
    age: int

And a verbose name plural::

    #cat: Kitty/Kitties
    --------
    name
    age: int

Another thing that may be placed in the header is a parent name::

    #animal->cat
    --------
    name
    age: int

See the :ref:`Inheritance` section for details.

Fields
----------

"name" and "age" are fields. Each field is displayed on a new line. Grouping fields with empty lines between them 
on a new line is also ok, and highly recommended::

    #cat
    --------
    name
    age: int

    owner_name
    owner_phone

The syntax for a field is::

    [modifiers] field_name: field_type

field_type is optional and is seen as "text(100)" by default.

You can read more about field types in the :ref:`FiledTypes` section.


Field modifiers
^^^^^^^^^^^^^^^^^^^^

The field may have a prefix with modifiers, e.g. required modifier::

    #cat
    --------
    *name
    *age: int

    owner_name
    owner_phone

This means that the name and age fields are required.

.. note::
    There are several field modifiers that can be used to change field behavior:

    **$**
        Make field localizable. Any type of field could be localized, including relationships.
        `django-modeltranslation <https://github.com/deschler/django-modeltranslation>`_ is used.

    **=**
        Value of this field is used when object is printed (__str__() method)

    **&**
        Unique index is created on a field

    **!**
        Index is created for a field

    **\***
        Required field (not blank). The field does not allow empty values when submitted through django forms.

    **~**
        Not null. Adds a "not null" constraint on the database level.


Help message
^^^^^^^^^^^^^^^^^^^^

Help message is an easy way to add comments to model fields. This message will be shown on 
forms as a "help message", usually a small text on the right side of the name::

    #cat
    --------
    *name
    *age: int

    owner_name
    *owner_phone ?phone is required if the cat is get lost

Verbose name
^^^^^^^^^^^^^^^^^^^^

A field name may not contain spaces, so it is sometimes useful to provide descriptive read-only name::

    #sauna_heater
    ----------------
    power: int /Maximum power
    room_size: int /"Sauna room size (min - max)"


Custom options
^^^^^^^^^^^^^^^^

When generator is not powerful enough for you, you can add extra options to fields::

    #boo
    ----------
    mydate: create_time

    // This will add option to field
    abc: str(255) ..{unique_for_date="mydate"}

    // This will replace all options of the fields
    abc: str {max_length=255, unique_for_date="mydate"}

    // This will replace entire field definition, so you are free to use custom fields
    abc: {models.BinaryField(max_length=255)}



Annotations
--------------

Annotations are super-powers in Zmei generator. They add different abilities to models, e.g. @admin generates an admin panel, and @rest adds an automatic REST API::

    #page
    -------------
    =*$title
    ~$slug: slug(title)
    $url

    @admin(
        list: *
    }
    @rest
    @api


Read more about extras in the :ref:`ModelExtras` section.




