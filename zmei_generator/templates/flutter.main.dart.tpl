
import './src/state.dart';
import './src/routes.dart';

void main() {
    PageStateProvider.setup("http://192.168.0.124:8000");

    routes();
}