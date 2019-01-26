

.. _FieldList:

Field list
===================

Field list syntax is used in many places, like @admin, @rest and other annotations.

All fields
^^^^^^^^^^^^^

Example::

   #boo
   ----------
   abc
   cda

   @admin(list: *)


Fields selected: 'abc', 'cda'

All fields with parent fields
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Example::

   #foo
   ----------
   a

   #foo->boo
   ----------
   b
   c

   @admin(list: *)


Fields selected: 'a', 'b', 'c'


Only current level fields
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Example::

   #foo
   ----------
   a

   #foo->boo
   ----------
   b
   c

   @admin(list: .*)


Fields selected: 'b', 'c'


Only specified fields
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Example::

   #boo
   ----------
   weight
   size_x
   size_y
   color_front
   color_back

   @admin(
      list: weight, size_x, size_y, color_front
   )


Fields selected: 'weight', 'size_x', 'size_y', 'color_front'


Exclude some fields
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Example::

     #boo
     ----------
     weight
     size_x
     size_y
     color_front
     color_back

     @admin(
         list: *, ^color_front, ^size_x
     )

Fields selected: 'weight', 'size_y', 'color_back'



Exclude by wildcard
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Example::

   #boo
   ----------
   weight
   size_x
   size_y
   color_front
   color_back

   @admin(
      list: *, ^color_*
   )

Fields selected: 'weight', 'size_x', 'size_y'


Include by wildcard
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Example::

   #boo
   ----------
   weight
   size_x
   size_y
   color_front
   color_back

   @admin(
      list: weight, size_*
   )

Fields selected: 'weight', 'size_x', 'size_y'


All fields with parent fields
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Example::

   #boo
   ----------
   abc
   cda

   @admin(list: *)


Fields selected: 'abc', 'cda'


