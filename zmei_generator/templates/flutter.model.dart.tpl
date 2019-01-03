{% if page.functions %}
import 'dart:convert';
import 'package:http/http.dart' as http;
{% endif %}{% if page.get_parent() %}
import '../{{ page.get_parent().collection_set.app_name }}/{{ page.get_parent().name }}_ui.dart';{% else %}
import '../../state.dart';
{% endif %}
import '../../app.dart';

abstract class {{ page.view_name }}State extends {% if page.get_parent() %}{{ page.get_parent().view_name }}StateUi{% else %}PageState{% endif %} {
    {%- if page.own_item_names %}
    {% for key in (page.own_item_names) %}
    dynamic {{ to_camel_case(key) }};{% endfor %}{% endif %}
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
    {%- for key in (page.own_item_names) %}
        if (data.containsKey('{{ key }}')) {
            {{ to_camel_case(key) }} = data['{{ key }}'];
        }{% endfor %}
    }
    {%- endif %}
    {%- for name, func in page.functions.items() %}

    {{ to_camel_case(name) }}({% if func.args %}{{ func.render_python_args() }}{% endif %}) async {
        return callRemote('{{ name }}', [{% if func.args %}{{ func.render_python_args() }}{% endif %}]);
    }
    {%- endfor %}
}