
{{ imports }}

{% for cname, col in models %}
class {{ col.class_name }}TranslationOptions(TranslationOptions):
    """
    {{ col.class_name }} TranslationOptions
    """
    {% if col.translatable_fields %}
    fields = [{{ col.translatable_fields|field_names }}]
    {% else %}
    pass
    {% endif %}

translator.register({{ col.class_name }}, {{ col.class_name }}TranslationOptions)
{% endfor %}