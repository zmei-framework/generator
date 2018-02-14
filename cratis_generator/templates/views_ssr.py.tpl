
{{ imports }}

{% for page in pages %}

class {{ page.class_name }}(CollectionTemplateView):
    template_name = '{{ page.template }}'
    {% if page.collections or page.api_calls %}
    def get_context_data(self, **kwargs):
        data = super().get_context_data(**kwargs)

        {% for c in page.collections %}
        data['{{ c.alias }}'] = self.collection_fetch('{{ c.name }}', by={{ c.by }}, page={{ c.page }}, order_by='{{ c.sorting }}', query={{ c.query }})
        {% endfor %}

        {% for c in page.api_calls %}
        data['{{ c.alias }}'] = self.api_fetch(url='{{ c.url }}', format='{{ c.format }}', by={{ c.by }}, order_by='{{ c.sorting }}', page={{ c.page }}, query={{ c.query }})
        {% endfor %}

        return data
    {% endif %}

{% endfor %}