{{ imports }}

{% for cname, col in collections %}
{% for rest_conf in col.rest_conf.values() %}
{% include 'serializer.py.tpl' %}
{% endfor %}
{% endfor %}
