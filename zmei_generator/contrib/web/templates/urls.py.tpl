{{ url_imports }}
{% if i18n %}
from django.utils.translation import gettext_lazy as _

urlpatterns = ({% for page in pages %}
    url(_(r'{{ page.urls_line }}'), {{ page.view_name }}.as_view(), name='{{ package_name }}.{{ page.url_alias }}'),
{% endfor %})
{% else %}
urlpatterns = ({% for page in pages %}
    url(r'{{ page.urls_line }}', {{ page.view_name }}.as_view(), name='{{ package_name }}.{{ page.url_alias }}'),
{% endfor %})
{% endif %}