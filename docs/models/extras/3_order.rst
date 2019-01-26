
@sortable
#####################

The @sortable mixin does two things:

1.	It adds a list sorting to the admin list and inlines 
2.	It configures the model so that it could be sorted out by order field

You are responsible for adding order field::

    #todo_item
    ------------
    title
    order: int

    @sortable(order)
    @admin


There is also an @order annotation that does the same, but does not add anything to admin::

    #todo_item
    ------------
    title
    order: int

    @order(order)






