
{% for extra in rest_conf.extra_serializers  %}
{% with rest_conf=extra %}
{% include 'serializer.py.tpl' %}
{% endwith %}
{% endfor %}

class {{ rest_conf.serializer_name }}Serializer(serializers.ModelSerializer):
    {% for name, declaration in rest_conf.field_declarations %}
    {{ name }} = {{ declaration }}{% endfor %}

    class Meta:
        model = {{ rest_conf.collection.class_name }}
        fields = ['{{ rest_conf.field_names|join("','") }}']

    {% if col.polymorphic %}
    def to_representation(self, obj):
        """
        Polymorphic serialization
        """
        {% for child in col.child_collections %}
        {% if child.rest %}
        if isinstance(obj, {{ child.class_name }}):
            return {{ child.class_name }}Serializer(obj, context=self.context).to_representation(obj)
        {% endif %}
        {% endfor %}

        return super().to_representation(obj)
    {% endif %}


