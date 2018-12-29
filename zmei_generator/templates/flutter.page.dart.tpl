import 'package:flutter/material.dart';
import '../../state.dart';
{% if page.functions %}
import 'dart:convert';
import 'package:http/http.dart' as http;
{% endif %}
abstract class {{ app_name.capitalize() }}{{ page.view_name }}State extends PageState {
    {%- if page.own_item_names %}
    {% for key in (page.own_item_names) %}
    dynamic {{ key }};{% endfor %}{% endif %}

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
        {{ key }} = data['{{ key }}'];{% endfor %}
    }
    {%- endif %}
    {%- for name, func in page.functions.items() %}

    {{ to_camel_case(name) }}({% if func.args %}{{ func.render_python_args() }}{% endif %}) async {
        return callRemote('{{ name }}', [{% if func.args %}{{ func.render_python_args() }}{% endif %}]);
    }
    {%- endfor %}
}