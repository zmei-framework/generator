{{ imports }}
{{ collection_set.page_imports }}

if '_' not in locals():
    _ = lambda s: s

{% for cname, col in collections %}
{% with rest_conf=col.rest_conf %}
{% include 'serializer.py.tpl' %}
{% endwith %}

{% if col.rest_conf.auth_methods.token %}
class {{ col.class_name }}TokenAuthentication(TokenAuthentication):
    model = {{ col.rest_conf.auth_methods.token.model }}
{% endif %}

class {{ col.class_name }}ViewSet({{ col.rest_conf.rest_class[1] }}):
    """
    {{ col.class_name }} API
    """

    filter_fields = ['{{ col.rest_conf.field_names|join("','") }}']
    serializer_class = {{ col.class_name }}Serializer
    permission_classes = [{% if col.rest_conf.auth_methods %}IsAuthenticated{% else %}AllowAny{% endif %}]
    authentication_classes = [{{ col.rest_conf.auth_method_classes|join(', ') }}]

    def get_queryset(self):
        return {{ col.class_name }}.objects.{{ col.rest_conf.query }}{% if col.rest_conf.user_field %}.filter({{ col.rest_conf.user_field }}=self.request.user){% endif %}{% if col.rest_conf.annotations %}.annotate({{ col.rest_conf.annotations|join(", ") }}){% endif %}
{% endfor %}

def cached(func, suffix='data'):
    def _wrap(self, *args, **kwargs):
        if hasattr(self, '_' + suffix):
            return getattr(self, '_' + suffix)
        data = func(self, *args, **kwargs)
        setattr(self, '_' + suffix, data)
        return data
    return _wrap

class _Data(object):
    def __init__(self, data=None):
        self.__dict__.update(data or {})

    def __add__(self, data):
        return _Data({**self.__dict__, **data})


class _View(object):
    def get_data(self, inherited):
        return _Data()

    def get_context_data(self, **kwargs):
        data = super().get_context_data(**self.kwargs)
        return {**data, **self.get_data().__dict__}

{% for page in pages %}
{% if page.is_login_required() %}@method_decorator(login_required, name='dispatch'){% endif %}
class {{ page.view_name }}({% if page.extra_bases %}{{ page.extra_bases|join(", ") }}, {% endif %}{{ page.parent_view_name }}):
    {% if page.options %}{% for key, option in page.options.items() %}{{ key }} = {{ option }}
    {% endfor %}{% endif %}{% if page.methods %}{% for key, method_code in page.methods.items() %}
    def {{ key }}(self, *args, **kwargs):
        {{ page.render_method_expr(method_code)|indent(8) }}
    {% endfor %}{% endif %}
    {% if page.has_sitemap %}
    @classmethod
    def get_sitemap(cls):
        return {{ page.sitemap_expr.render_python_code() }}
    {% endif %}
    def get_template_names(self):
        {{ page.render_template_name_expr()|indent(8) }}

    {% set code=page.render_page_code() %}{% if code or page.page_item_names %}
    @cached
    def get_data(self, inherited=False):
        data = super().get_data(inherited=True)
        {{ code|indent(8) }}
        {% if page.page_item_names %}
        return data + { {% for key in (page.page_item_names) %}'{{ key }}': {{ key }}{% if not loop.last %}, {% endif %}{% endfor %} }
        {% else %}
        return data
        {% endif %}
    {% endif %}

    {% if page.allow_post %}
    post = {{ page.parent_view_name }}.get
    {% endif %}
{% if page.name == 'global' %}
def global_context(request):
    return GlobalView(request=request, kwargs={}, args=[]).get_context_data()
{% endif %}

{% if page.handlers %}
from django.conf import urls
{% for handler_code in page.handlers %}
from django.conf.urls import handler{{ handler_code }}
handler_{{ handler_code }}_view = {{ page.view_name }}.as_view()
setattr(urls, 'handler{{ handler_code }}', '{{ collection_set.app_name }}.views.handler_{{ handler_code }}_view')
{% endfor %}
{% endif %}

{% endfor %}