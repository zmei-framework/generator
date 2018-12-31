import '../../state.dart';
{% if page.functions %}
import 'dart:convert';
import 'package:http/http.dart' as http;
{% endif %}{% if page.get_parent() %}
import '../{{ page.get_parent().collection_set.app_name }}/{{ page.get_parent().name }}.dart';
{% endif %}
abstract class {{ page.view_name }}State extends {% if page.get_parent() %}{{ page.get_parent().view_name }}StateUi{% else %}PageState{% endif %} {
    {%- if page.own_item_names %}
    {% for key in (page.own_item_names) %}
    dynamic {{ to_camel_case(key) }};{% endfor %}{% endif %}

    {% if page.own_item_names or page.stream or page.functions %}
    @override
    void initState() {
        super.initState();

        reload();

        {% if page.own_item_names -%}
        hasRemoteData = true;
        {%- endif %}{% if page.stream -%}
        hasStreams = true;
        listenStream();
        {%- endif %}
    }
    {% endif %}

    {%- if page.own_item_names %}

    void loadData(data) {
        super.loadData(data);
    {%- for key in (page.own_item_names) %}
        {{ to_camel_case(key) }} = data['{{ key }}'];{% endfor %}
    }
    {%- endif %}
    {%- for name, func in page.functions.items() %}

    {{ to_camel_case(name) }}({% if func.args %}{{ func.render_python_args() }}{% endif %}) async {
        return callRemote('{{ name }}', [{% if func.args %}{{ func.render_python_args() }}{% endif %}]);
    }
    {%- endfor %}
}