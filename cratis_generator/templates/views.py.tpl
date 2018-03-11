{{ imports }}
{% for cname, col in collections %}
{% with rest_conf=col.rest_conf %}
{% include 'serializer.py.tpl' %}
{% endwith %}

class {{ col.class_name }}ViewSet({{ col.rest_class[1] }}):
    """
    {{ col.class_name }} API
    """

    filter_backends = (AnyFilterBackend,)
    filter_fields = ['{{ col.rest_conf.field_names|join("','") }}']
    queryset = {{ col.class_name }}.objects.all(){% if col.rest_conf.annotations %}.annotate({{ col.rest_conf.annotations|join(", ") }}){% endif %}
    serializer_class = {{ col.class_name }}Serializer
    pagination_class = Pagination
    permission_classes = [AllowAny]

{% endfor %}
{{ collection_set.page_imports }}
{% for page in pages %}
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

    {% set code=page.render_page_code() %}{% if code %}
    def get_context_data(self, **kwargs):
        data = super().get_context_data(**self.kwargs)
        {{ code|indent(8) }}
        {% if page.page_item_names %}
        return {**data, **{ {% for key in (page.page_item_names) %}'{{ key }}': {{ key }}{% if not loop.last %}, {% endif %}{% endfor %} } }
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