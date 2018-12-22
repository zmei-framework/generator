import 'package:flutter/material.dart';
{% for app_name, app in apps.items() %}{% if app.flutter %}{% for name, page in app.pages.items() %}{% if page.flutter -%}
import './pages/{{ app_name }}/{{ name }}.dart';
{% endif %}{% endfor %}{% endif %}{% endfor %}

void routes(String baseUrl) {
    runApp(MaterialApp(
        title: 'Named Routes Demo',
        initialRoute: '/',

        theme: ThemeData(
            primarySwatch: Colors.purple,
        ),

        routes: {
            {%- for app_name, app in apps.items() %}{% if app.flutter %}{% for name, page in app.pages.items() %}{% if page.flutter %}
            '{{ page.uri }}': (context) => {{ app_name.capitalize() }}{{ page.view_name }}State().setUrl(baseUrl + '{{ page.uri }}').asWidget(),
            {%- endif %}{% endfor %}{% endif %}{% endfor %}
        },
    ));
}
