
{{ imports }}

###################
# Collection imports
###################

{{ collection_set.collection_imports }}

###################
# Model code
###################

{% for cname, col in collections %}
class {{ col.class_name }}({% for import_str, class_name, alias in col.mixin_classes %}{{ alias }}, {% endfor %}{{ col.model_class_declaration }}):
    """
    {{ col.class_name }}
    """

    {% if col.tree and col.polymorphic %}
    parent = PolymorphicTreeForeignKey('self', null=True, blank=True, related_name='children', db_index=True)
    {% elif col.tree %}
    parent = TreeForeignKey('self', null=True, blank=True, related_name='children', db_index=True)
    {% endif %}

    {% for field in col.own_fields %}{% if not field.read_only %}
    {{ field.name }} = {{ field.get_model_field(col).declaration }}{% endif %}{% endfor %}
    {% for field in col.expression_fields %}
    {% if field.static %}
    @classmethod
    def {{ field.name }}(cls):
        return {{ field.expression }}
    {% else %}
    @property
    def {{ field.name }}(self):
        return {{ field.expression }}
    {% endif %}{% endfor %}

    {% if col.to_string %}
    def __str__(self):
        return "{{ col.to_string }}".format(me=self)
    {% elif col.display_field  %}
    def __str__(self):
        return str(self.{{ col.display_field.name }}) or "{{ col.name }} {}".format(self.id)
    {% endif %}

    {% if col.parent or col.polymorphic %}
    @classmethod
    def get_ref(cls):
        return '{{ col.short_ref }}'
    {% endif %}

    class Meta:
        verbose_name = "{{ col.name }}"{% if col.name_plural %}
        verbose_name_plural = "{{ col.name_plural }}"
        {% endif %}
        {% if col.sortable_field %}
        ordering = ['{{ col.sortable_field }}']
        {% endif %}

{% endfor %}