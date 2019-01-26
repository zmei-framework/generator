
Polymorphic blocks with sorting
===================================

blocks.col::

    #block
    ----------
    page: one(#page -> blocks)
    title
    order: int

    @sortable(order)

    #block~>type_1
    ----------
    foo
    bar

    template: << 'content/tpl1.html';

    @admin

    #block~>type_2
    ----------
    baz

    template: << 'content/tpl2.html';

    @admin


    #page
    ----------
    title

    @admin {
        list: *
        inline: blocks(type: polymorphic)
    }