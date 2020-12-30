{{ url_imports }}
from django.conf import settings
from django.conf.urls.static import static
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


if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)