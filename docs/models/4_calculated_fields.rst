

Calculated fields
---------------------------

Calculated fields are fields that are generated at the moment of access and can contain ant one-liner expressions::

    my_field: << 3 + 3;

Calculated field start with "<<" symbols, following by any valid python code, and closed by ";"

.. note::

    As calculated field namely is generated during access, accessing it many time, causes expression to be evaluted
    many times. Watch the performance!

Model instance is accessible through **self**::

    #man
    -----
    name
    lastname
    fullname: << '{} {}'.format(self.name, self.lastname);

There is also a way to define static (class-level) calculated fields, they have access to **cls** variable
that represents class::

    my_field: <@ 'class name is: {}'.format(type(cls));

Both class-level and instance level fields have access to get_ref() method, which return model ref, ex "cat" for
"#cat" model::

    my_field: << 'My ref is {}'.format(self.get_ref());
    my_field: <@ 'My ref is {}'.format(cls.get_ref());


Use external functionality in expressions
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

You can use any functionality in expressions by adding import section::

    %%
    %%
    from django.urls import reverse
    %%

    #menu_item
    -------------
    =$label

    page: one(#page)
    url: << reverse('pages.page', kwargs={'slug': self.page.slug or ''});

.. note::

    Avoid too complex expression. There is @mixin extra, that allows to add complex functionality to the model.


