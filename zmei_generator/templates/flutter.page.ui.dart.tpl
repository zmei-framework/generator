import 'package:flutter/material.dart';
import './{{ page.name }}.dart';

{% if not page.uri %}abstract {% endif %}class {{ page.view_name }}StateUi extends {{ page.view_name }}State {

    {% if not page.get_parent() %}
        @override
        Widget build(BuildContext context) {
            return Scaffold(
                appBar: buildAppBar(),
                body: buildBodyWhenReady(),
                floatingActionButton: buildFloatingActionButton(),
                bottomNavigationBar: buildBottomMenu(),
                drawer: buildDrawer()
            );
        }

          @override
          Widget build(BuildContext context) {
            return Scaffold(
                appBar: buildAppBar(),
                body: buildBodyWhenReady(),
                floatingActionButton: buildFloatingActionButton(),
                bottomNavigationBar: buildBottomMenu(),
                drawer: buildDrawer()
            );
          }

          AppBar buildAppBar() {
            return AppBar(
              backgroundColor: Colors.green,
              title: Text(getPageName()),
            );
          }

          Widget buildFloatingActionButton() {
            return null;
          }

          Widget buildDrawer() {
            return null;
          }

          Widget buildBodyWhenReady() {
            return isDataReady() ? Builder(builder: buildBody) : Center(
                child: CircularProgressIndicator());
          }

          Widget buildBody(BuildContext context) {
            return Center(
              child: Text('Data received: $data'),
            );
          }
    {% endif %}

    {% if page.uri %}
    Widget build(BuildContext context) {
        return Center(
            child: Text('Nothing here!'),
        );
    }
    {% endif %}

    @override
    String getPageName() {
        return "{{ app_name.capitalize() }}{{ page.view_name }}";
    }
}