import 'package:flutter/material.dart';
import '../../base.dart';


class {{ app_name.capitalize() }}{{ page.view_name }}State extends ScaffoldPageState {
    {%- if page.own_item_names %}
    {% for key in (page.own_item_names) %}
    dynamic {{ key }};{% endfor %}{% endif %}

    {{ app_name.capitalize() }}{{ page.view_name }}State() : super({% if page.own_item_names %}true{% else %}false{% endif %});

    {%- if page.own_item_names %}

    void loadData(data) {
    {%- for key in (page.own_item_names) %}
        {{ key }} = data['{{ key }}'];{% endfor %}
    }
    {%- endif %}

    Widget buildBody() {
        return Center(
            child: Text('Data received: $data'),
        );
    }

    @override
    String getPageName() {
        return "{{ app_name.capitalize() }}{{ page.view_name }}";
    }
}