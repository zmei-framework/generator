{{ imports }}
{{ application.page_imports }}
{% if application.channels %}
{% endif %}

from django.utils.translation import gettext_lazy as _

{% for page in pages %}
{% if page.name == 'global' %}
def global_context(request):
    return GlobalView(request=request, kwargs={}, args=[]).get_context_data()
{% endif %}
{%- for prefix, form in page.forms.items() %}
class {{ form.get_form_name() }}({{ form.get_form_class() }}):
    {{ form.get_form_code()|indent(8) }}
{% endfor -%}
class {{ page.view_name }}({% if page.get_extension_bases() %}{{ page.get_extension_bases()|join(", ") }}, {% endif %}{{ page.parent_view_name }}):
    {% if page.options %}{% for key, option in page.options.items() %}{{ key }} = {{ option }}
    {% endfor %}{% endif %}{% if page.react %}
    react_server = rs
    react_components = {{ page.react_component_names|repr }}
    {% if not page.react_server %}server_render = False{% endif %}
    {% endif %}{% if page.methods %}{% for key, method_code in page.methods.items() %}
    def {{ key }}(self, *args, **kwargs):
        {{ page.render_method_expr(method_code)|indent(8) }}
    {% endfor %}{% endif -%}
    {%- if page.has_sitemap %}
    @classmethod
    def get_sitemap(cls):
        return {{ page.sitemap_expr.render_python_code() }}
    {% endif %}
    {{ page.render_template_name_expr()|indent(4) }}
    {% for name, func in page.functions.items() %}
    def {{ func.python_name }}(self, url, request{% if func.args %}, {{ func.render_python_args() }}{% endif %}):
        {% if func.has_data_arg %}data = self._get_data()
        {% for arg in func.get_data_args() %}
        {{ arg }} = data.get('{{ arg }}'){% endfor %}
        {% endif %}
        {% if func.body -%}
        {{ func.body|indent(8) }}
        {%- else -%}
        return {{ func.name }}({% if func.out_args %}{{ func.render_python_args(out=True) }}{% endif %})
        {%- endif %}
    {% endfor %}
    {% set code=page.render_page_code() %}{% if code or page.page_item_names %}
    def get_data(self, url, request, inherited=False):
        {%- if page.parent_name %}
        data = super().get_data(url, request, inherited)
        {% else %}
        data = Data()
        {% endif %}
        {% if code %}{{ code|indent(8) }}{% endif %}
        {%- if page.page_item_names %}
        data.update({ {% for key in (page.page_item_names) %}'{{ key }}': {{ key }}{% if not loop.last %}, {% endif %}{% endfor %} })
        {% endif %}
        return data
    {% endif %}

    {% if page.allow_post %}
    post = {{ page.parent_view_name }}.get
    {% endif %}


{% if page.handlers %}
from django.conf import urls
{% for handler_code in page.handlers %}
from django.conf.urls import handler{{ handler_code }}
handler_{{ handler_code }}_view = {{ page.view_name }}.as_view()
setattr(urls, 'handler{{ handler_code }}', '{{ application.app_name }}.views.handler_{{ handler_code }}_view')
{% endfor %}
{% endif %}

{% endfor %}