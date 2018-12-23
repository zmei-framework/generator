import 'package:flutter/material.dart';
import './state.dart';

abstract class ScaffoldPageState extends PageState {

    ScaffoldPageState(bool hasRemoteData) : super(hasRemoteData);

    @override
    Widget build(BuildContext context) {
        return Scaffold(
            appBar: AppBar(
                title: Text(getPageName()),
            ),
            body: data != null ? buildBody() : Center(child: CircularProgressIndicator()),
            bottomNavigationBar: BottomAppBar(
                child: Container(
                    height: 50.0,
                ),
            ),

            drawer: Drawer(
                child: ListView(
                    padding: EdgeInsets.zero,

                    children: <Widget>[
                        ListTile(
                            title: Text('Menu',
                                style: TextStyle(
                                    fontWeight: FontWeight.bold,
                                    fontSize: 19,
                                ))
                        ),

                        // Menu
                        {%- for app_name, app in apps.items() %}{% if app.flutter %}{% for name, page in app.pages.items() %}{% if page.flutter %}
                        ListTile(
                            title: Text('{{ page.view_name }}'),
{#                            selected: this is {{ app_name.capitalize() }}{{ page.view_name }},#}
                            onTap: () {
                                Navigator.pushNamed(context, '{{ page.uri }}');
                            },
                        ),
                        {%- endif %}{% endfor %}{% endif %}{% endfor %}
                    ],
                ),
            )
        );
    }

    Widget buildBody();

    String getPageName();
}

