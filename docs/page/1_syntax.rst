Page syntax
####################

Pages allow you to generate Views & and basic structure for templates.

Page header
========================

Syntax is following::

    [ page_parent->page_name : /page/url/ : template/name/that/page/will/use.html ]


Minimal page declaration
^^^^^^^^^^^^^^^^^^^^^^^^^^

Minimum that page requires to be a valid page is a name::

    [index]

Several pages declaration::

    [index]

    [hoo]


Page name
^^^^^^^^^^^^^

The name should be written in lower-case letters, can contain underscores.

Examples of model names:

- my_fancy_page
- index
- item_list

Page parent
^^^^^^^^^^^^^^^

Page can have a parent. It means it inherits variables from parent page, content blocks, and may also extend url of the parent.

See :ref:`PageParent` for details.

Page url
^^^^^^^^^^^

The page may have a url::

    [index: /]

Or a more complex url expression::

    [index: /cat/<pk>]

A url may be `"translatable" <https://docs.djangoproject.com/en/2.0/topics/i18n/translation/#django.conf.urls.i18n.i18n_patterns>`_, - it means it will get a language prefix like "/en/"::

    [index: $/cat/<pk>]

Template
^^^^^^^^^^^

Every [page] has its own template. By default, the template name will be "myapp/page_name.html".

But you can specify the template name explicitly::

    [index: /: myindex_template.html]

Another cool trick is that you can generate template names dynamically::

    [index: /some/<username>: {"user_templates/{}.html" % url.username>}]

Inside {} you can insert any python code, but one-liner is preferred, otherwise it will look ugly. (:ref:`PythonCode`).

.. note::
    If the template does not exist, it will be generated as well.


Page body
========================

Page body can contain variable declarations, python code and annotations.

Syntax::

    [page_header]

    var_name := python_code
    var_name := python_code
    var_name := python_code
    var_name := python_code
    var_name := python_code
    {
        ..page source python code ..
    }

    @annot .. annotation body ..
    @annot .. annotation body ..
    @annot .. annotation body ..
    @annot .. annotation body ..


Variables
^^^^^^^^^^^^^

Variables are values that are forwarded to page templates and all other page parts.

Syntax is following::

    [variable_name] := [line of python code] .. expression annotations ..

Line of code is a one-line python expressions (:ref:`PythonCode`). You can also use :ref:`Imports` to use external code in expression.

Each next variable can use the result of previous declarations as a local python variable::

    [index: /]
    boo:= 123
    foo:= 777 - boo

You can access the Django request object::

    [index: /]
    me:= request.user


There is a special "url" object that gives access to url parameters::

    [index: /myurl/<param1>/<param2>/<pk>]
    foo:= "Params are: {}, {}.".format(url.param1, url.param2)
    cat:= Cat.objects.get(pk=url.pk)

Variable annotations
^^^^^^^^^^^^^^^^^^^^^^

Currently only one annotation exist: @or_404
It is very useful for handling DoesNotExist exception::

    [index: /cat/<cat_id>]
    cat:= Cat.objects.get(pk=url.cat_id) @or_404

Instead of showing exception, it shows proper Http404 error to user.

Python code
^^^^^^^^^^^^^^

If you need to run custom python code, you can do it::

    [boo] {
        print("That's my code!")
    }

Or combined with variables::

    [boo]
    foo = 123
    {
        print(f"That's my code! Variables are also available here: {foo}")
    }

And you can assign new variables to "data"::

    [boo] {
        data['smth'] = '321'
    }


Annotations
^^^^^^^^^^^^^

Annotations are super-powers in Zmei generator. They add different abilities to pages, e.g. @crud generates CRUD subpages to current page::

    [cat: /cats/]
    @crud(#cat)

    #cat
    --------
    name


Read more about extensions in the :ref:`ModelExtensions` section.