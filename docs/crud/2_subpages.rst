

Subpage customisation
=============================

@crud annotation generates 4 new subpages, that are inherited from current page:

* detail
* edit
* create
* delete

Each subpage can be customised with the following syntax::

    [boo: /mycrud]
    zoo := 321

    @crud(#foo

        detail(
            lala := 123

            @markdown {
                test
            }
        )
    )

    #foo
    ------
    a

detail(... page body definition here ...) have same syntax as a page body have (see page docs).

And even sub-cruds are allowed::

    [boo: /mycrud]
    zoo := 321

    @crud(#foo

        detail(
            lala := 123

            @crud.lala(#goo)
        )
    )

    #foo
    ------
    a

    #goo
    ------
    a

And there is no limits of @curd/pages levels...

