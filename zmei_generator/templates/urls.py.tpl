{{ url_imports }}

urlpatterns = ({% for page in pages %}
    url(r'{{ page.urls_line }}', {{ page.view_name }}.as_view(), name='{{ package_name }}.{{ page.url_alias }}'),
{% endfor %})