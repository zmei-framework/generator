import 'package:flutter/material.dart';
import './{{ page.name }}.dart';
import './../../app.dart';


{% if not page.uri %}abstract {% endif %}class {{ page.view_name }}StateUi extends {{ page.view_name }}State {
    {% if page.uri %}
    Widget buildBody(BuildContext context) {
        return Center(
            child: Text('{{ page.collection_set.app_name }}.{{ page.name }}: Nothing here!'),
        );
    }
    {% endif %}
}