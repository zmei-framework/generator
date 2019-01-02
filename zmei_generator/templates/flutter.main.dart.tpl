import 'package:flutter/material.dart';

import './src/state.dart';
import './src/app.dart';

void main() {
    PageStateProvider.setup("http://192.168.0.124:8000");
//    PageStateProvider.setup("http://192.168.1.122:8000");
//    PageStateProvider.setup("http://192.168.0.124:8000");

    runApp(new AppComponent());
}