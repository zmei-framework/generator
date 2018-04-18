from cratis.features import Feature, require
{% if collection_set.admin %}
from cratis_admin.features import AdminArea
{% endif %}

{#{% if collection_set.rest %}#}
{#from cratis_api.features import RestApi#}
{#{% endif %}#}

{% if collection_set.admin or collection_set.rest %}
@require({% if collection_set.admin %}
    AdminArea(),{% endif %}
{#    {% if collection_set.rest %}#}
{#    RestApi(),{% endif %}#}
){% endif %}
class {{ feature_name }}(Feature):

    def init(self):
        self.append_apps({{ collection_set.apps|repr }})

        {% if collection_set.admin %}
        with self.use(AdminArea) as admin:
            admin.add_menu({'label': '{{ package_name }}', 'models': ({% for name, collection in collection_set.collections.items() %}{% if not collection.parent %}
                '{{ package_name }}.{{ collection.class_name }}',{% endif %}{% endfor %}
            )})
        {% endif %}

{#        {% if collection_set.rest %}#}
{#        with self.use(RestApi) as api:#}
{#            {% for name, collection in collection_set.collections.items() %}{% if collection.rest %}#}
{#            api.routes.append(#}
{#                (r'{{ package_name }}/{{ name }}', '{{ package_name }}.views.{{ collection.class_name }}ViewSet', "{{ name }}")#}
{#            )#}
{#            {% endif %}{% endfor %}#}
{#        {% endif %}#}

        {% if 'global' in collection_set.pages %}
        self.append_template_processor(
            ('{{ package_name }}.views.global_context', )
        )
        {% endif %}

    {% if collection_set.has_sitemap %}
    def sitemaps(self):
        sitemap_data = { {% for page in collection_set.pages.values() %}{% if page.has_sitemap %}
            '{{ package_name }}.{{ page.name }}': {{ page.view_name }}.get_sitemap(),{% endif %}{% endfor %}
        }

        return sitemap_data

    {% endif %}

    {% if pages_i18n or pages %}
    def configure_urls(self, urls):
        from django.conf.urls import url, include
        {% if pages_i18n -%}
        from django.conf.urls.i18n import i18n_patterns
        urls += tuple(i18n_patterns(
            url(r'^', include('{{ collection_set.app_name }}.urls_i18n')),
        ))
        {% endif %}
        {% if collection_set.rest %}
        urls += tuple(i18n_patterns(
            url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework')),
            url(r'^api/{{ collection_set.app_name }}/', include('{{ collection_set.app_name }}.urls_rest')),
        ))
        {% endif %}

        {% if pages %}
        urls += (
            url(r'^', include('{{ collection_set.app_name }}.urls')),
        )
        {% endif %}
    {% endif %}

    {% if collection_set.deps %}
    def get_deps(self):
        return {{ collection_set.deps|repr }}
    {% endif %}