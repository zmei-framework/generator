Overview
####################

The Pages feature is powerful way to automat all common patterns with
web-application view-controller layer (templates & Views in Django terminology).

Minimal page structure
========================

Example of minimal page (test.col file)::

    [index: /]

"index" is a page's "ref" (Reference). And "/" is an url pattern.

Result of generation is Django view::

    from django.views.generic import TemplateView

    class IndexView(TemplateView):

        def get_template_names(self):
            return ["test/index.html"]

        def get_context_data(self, inherited=False, **kwargs):
            data = super().get_context_data(inherited=True, **self.kwargs)
            url = type('url', (object,), self.kwargs)

            return {**data, **{'url': url}}

Template context is generated initially empty, but with boilerplate code, so you can
write in your own code here. only *url* helper is injected.

Genius automatically assumes template name by combining application name and view name.
Template html looks like this::

    {# generated #}
    {% extends 'base.html' %}

.. note::
    "{# generated #}" marker is used by Genius to determine if file has been changed by hands or not.
    If file has no this marker, then generator thinks it's file written by hands, and never overwrite it.

Template name can be specified explicitly::

    [index: /: somedir/somefile.html]

