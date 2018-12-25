import 'package:flutter/material.dart';
import 'package:my_app/src/app.dart';
{% for app_name, app in apps.items() %}{% if app.flutter %}{% for name, page in app.pages.items() %}{% if page.flutter -%}
import './pages/{{ app_name }}/{{ name }}_ui.dart';
{% endif %}{% endfor %}{% endif %}{% endfor %}

void routes(String baseUrl) {
    runApp(buildApp({
        {%- for app_name, app in apps.items() %}{% if app.flutter %}{% for name, page in app.pages.items() %}{% if page.flutter %}
        '{{ page.uri }}': (context) => {{ app_name.capitalize() }}{{ page.view_name }}StateUi()
        {%- if page.own_item_names or page.functions %}.setDataUrl(baseUrl + '{{ page.uri }}'){% endif -%}
        {%- if page.stream %}.setWsUrl(baseUrl + '/ws/pages{{ page.uri }}'){% endif -%}
        .asWidget(),
        {%- endif %}{% endfor %}{% endif %}{% endfor %}
    }));
}