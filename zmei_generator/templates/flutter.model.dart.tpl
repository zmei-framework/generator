{% for import in imports %}import './{{ import }}.dart';
{% endfor %}
_(t) => t;  // mock translations

{% for cname, col in collection_set.collections.items() %}
class {{ col.class_name }} {

    {{ col.class_name }}({ {% for field in col.fields.values() %}
        this.{{ to_camel_case(field.name) }}{% if not loop.last %}, {% endif %}{% endfor %}
    });

    int id;

    // Model fields
    {% for field in col.fields.values() %}
    {{ field.get_flutter_field() }} {{ to_camel_case(field.name) }};
    {% endfor %}
    {% for field in col.expression_fields %}
    dynamic {{ to_camel_case(field.name) }};{% endfor %}
    {% if col.display_field  -%}
    String toString() {
        return "${{ col.display_field.name }}";
    }
    {% endif %}
    {%- if col.parent or col.polymorphic %}
    String getRef() {
        return '{{ col.short_ref }}';
    }
    {% endif %}
    String getVerboseName() {
        return _("{{ col.name }}");
    }

    String getVerboseNamePlural() {
        return {% if col.name_plural %}_("{{ col.name_plural }}"){% else %}_("{{ col.name }}s"){% endif %};
    }

    {{ col.class_name }}.fromJson(Map<String, dynamic> data) {
        if (data['id'] != null) {
            id = data['id'];
        }
        {% for name, field in col.fields.items() %}if (data['{{ name }}'] != null) {
            {{ to_camel_case(name) }} = {{ field.get_flutter_from_json(name) }};
        }{% if not loop.last %}
        {% endif %}{% endfor %}
    }
}{% endfor %}
