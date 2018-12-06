{{ imports }}
{{ collection_set.page_imports }}
{% if collection_set.channels %}
channel_layer = get_channel_layer()
{% endif %}

from django.utils.translation import gettext_lazy as _

{% for cname, col in collections %}
{% for rest_conf in col.published_apis.values() %}

{% if rest_conf.auth_methods.token %}
class {{ col.class_name }}TokenAuthentication(TokenAuthentication):
    model = {{ rest_conf.auth_methods.token.model }}
{% endif %}

class {{ rest_conf.serializer_name }}ViewSet({{ rest_conf.rest_class[1] }}):
    """
    {{ col.class_name }} API
    """

    filter_fields = ['{{ rest_conf.field_names|join("','") }}']
    serializer_class = {{ rest_conf.serializer_name }}Serializer
    {% if rest_conf.auth_methods %}
    permission_classes = [IsAuthenticated]
    authentication_classes = [{{ rest_conf.auth_method_classes|join(', ') }}]
    {% endif %}

    def get_queryset(self):
        return {{ col.class_name }}.objects.{{ rest_conf.query }}{% if rest_conf.user_field %}.filter({{ rest_conf.user_field }}=self.request.user){% endif %}{% if rest_conf.annotations %}.annotate({{ rest_conf.annotations|join(", ") }}){% endif %}
{% endfor %}
{% endfor %}
{%- if collection_set.react %}
rs = ZmeiReactServer()
rs.load(settings.BASE_DIR + '/app/static/react/{{ collection_set.app_name }}.bundle.js')
{% endif -%}
{% for page in pages %}
class {{ page.view_name }}({% if page.get_extra_bases() %}{{ page.get_extra_bases()|join(", ") }}, {% endif %}{{ page.parent_view_name }}):
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
    {%- if page.crud_views %}
    def get_crud_views(self):
        return ({% for cls in page.crud_views.values() %}
            {{ cls }},{% endfor %}
        )
    {% endif %}
    {{ page.render_template_name_expr()|indent(4) }}
    {% for name, func in page.functions.items() %}
    def {{ func.python_name }}(self, url, request{% if func.args %}, {{ func.render_python_args() }}{% endif %}):
        {{ func.body|indent(8) }}
    {% endfor %}
    {% set code=page.render_page_code() %}{% if code or page.page_item_names %}
    def get_data(self, url, request, inherited):
        {%- if page.parent_name %}
        data = super().get_data(url, request, inherited)
        {% else %}
        data = {}
        {% endif %}
        {%- if code %}{{ code|indent(8) }}{% endif %}
        {%- if page.page_item_names %}
        data.update({ {% for key in (page.page_item_names) %}'{{ key }}': {{ key }}{% if not loop.last %}, {% endif %}{% endfor %} })
        {% endif %}
        return data
    {% endif %}

    {% if page.allow_post %}
    post = {{ page.parent_view_name }}.get
    {% endif %}
{% if page.name == 'global' %}
def global_context(request):
    return GlobalView(request=request, kwargs={}, args=[]).get_context_data()
{% endif %}

{% if page.stream %}
class {{ page.view_name }}Consumer(AsyncWebsocketConsumer):
    async def connect(self):
        await self.channel_layer.group_add('page_{{ page.name }}', self.channel_name)
        await self.accept()

    async def disconnect(self, close_code):
        await self.channel_layer.group_discard('page_{{ page.name }}', self.channel_name)

    async def state_update(self, event):
        await self.send(text_data=ZmeiReactJsonEncoder(view=self.scope['url_route']).encode(event['message']))

{% for item in page.page_items.values() %}
@receiver(post_save, sender={{ item.stream_model }})
def counter_post_save_callback(sender, instance, **kwargs):
    async_to_sync(channel_layer.group_send)("page_{{ page.name }}", {
        "type": "state_update",
        "message": {
            '__state__': {
                '{{ item.key }}': {{ item.render_python_code() }}
            }
        }
    })
{% endfor %}
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