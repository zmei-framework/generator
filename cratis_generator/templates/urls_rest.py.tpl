{{ url_imports }}

router = routers.DefaultRouter()
{% for name, collection in collection_set.collections.items() %}{% if collection.rest -%}
router.register(r'{{ name }}', {{ collection.class_name }}ViewSet, r'{{ name }}')
{% endif %}{% endfor %}

# Wire up our API using automatic URL routing.
# Additionally, we include login URLs for the browsable API.
urlpatterns = [
    url(r'^', include(router.urls)),

]