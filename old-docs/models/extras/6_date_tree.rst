@date_tree
###########

Just adds a date_hierarchy filter to admin::

    #record
    -----------------
    title
    publish_date: create_time

    @admin
    @date_tree(publish_date)
