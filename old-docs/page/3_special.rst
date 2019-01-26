Special features
##################

Global context
=================

There is a special page named "global" that you can define. All data from this page are stored in global context and will be available in all templates::

    [global]
    foo:= 123

A "global_context" function is generated - it is automatically added to the settings into the "context_processors" section.