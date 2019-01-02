import 'package:flutter/material.dart';
import 'package:my_app/src/app.dart';
import 'package:fluro/fluro.dart';

{% for app_name, app in apps.items() %}{% if app.flutter %}{% for name, page in app.pages.items() %}{% if page.flutter and page.uri -%}
import './pages/{{ app_name }}/{{ name }}_ui.dart';
{% endif %}{% endfor %}{% endif %}{% endfor %}

routeHandler(cls) {
    return Handler(handlerFunc: (
        BuildContext context, Map<String, List<String>> url) => cls().setUrl(url.map((key, val) => MapEntry(key, val[0]))).asWidget()
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


{% for app_name, app in apps.items() %}{% if app.flutter %}
class Routes{{ to_camel_case_classname(app_name) }} {
    {% for name, page in app.pages.items() %}{% if page.flutter and page.uri -%}
    String {{ to_camel_case(name) }}({% if page.uri_params %}{ {% for param in page.uri_params %}{{ to_camel_case(param) }}{% if not loop.last %}, {% endif %}{% endfor %} }{% endif %}) {
        return '{{ format_uri(page.uri) }}'{% for param in page.uri_params %}.replaceAll(':{{ param }}', {{ to_camel_case(param) }}.toString()){% endfor %};
    }
    {% endif %}{% endfor %}
}
{% endif %}{% endfor %}

class Routes { {% for app_name, app in apps.items() %}{% if app.flutter %}
    final {{ to_camel_case(app_name) }} = Routes{{ to_camel_case_classname(app_name) }}();{% endif %}{% endfor %}
}
