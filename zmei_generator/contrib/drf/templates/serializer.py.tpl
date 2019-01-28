{% for extension in rest_conf.extension_serializers  %}
{% with rest_conf=extension %}
{% include 'serializer.py.tpl' %}
{% endwith %}
{% endfor %}

class {{ rest_conf.serializer_name }}Serializer(serializers.ModelSerializer):
    {% for name, declaration in rest_conf.field_declarations %}
    {{ name }} = {{ declaration }}{% endfor %}

    class Meta:
        model = {{ rest_conf.model.class_name }}
        fields = ['{{ rest_conf.field_names|join("','") }}']
        {% if rest_conf.read_only_fields %}read_only_fields = ['{{ rest_conf.read_only_fields|join("','") }}']{% endif %}

    {% if rest_conf.is_writable and rest_conf.is_root %}
    def create(self, validated_data):
        {% for extension in rest_conf.extension_serializers  %}{% if extension.is_writable %}
        {{ extension.parent_field.name }}_data = validated_data.pop('{{ extension.parent_field.name }}')
        {% endif %}{% endfor %}

        item = {{ rest_conf.model.class_name }}.objects.create(
            {% if rest_conf.user_field %}{{ rest_conf.user_field }}=self.context.get('request').user, {% endif %}**validated_data)

        {% for extension in rest_conf.extension_serializers  %}{% if extension.is_writable %}
        for data in {{ extension.parent_field.name }}_data:
            {{ extension.model.class_name }}.objects.create({{ extension.parent_field.source_field_name }}=item,{% if extension.user_field %}{{  extension.user_field }}=self.context.get('request').user, {% endif %}**data)
        {% endif %}{% endfor %}

        {{ rest_conf.on_create|indent(8) }}

        return item
    {% endif %}

    {% if col.polymorphic or rest_conf.filter_out %}
    def to_representation(self, obj):
        {% if col.polymorphic %}
        {% for child in col.child_models %}
        {% if child.rest %}
        if isinstance(obj, {{ child.class_name }}):
            return {{ child.class_name }}Serializer(obj, context=self.context).to_representation(obj)
        {% endif %}
        {% endfor %}
        {% endif %}
        {% if rest_conf.filter_out %}
        data = super().to_representation(obj)
        {{ rest_conf.filter_out|indent(8) }}
        return data
        {% else %}
        return super().to_representation(obj)
        {% endif %}
    {% endif %}


