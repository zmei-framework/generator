import 'package:flutter/material.dart';
import 'package:fluro/fluro.dart';

import './routes.dart';


class App {
    static Router router;
    static Routes url = Routes();
    static List<String> urlStack;
}

class AppComponent extends StatefulWidget {
    @override
    State createState() {
        return new AppComponentState();
    }
}

class AppComponentState extends State<AppComponent> {
    AppComponentState() {
        final router = new Router();
        configureRoutes(router);
        App.router = router;
    }

    @override
    Widget build(BuildContext context) {
        final app = new MaterialApp(
            title: 'My app',
            debugShowCheckedModeBanner: false,
//            theme: new ThemeData(
//                primaryColor: Colors.green,
//
//            ),
            onGenerateRoute: App.router.generator,
        );
        print("initial route = ${app.initialRoute}");
        return app;
    }
}