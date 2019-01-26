.. _FiledTypes:

Field types
================

Here the core field types are outlined, except for relation fields and calculated fields 
which are described in a separate section.

Text
---------

str
^^^^^^^^^

Str refers to any unicode string with a fixed length. The database field will be VARCHAR

In its simplest form, it’s just a text line with the default length of 100::

    my_field: str

The text length can also be specified::

    my_field: str(255)

The str field can also contain predefined choices - in this case a select box will be displayed in forms instead of an  input field::

    my_field: str(10, choices=Monday, Tuesday)

Predefined choices may also have a key::

    my_field: str(10, choices=mon:Monday, tue:Tuesday)

And the field length can be auto-calculated::

    my_field: str(?, choices=mon:Monday, tue:Tuesday)

Unicode symbols in the label are allowed::

    my_field: str(?, choices=mon:"Понедельник", tue:"Teisipäev")


text
^^^^^^^^^^^^^

Long text is mapped to the TEXT field in the database::

    my_field: text


html
^^^^^^^^^

Html is same as longtext, except it is represented as Html editor::

    my_field: html


slug
^^^^^^^^^

A slug field is another type of text field, but it’s generated from another field by 
replacing all characters that are not latin or digits with some latin transcription.

Most commonly slugs are used in urls.

The syntax is as follows::

    my_field: slug(target_field)

target_field should be a text field.

Several fields also can be specified::

    my_field: slug(target_field, another)

.. note::
    The slug field length is taken from the target field.


Number
-----------

int
^^^^^^^^

Just an integer::

    my_field: int

Int supports choices, the syntax is same as with text field::

    my_field: int(choices=1, 2, 3, 4)
    my_field: int(choices=1:Monday, 2:Tuesday)
    my_field: int(choices=1:"Понедельник", 2:"Teisipäev")

float
^^^^^^^^^^

Float is FLOAT in the database ::

    my_field: float

.. note::

    For storing money related numbers, it's better to use float `<https://stackoverflow.com/questions/3730019/why-not-use-double-or-float-to-represent-currency>`_

decimal
^^^^^^^^^^^^

Decimal is mapped to the DECIMAL field in the database. A good choice for storing currency amounts::

    myfield: decimal

bool
---------

True or False value, False by default::

    myfield: bool

You can also set a default value explicitly::

    myfield: bool(true)

Date
---------

date
^^^^^^^^^

Date value without time::

    my_field: date

datetime
^^^^^^^^^^^^^

Date value with time::

    my_field: datetime


create_time
^^^^^^^^^^^^^^^^

Same as datetime, but the field value is set to current date and time when a new object is created::

    my_field: create_time

update_time
^^^^^^^^^^^^^^^^

Same as datetime, but the field value is set to current date and time when a new object is updated::

    my_field: update_time


Files
----------

file
^^^^^^^^^

Field for storing files. In admin it is represented as a file field::

    my_field: file



image
^^^^^^^^^^

Same as file, but allows only images::

    my_field: image

With image, you can also specify image size, it is used when generating REST API::

    my_field: image(default=300x300|crop|upscale)

