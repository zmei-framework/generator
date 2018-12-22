import 'package:flutter/material.dart';

import 'dart:convert';
import 'package:http/http.dart' as http;


class PageStatefulWidget extends StatefulWidget {
    PageState state;

    PageStatefulWidget(this.state);

    @override
    PageState createState() => state;
}


abstract class PageState extends State<PageStatefulWidget> {
    dynamic data;
    String pageUrl = "";

    @override
    void initState() {
        super.initState();

        loadPageData();
    }

    PageState setUrl(String url) {
        pageUrl = url;

        return this;
    }

    Widget asWidget() {
        return PageStatefulWidget(this);
    }

    loadPageData() async {
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
