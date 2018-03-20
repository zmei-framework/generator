
@sortable
#####################

@sortable mixing does two things:

1. adds list sorting to admin list and inlines
1. configure model to be sortable by order field

You are responsible for adding order field.


.. code-block:: col
    :caption: admin.py

    #todo_list
    --------
    title

    @admin {
        inline: items
    }

    #todo_item
    ------------
    list: one(#todo_list -> items)
    title
    order: int

    @sortable(order)
    @admin


There is also @order extra that does the same, but do not add anything to admin:

.. code-block:: col
    :caption: models.py

    #todo_list
    --------
    title

    #todo_item
    ------------
    list: one(#todo_list -> items)
    title
    order: int

    @order(order)






