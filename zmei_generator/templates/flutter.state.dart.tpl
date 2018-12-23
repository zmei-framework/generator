import 'package:flutter/material.dart';

import 'dart:convert';
import 'package:http/http.dart' as http;
import 'package:web_socket_channel/io.dart';
import 'package:web_socket_channel/status.dart' as status;


class PageStatefulWidget extends StatefulWidget {
    final PageState state;

    PageStatefulWidget(this.state);

    @override
    PageState createState() => state;
}


abstract class PageState extends State<PageStatefulWidget> {
    static String cookie = '';

    bool hasRemoteData = false;
    bool hasStreams = false;
    IOWebSocketChannel channel;

    dynamic data;
    String pageUrl = "";
    String wsUrl = "";

    void loadData(newState) {
        data = newState;
    }

    @override
    void initState() {
        super.initState();

        if (hasRemoteData) {
            reload();
        }

        if (hasStreams) {
            listenStream();
        }
    }

    @override
    void dispose() {
        if (channel != null) {
            channel.sink.close(status.goingAway);
            channel = null;
        }
    }

    PageState setDataUrl(String url) {
        pageUrl = url;
        hasRemoteData = true;

        return this;
    }

    PageState setWsUrl(String url) {
        wsUrl = url.replaceFirst('http', 'ws');
        hasStreams = true;

        return this;
    }

    Widget asWidget() {
        return PageStatefulWidget(this);
    }

    listenStream() async {
        channel = await IOWebSocketChannel.connect(wsUrl);

        channel.stream.listen((message) {
            setState(() {
                loadData(json.decode(message)['__state__']);
            });
        });

    }

    reload() async {
        final response = await http.get(pageUrl, headers: {
            "Accept": "application/json",
            "Cookie": PageState.cookie
        });

        if (response.headers.containsKey('set-cookie')) {
            PageState.cookie = response.headers['set-cookie'];
        }

        if (response.statusCode == 200) {
            setState(() {
                loadData(json.decode(response.body));
            });
        } else {
            // If that response was not OK, throw an error.
            throw Exception('Failed to load post');
        }
    }

    callRemote(String method, args) async {
        final response = await http.post(pageUrl, headers: {
            "Content-type": "application/json",
            "Accept": "application/json",
            "Cookie": PageState.cookie
        }, body: json.encode({'method': method, 'args': args}));

        if (response.statusCode == 200) {
            Map<String, dynamic> data = json.decode(response.body);

            if (data.containsKey('__error__')) throw Exception(data['__error__']);
            if (data.containsKey('__state__')) {
                setState(() {
                    loadData(data['__state__']);
                });

                return data['__state__'];
            }

            return data;

        } else {
            // If that response was not OK, throw an error.
            throw Exception('Failed to load post');
        }
    }
}