{{ imports }}

urlpatterns = ()
{% for page in collection_set.pages.values() %}
{% if page.i18n %}urlpatterns += tuple(i18n_patterns({% else %}urlpatterns += ({% endif %}
    url(r'{{ page.urls_line }}', {{ page.view_name }}.as_view(), name='{{ page.name }}'),
{% if page.i18n %})){% else %}){% endif %}
{% endfor %}
