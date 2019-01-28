@rest
#########

The @rest annotation configures django-rest-framework to expose your model api.

Basic syntax
===============

Serializer
^^^^^^^^^^^^^

To create a REST serializer for your model, just add @rest annotation::

    #boo
    ----------
    abc
    cda

    @rest

You can add as many serializers to a model as needed, adding descriptor::

    #boo
    ----------
    abc
    cda

    @rest
    @rest.another
    @rest.foo

Every @rest annotation can have different configuration.

Public api
^^^^^^^^^^^^^^^

To expose a public REST endpoint, you need @api annotation::

    #boo
    ----------
    abc
    cda

    @rest
    @api

Now you can see this on /api/ url of your application.

If you have multiple serializers, you must to specify which ones to expose::


    #boo
    ----------
    abc
    cda

    @rest
    @rest.another
    @rest.foo

    @api(_,another,foo)

Or all at once::


    #boo
    ----------
    abc
    cda

    @rest
    @rest.another
    @rest.foo

    @api(*)


Rest configuration
==========================

Field names
^^^^^^^^^^^^^^^

Specify which fields to use in serializer (:ref:`FieldList` syntax)::

    #boo
    ----------
    abc
    cda

    @rest(
        fields: *
    )


Read-only fields
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Some fields may be read-only (:ref:`FieldList` syntax)::

    #boo
    ----------
    abc
    cda
    efg

    @rest(
        fields: *
        read_only: *, ^abc
    )

I18n url
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

You can have i18n for rest (language prefix added to the urls)::

    #boo
    ----------
    abc
    cda

    @rest(
        i18n: true
    )

Permissions
^^^^^^^^^^^^^^^

You can specify is rest endpoint is read, write or both::

    #boo
    ----------
    abc
    cda

    @rest.r(
        fields: * [r]
    )
    @rest.rw(
        fields: * [rw]
    )
    @rest.w(
        fields: * [w]
    )

* r - read-only (default)
* rw - read and write
* w - write only, read not allowed

User-field
^^^^^^^^^^^^^^^

Objects may be queued/created by user::

    #boo
    ----------
    owner: one(auth.User)
    cda

    @rest(
        fields: * [rw]
        user_field: owner
    )

* Rest endpoint will show only records filtered by current user.
* Rest endpoint will assign current user for new model instances.

Query
^^^^^^^^^^^^^^^

You can adjust query of rest endpoint::

    #boo
    ----------
    abc
    cda

    @rest.yes(
        query := filter(a=123)
    )

"query" use python code one-line syntax(:ref:`PythonCode`). You can also use :ref:`Imports` to use external code in expression.


On create
^^^^^^^^^^^^^^^

You can specify a piece of code to run, after create method called (:ref:`PythonCode` syntax)::

    #boo
    ----------
    abc
    cda

    @rest(
        on_create {
            3 + 3 = 4
        }
    )

It's not the same as adding @post_save on a model, as on_create is called after all models are created
including all relations.

And one-liner::

    #boo
    ----------
    abc
    cda

    @rest(
        on_create := some()
    )

You can also use :ref:`Imports` to use external code in expression.

Inlines
^^^^^^^^^^^^^^^

Serializers can be nested as many levels as needed::

    #other
    -----------
    lala1
    lala2
    lala3

    #boo
    ----------
    abc: one(#other)
    cda

    @rest(
        inline: abc(
            fields: *, ^lala2

            // also you can add another inline here, and one more inside... but mind performance, and use prefetch_related in query
            // inline (
            //     ...
            // )
        )
    )

Annotate
-----------

@rest supports the Count() annotation on fields::

    #item
    ---------
    lala

    #boo
    ----------
    items: many(#item)

    @rest(
        annotate: count items as item_count
    )

Later more annotations will be added. For the moment, you can create annotations by setting custom query.


Authentication
-----------------

You can easily add an authentication of your choice::

    #dog
    --------------
    name
    age

    @rest(
        auth(basic, session)
    )

Or token authentication::

    #token
    ----------
    name
    user: one(cratis_profile.User)

    @mixin(rest_framework.authtoken.models.Token)


    #dog
    --------------
    name
    age

    @rest(
        auth(token: #token)
    )

Authentication options are:

basic
    `Basic http authentication <http://www.django-rest-framework.org/api-guide/authentication/#basicauthentication>`_. Not secure. Use only over SSL

session
    Allow access if user is authenticated through web. Useful for debugging REST api in browser.

token
    `Token based authentication <http://www.django-rest-framework.org/api-guide/authentication/#tokenauthentication>`_. Use only over SSL.

