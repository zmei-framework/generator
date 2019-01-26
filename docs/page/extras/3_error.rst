
@error(xxx)
############################

You can easily override error pages with the @error annotation::

    [not_found]
    boo: 321

    @error(404)

500 error::

    [just_error]
    boo: 123

    @error(500)
