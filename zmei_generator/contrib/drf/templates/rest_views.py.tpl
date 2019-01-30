{{ imports }}

{% for model_name, model in models %}
{% for rest_conf in model[ext].published_apis.values() %}

{% if rest_conf.auth_methods.token %}
class {{ model.class_name }}TokenAuthentication(TokenAuthentication):
    model = {{ rest_conf.auth_methods.token.model }}
{% endif %}

class {{ rest_conf.serializer_name }}ViewSet({{ rest_conf.rest_class[1] }}):
    """
    {{ model.class_name }} API
    """

    filter_fields = ['{{ rest_conf.field_names|join("','") }}']
    serializer_class = {{ rest_conf.serializer_name }}Serializer
    {% if rest_conf.auth_methods %}
    permission_classes = [IsAuthenticated]
    authentication_classes = [{{ rest_conf.auth_method_classes|join(', ') }}]
    {% endif %}

    def get_queryset(self):
        return {{ model.class_name }}.objects.{{ rest_conf.query }}{% if rest_conf.user_field %}.filter({{ rest_conf.user_field }}=self.request.user){% endif %}{% if rest_conf.annotations %}.annotate({{ rest_conf.annotations|join(", ") }}){% endif %}
{% endfor %}
{% endfor %}