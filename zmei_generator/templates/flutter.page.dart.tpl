import 'package:flutter/material.dart';
import '../../base.dart';


class {{ app_name.capitalize() }}{{ page.view_name }}State extends ScaffoldPageState {

    Widget buildBody() {
        return Center(
            child: Text('Data received: ${data}'),
        );
    }

    @override
    String getPageName() {
        return "{{ app_name.capitalize() }}{{ page.view_name }}";
    }
}