{% if page.cruds %}
import 'package:flutter/material.dart';
{% endif %}{% if page.functions %}
import 'dart:convert';
import 'package:http/http.dart' as http;
{% endif %}{% if page.get_parent() %}
import '../{{ page.get_parent().collection_set.app_name }}/{{ page.get_parent().name }}_ui.dart';{% else %}
import '../../state.dart';
{% endif %}
import '../../app.dart';{% for import in imports %}import './../../models/{{ import }}.dart';
{% endfor %}

abstract class {{ page.view_name }}State extends {% if page.get_parent() %}{{ page.get_parent().view_name }}StateUi{% else %}PageState{% endif %} {

    {% if page.own_item_names %}
    {%- for key, (item, collection) in page_items.items() -%}
    {% if not collection %}dynamic {{ to_camel_case(key) }};
    {% elif item.collection_many %}List<{{ collection.class_name }}> {{ to_camel_case(key) }};
    {% elif item.collection_dict %}Map<String, {{ collection.class_name }}> {{ to_camel_case(key) }};
    {% else %}{{ collection.class_name }} {{ to_camel_case(key) }};
    {% endif %}
    {%- endfor %}
    {%- endif %}
    {% if page.uri %}
    @override
    String getPageUrl() {
        return App.url.{{ to_camel_case(page.collection_set.app_name) }}.{{ to_camel_case(page.name) }}({% for param in page.uri_params %}{{ to_camel_case(param) }}: url['{{ param }}']{% if not loop.last %}, {% endif %}{% endfor %});
    }
    {% if page.has_data %}
    @override
    bool hasRemoteData() {
        return true;
    }
    {% endif %}
    {% endif %}
    {% if page.stream %}
    @override
    void initState() {
        subscribeStream('/ws/pages/{{ page.collection_set.app_name }}/{{ page.name }}');
        super.initState();
    }

    @override
    void dispose() {
        unsubscribeStream('/ws/pages/{{ page.collection_set.app_name }}/{{ page.name }}');
        super.dispose();
    }
    {% endif %}
    {%- if page.own_item_names %}
    void loadData(data) {
        super.loadData(data);
        {%- for key, (item, collection) in page_items.items() %}
        if (data['{{ key }}'] != null) {
            {% if not collection %}{{ to_camel_case(key) }} = data['{{ key }}'];
            {% elif item.collection_many %}{{ to_camel_case(key) }} = data['{{ key }}'].map<{{ collection.class_name }}>((item) => {{ collection.class_name }}.fromJson(item)).toList();
            {% elif item.collection_dict %}{{ to_camel_case(key) }} = data['{{ key }}'].map<String, {{ collection.class_name }}>((key, item) => MapEntry(key, {{ collection.class_name }}.fromJson(item)));
            {% else %}{{ to_camel_case(key) }} = {{ collection.class_name }}.fromJson(data['{{ key }}']);
            {% endif %}
        }{% endfor %}
    }
    {%- endif %}
    {%- for name, func in page.functions.items() %}

    {{ to_camel_case(name) }}({% if func.args %}{{ func.render_python_args() }}{% endif %}) async {
        return callRemote('{{ name }}', [{% if func.args %}{{ func.render_python_args() }}{% endif %}]);
    }
    {% endfor %}
    // {{ page.cruds }}
    {%- for descriptor, crud_list in page.cruds.items() %}{%- for type, crud in crud_list.items() %}
    Widget build{{ to_camel_case_classname(descriptor) }}{{ to_camel_case_classname(type) }}Ui(BuildContext context) {
        {% if type == 'crud' %}

            return Text('List');

        {% elif type == 'crud_create' %}

            return Text('Create');

        {% elif type == 'crud_delete' %}

            return Text('Delete');

        {% elif type == 'crud_detail' %}

            return Text('Detail');

        {% elif type == 'crud_edit' %}

            return Text('Edit');

        {% endif %}
    }{% endfor %}{% endfor %}
}