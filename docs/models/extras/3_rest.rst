@rest
#########

@rest extra is simple way to add rest api to your models.

Empty @rest extra, will add read only api for your model:

.. code-block:: col
    :caption: views.py

    #dog
    --------------
    name
    age

    @rest

By default, all fields are published.

Syntax
===========

@rest extra structure is following::

    @rest {
        /* rest configuration */

        auth(basic, session, token: #token)
        i18n: true/false
        query: .all()
        on_create: one_line_of_python_code_here()

        /* recursive serializer configuration */

        fields: *, name [rw]
        read_only: name
        user_field: user
        annotate: count books as books_cnt

        inline:
            one_inline_field(

                /* recursive serializer configuration */

                fields: *, name [rw]
                read_only: name
                user_field: user
                annotate: count books as books_cnt
            ),
            another_field(
                fields: *
                user_field: user

                inline: files(
                    fields: *
                    user_field: user
                )
            )
    }

Example
-----------

Full example (use "open in new tab" button to see full code):

.. code-block:: col
    :caption: views.py

    #token
    ----------
    name
    user: one(cratis_profile.User)

    @mixin(rest_framework.authtoken.models.Token)


    #request
    --------------
    =name
    date_created: create_time
    user: one(cratis_profile.User)
    collections: text(255)

    @rest {
        auth(token: #token, session)
        on_create: do_generate(item)

        fields: * [rw]
        read_only: response

        user_field: user

        inline:
            files(
                fields: * [rw]
                user_field: user
            ),
            response(
                fields: *
                user_field: user

                inline: files(
                    fields: *
                    user_field: user
                )
            )
    }


    #request_file
    -----------------
    request: one(#request -> files)
    user: one(cratis_profile.User)
    =name: text(255)
    body: longtext


    #response
    --------------
    request: one2one(#request -> response)
    date_created: create_time
    user: one(cratis_profile.User)


    #response_file
    -----------------
    response: one(#response -> files)
    user: one(cratis_profile.User)
    =name: text(255)
    body: longtext





Authentication
===================

You can add authentication of your choice easily:

.. code-block:: col
    :caption: views.py

    #dog
    --------------
    name
    age

    @rest {
        auth(basic, session)
    }

Or token authentication:

.. code-block:: col
    :caption: views.py

    #token
    ----------
    name
    user: one(cratis_profile.User)

    @mixin(rest_framework.authtoken.models.Token)


    #dog
    --------------
    name
    age

    @rest {
        auth(token: #token)
    }

Authentication options are:

basic
    `Basic http authentication <http://www.django-rest-framework.org/api-guide/authentication/#basicauthentication>`_. Not secure. Use only over SSL

session
    Allow access if user is authenticated through web. Useful for debugging REST api in browser.

token
    `Token based authentication <http://www.django-rest-framework.org/api-guide/authentication/#tokenauthentication>`_. Use only over SSL.



