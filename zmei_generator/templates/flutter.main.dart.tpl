import 'package:flutter/material.dart';

import './src/state.dart';
import './src/app.dart';

void main() {
    PageStateProvider.setup("http://{{ host }}");

    runApp(new AppComponent());
}