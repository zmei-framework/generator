import 'package:flutter/material.dart';

MaterialApp buildApp(final Map<String, WidgetBuilder> routes) {
    return MaterialApp(
        title: 'Named Routes Demo',
        initialRoute: '/',

        theme: ThemeData(
            primarySwatch: Colors.purple,
        ),

        routes: routes,
    );
}

