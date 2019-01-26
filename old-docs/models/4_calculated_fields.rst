

Calculated fields
---------------------------

Calculated fields are fields that are generated at the moment of access and can contain a one-line python expressions (:ref:`PythonCode`)::

    my_field := 3 + 3;

Calculated field start with "<<" symbols, following by any valid python code, and end with ";"

.. note::

    Since a calculated field is generated during access, accessing it many times causes the expression to be evaluated many times. Watch the performance!

Model instance is accessible through **self**::

    #man
    -----
    name
    lastname
    fullname := '{} {}'.format(self.name, self.lastname);

There is also a way to define static (class-level) calculated fields, they have access to the **cls** variable 
that represents class::

    my_field @= 'class name is: {}'.format(type(cls));

Both class-level and instance level fields have access to the get_ref() method, which returns model ref, e.g. "cat" for the 
"#cat" model::

    my_field := 'My ref is {}'.format(self.get_ref());
    my_field @= 'My ref is {}'.format(cls.get_ref());

Field can be declared as "boolean". It is useful in django admin::

    my_field := ! 'My ref is {}'.format(self.get_ref());


Use external functionality in expressions
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

You can use any functionality in expressions by adding an import section::

    from django.urls import reverse

    #menu_item
    -------------
    =$label

    page: one(#page)
    url := reverse('pages.page', kwargs={'slug': self.page.slug or ''});

.. note::

    Avoid overly complex expressions. There is a @mixin extra that allows complex functionality to be added to the model.
    You can also use :ref:`Imports` to use external code in expression.