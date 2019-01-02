import 'package:flutter/material.dart';
import 'package:my_app/src/app.dart';
import 'package:fluro/fluro.dart';

{% for app_name, app in apps.items() %}{% if app.flutter %}{% for name, page in app.pages.items() %}{% if page.flutter and page.uri -%}
import './pages/{{ app_name }}/{{ name }}_ui.dart';
{% endif %}{% endfor %}{% endif %}{% endfor %}

routeHandler(cls) {
    return Handler(handlerFunc: (
        BuildContext context, Map<String, List<String>> url) => cls().setUrl(url).asWidget()
    );
}

configureRoutes(Router router) {
    router.notFoundHandler = new Handler(
        handlerFunc: (BuildContext context, Map<String, List<String>> params) {

        print("ROUTE WAS NOT FOUND !!!");
    });
    {% for uri, ui_class in app_routes.items() %}
    router.define('{{ uri }}',{{ ' ' * (max_len - len(uri)) }} handler: routeHandler(()=>{{ ui_class }}()));
    {%- endfor %}
}
