import 'package:flutter/material.dart';
import './../../base.dart';
import './{{ page.name }}.dart';

class {{ page.view_name }}StateUi extends {{ page.view_name }}State with ScaffoldPageStateMixin {

    Widget buildBody(BuildContext context) {
        return Center(
            child: Text('Data received: $data'),
        );
    }

    @override
    String getPageName() {
        return "{{ app_name.capitalize() }}{{ page.view_name }}";
    }
}