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
class {{ page.view_name }}({{ page.parent_view_name }}):
    {% if page.has_sitemap %}
    @classmethod
    def get_sitemap(cls):
        return {{ page.sitemap_expr.render_python_code() }}
    {% endif %}
    def get_context_data(self, **kwargs):
        data = super().get_context_data(**kwargs)
        request = self.request
        parent = type('parent', (object,), data)
        url = type('url', (object,), self.kwargs)

        {% for key, item in page.page_items.items() %}{% if not item.or_404 %}
        {{ key }} = {{ item.render_python_code() }}{% else %}
        try:
            {{ key }} = {{ item.render_python_code() }}
        except ObjectDoesNotExist:
            raise Http404
        {% endif %}{% endfor %}

        self.template_name = {{ page.template_name_expr }}

        data.update({ {% for key in (page.page_item_names + ['url']) %}'{{ key }}': {{ key }}{% if not loop.last %}, {% endif %}{% endfor %} })
        return data
    {% if page.allow_post %}
    post = {{ page.parent_view_name }}.get
    {% endif %}
{% if page.name == 'global' %}
def global_context(request):
    return GlobalView(request=request, kwargs={}, args=[]).get_context_data()
{% endif %}

{% endfor %}