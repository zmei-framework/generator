Fields
###########

Field modifiers
================

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
=================

Verbose name
=================
