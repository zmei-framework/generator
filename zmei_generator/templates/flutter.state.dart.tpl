//# generated: 141b1f119c1443611d2ded6667616db7

import 'package:flutter/material.dart';

import 'dart:convert';
import 'package:http/http.dart' as http;


class PageStatefulWidget extends StatefulWidget {
    final PageState state;

    PageStatefulWidget(this.state);

    @override
    PageState createState() => state;
}


abstract class PageState extends State<PageStatefulWidget> {
    final bool hasRemoteData;

    PageState(this.hasRemoteData);

    dynamic data;
    String pageUrl = "";

    void loadData(data) {}

    @override
    void initState() {
        super.initState();

        if (hasRemoteData) {
            reload();
        }
    }

    PageState setUrl(String url) {
        pageUrl = url;

        return this;
    }

    Widget asWidget() {
        return PageStatefulWidget(this);
    }

    reload() async {
        final response = await http.get(pageUrl, headers: {
            "Accept": "application/json"
        });

        if (response.statusCode == 200) {
            setState(() {
                data = json.decode(response.body);
            });
        } else {
            // If that response was not OK, throw an error.
            throw Exception('Failed to load post');
        }
    }
}