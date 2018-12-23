import 'package:flutter/material.dart';
import './{{ page.name }}.dart';

class {{ app_name.capitalize() }}{{ page.view_name }}StateUi extends {{ app_name.capitalize() }}{{ page.view_name }}State {

    Widget buildBody() {
        return Center(
            child: Text('Data received: $data'),
        );
    }
}