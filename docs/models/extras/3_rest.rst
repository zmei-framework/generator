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


Rest configuration
=======================


Authentication
-----------

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


i18n
-----------

You can enable i18n urls for @rest by adding i18n: true option.


Query
-----------

Default query can be specified with "query":


.. code-block:: col
    :caption: views.py

    #dog
    --------------
    name
    age
    alive: bool

    @rest {
        query: filter(alive=True)
    }


Serializer configuration
==========================

Fields
----------

"fields:" are list of fields that will be used by serializer.

Fields can be specified as coma separated list:

.. code-block:: col
    :caption: views.py

    #dog
    ----------
    name
    age
    height
    length
    weight

    @rest {
        fields: name, age
    }

Or *, for all fields:

.. code-block:: col
    :caption: views.py

    #dog
    ----------
    name
    age
    height
    length
    weight

    @rest {
        fields: *
    }

Some fields may be excluded:

.. code-block:: col
    :caption: views.py

    #dog
    ----------
    name
    age
    height
    length
    weight

    @rest {
        fields: *, ^length
    }

Fields may be marked as read-only. Read only has same syntax as fields:

.. code-block:: col
    :caption: views.py

    #dog
    ----------
    name
    age
    height
    length
    weight

    @rest {
        fields: *, ^length
        read_only: *, ^name
    }

User field
--------------

Sometimes it is needed to restrict user to work only with objects created
only by himself. Then "user" field may be used:

.. code-block:: col
    :caption: views.py

    #dog
    ----------
    name
    age
    owner: one(some.User)

    @rest {
        fields: * [rw]
        user_field: owner
    }

Serializer will auto-sign authenticated user to the field and will filter
entries by this user.

Inline
-----------

Serializer may include other serializers using "include":


.. code-block:: col
    :caption: views.py

    #dog
    --------------
    name
    age
    alive: bool

    @rest {
        fields: *

        inline: dogs(
            fields: *
        )
    }

    #man
    -----------
    age: int
    dogs: many(#dog -> dogs)


Also inlines may be writable, then special create method will be defined:


.. code-block:: col
    :caption: views.py

    #dog
    --------------
    name
    age
    alive: bool

    @rest {
        fields: * [rw]

        inline: owners(
            fields: * [rw]
        )
    }

    #man
    -----------
    age: int
    dogs: many(#dog -> owners)

Inlines may be nested:

.. code-block:: col
    :caption: views.py

    #dog
    --------------
    name
    age
    alive: bool

    @rest {
        fields: *

        inline: owners(
            fields: *
            inline: home_addresses(
                fields: *
            )
        )
    }

    #man
    -----------
    age: int
    dogs: many(#dog -> owners)


    #address
    --------------
    man: one(#man -> home_addresses)
    city
    street
    house


Annotate
-----------

@rest support Count() annotation on fields. Later more annotations will be added:

.. code-block:: col
    :caption: views.py

    #dog
    --------------
    name
    age
    alive: bool

    #man
    -----------
    age: int
    dogs: many(#dog -> dogs)

    @rest {
        query: filter(age__gt=50)
        annotate: count(dogs) as dog_cnt
    }

