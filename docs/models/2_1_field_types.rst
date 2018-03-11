Field types
================

Here are outlined core field types, except relation fields and calculated fields, that
are described in separate section.

Text
---------

text
^^^^^^^^^

Text is a any unicode string with fixed length. Database field will be VARCHAR

In simplest form, it's just a text line with default length of 100::

    my_field: text

Text length can be specified::

    my_field: text(255)

Also text field can contain predefined choices, this allows to show select box in forms instead of
input field::

    my_field: text(10, choices=Monday, Tuesday)

Choices may have also a key::

    my_field: text(10, choices=mon/Monday, tue/Tuesday)

And field length maybe auto-calculated::

    my_field: text(?, choices=mon/Monday, tue/Tuesday)

Unicode symbols in label are allowed::

    my_field: text(?, choices=mon/"Понедельник", tue/"Teisipäev")


longtext
^^^^^^^^^^^^^

Long text is mapped to TEXT field in db::

    my_field: longtext


html
^^^^^^^^^

Html is same as longtext, except it is represented as Html editor::

    my_field: html


slug
^^^^^^^^^

Slug field is another type of text field, but it's generated from another field,
by replacing all character that are not latin or digits with some latin transcription.

Most commonly slugs are used in urls.

Syntax is following::

    my_field: slug(another_field)

another_field should be a text field.


Number
-----------

int
^^^^^^^^

Just an integer::

    my_field: int

Int support choices, syntax is same as with text field::

    my_field: int(choices=1, 2, 3, 4)
    my_field: int(choices=1/Monday, 2/Tuesday)
    my_field: text(choices=1/"Понедельник", 2/"Teisipäev")

float
^^^^^^^^^^

Float is FLOAT in database ::

    my_field: float

.. note::

    For storing money related numbers, it's better to use float `<https://stackoverflow.com/questions/3730019/why-not-use-double-or-float-to-represent-currency>`_

decimal
^^^^^^^^^^^^

Decimal is mapped to DECIMAL field in db. Good choice to store currency amounts::

    myfield: decimal

bool
---------

True or False value, False by default::

    myfield: bool

You can also specify default value explicitly::

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

Same as datetime, but field value is set to current date and time when a new object is created::

    my_field: create_time

update_time
^^^^^^^^^^^^^^^^

Same as datetime, but field value is set to current date and time when a new object is updated::

    my_field: update_time


Files
----------

file
^^^^^^^^^

Field for storing files. In admin it is represented as django-filer file field::

    my_field: file

folder
^^^^^^^^^^^


Field for storing files. In admin it is represented as django-filer folder field::

    my_field: folder


image
^^^^^^^^^^

Same as file, but allows only images::

    my_field: image

With image, you can also specify image size, it is used when generating REST API::

    my_field: image(default=300x300|crop|upscale)
