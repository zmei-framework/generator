{{ url_imports }}

router = routers.DefaultRouter()
{% for name, model in application.models.items() %}{% if model.supports(ext) -%}
{% for rest_conf in model[ext].published_apis.values() %}
router.register(r'{{ name }}{{ rest_conf.descriptor_suffix }}', {{ rest_conf.serializer_name }}ViewSet, r'{{ name }}{{ rest_conf.descriptor_suffix }}')
{% endfor %}
{% endif %}{% endfor %}

# Wire up our API using automatic URL routing.
# Additionally, we include login URLs for the browsable API.
urlpatterns = [
    url(r'^', include(router.urls)),
]