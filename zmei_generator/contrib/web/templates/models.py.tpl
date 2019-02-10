
{{ imports }}

{{ application.model_imports }}

from django.utils.translation import gettext_lazy as _


{% for cname, col in models %}
class {{ col.class_name }}({% for import_str, class_name, alias in col.mixin_classes %}{{ alias }}, {% endfor %}{{ col.model_class_declaration }}):
    """
    {{ col.class_name }}
    """

    {% if col.tree and col.polymorphic %}
    parent = PolymorphicTreeForeignKey('self', null=True, blank=True, related_name='children', db_index=True, on_delete=models.PROTECT)
    {% elif col.tree %}
    parent = TreeForeignKey('self', null=True, blank=True, related_name='children', db_index=True, on_delete=models.PROTECT)
    {% endif %}

    {% for field in col.own_fields_non_expr %}
    {{ field.name }} = {{ field.get_model_field().declaration }}{% endfor %}
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
        return _("{{ col.to_string }}").format(me=self)
    {% elif col.display_field  %}
    def __str__(self):
        return str(self.{{ col.display_field.name }}) or "{{ col.name }} {}".format(self.id)
    {% endif %}

    {% if col.parent or col.polymorphic %}
    @classmethod
    def get_ref(cls):
        return '{{ col.short_ref }}'
    {% endif %}

    {% if col.validators %}
    def clean(self):
        {% for validator in col.validators -%}
        def _clean():
            {{ validator|indent(24) }}
        errors = _clean()
        if errors:
            raise ValidationError(errors)
        {%- endfor %}
    {% endif %}

    class Meta:
        verbose_name = _("{{ col.name }}"){% if col.name_plural %}
        verbose_name_plural = _("{{ col.name_plural }}")
        {% endif %}
        {% if col.sortable_field %}
        ordering = {{ col.sortable_field|repr }}
        {% endif %}

{% for handlers, code in col.signal_handlers %}
{% for pkg, signal in handlers %}
@receiver({{ signal }}, sender={{ col.class_name }}){% endfor %}
def {{ col.ref }}_{{ signal }}_callback{{ loop.index }}(sender, instance, **kwargs):
    args = type('args', (object,), kwargs)
    {{ code|indent(4) }}
{% endfor %}

{% endfor %}