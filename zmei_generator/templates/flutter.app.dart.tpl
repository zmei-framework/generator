import 'package:flutter/material.dart';

MaterialApp buildApp(final Map<String, WidgetBuilder> routes) {
    return MaterialApp(
        title: 'My app',
        initialRoute: '/',

        theme: ThemeData(
            primarySwatch: Colors.purple,
        ),

        routes: routes,
    );
}

