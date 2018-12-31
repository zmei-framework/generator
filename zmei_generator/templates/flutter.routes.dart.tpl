import 'package:flutter/material.dart';
import 'package:my_app/src/app.dart';
{% for app_name, app in apps.items() %}{% if app.flutter %}{% for name, page in app.pages.items() %}{% if page.flutter and page.uri -%}
import './pages/{{ app_name }}/{{ name }}_ui.dart';
{% endif %}{% endfor %}{% endif %}{% endfor %}

void routes() {
    runApp(buildApp({
        {%- for app_name, app in apps.items() %}{% if app.flutter %}{% for name, page in app.pages.items() %}{% if page.flutter and page.uri %}
        '{{ page.uri }}': (context) => {{ page.view_name }}StateUi().asWidget(),
        {%- endif %}{% endfor %}{% endif %}{% endfor %}
    }));
}