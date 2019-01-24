import 'package:fluro/fluro.dart';
import 'package:flutter/material.dart';

import '../app.dart';

class MenuItem {
  Icon icon;
  String title;
  String route;
  Map<String, String> args;

  MenuItem(this.icon, this.title, this.route, {this.args});

  onTapped(BuildContext context) {
    App.router.navigateTo(context, route, transition: getTransitionType(), clearStack: true);
  }

  static const transitions = <String, TransitionType>{
    'native': TransitionType.native,
    'nativeModal': TransitionType.nativeModal,
    'inFromLeft': TransitionType.inFromLeft,
    'inFromRight': TransitionType.inFromRight,
    'inFromBottom': TransitionType.inFromBottom,
    'fadeIn': TransitionType.fadeIn,
    'custom': TransitionType.custom,
  };

  TransitionType getTransitionType() {
    if (args != null && args.containsKey('transition') && transitions.containsKey(args['transition'])) {
      return transitions[args['transition']];
    }

    return TransitionType.fadeIn;
  }

  bool isActive() {
    if (App.urlStack == null) return false;
    return App.urlStack.contains(this.route);
  }

  BottomNavigationBarItem buildBottomNavBarItem(BuildContext context) {
    return BottomNavigationBarItem(icon: icon, title: Text(title));
  }

  Widget buildDrawerItem(BuildContext context) {
    return GestureDetector(
      onTap: () => onTapped(context),
      child: ListTile(
        contentPadding: EdgeInsets.only(left: 30),
        leading: icon,
        title: Text(
          title,
          style: TextStyle(fontWeight: FontWeight.bold, fontSize: 18),
        ),
      ),
    );
  }
}