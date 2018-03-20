@dateTree
###########

Just adds date_hierarchy filter to admin

Example:

.. code-block:: col
    :caption: admin.py

    #record
    -----------------
    title
    publish_date: create_time

    @admin
    @dateTree(publish_date)
