import 'dart:io';

import 'package:flutter/material.dart';

import 'dart:convert';
import 'package:http/http.dart' as http;
import 'package:web_socket_channel/io.dart';


class PageStatefulWidget extends StatefulWidget {
    final PageState state;

    PageStatefulWidget(this.state);

    @override
    PageState createState() => state;
}


abstract class PageState extends State<PageStatefulWidget> {

    static String cookie = null;
    static String csrf = null;

    bool hasRemoteData = false;
    bool hasStreams = false;
    bool reconnecting = false;
    bool closed = false;
    IOWebSocketChannel channel;

    dynamic data;
    String pageUrl = "";
    String wsUrl = "";

    bool isDataReady() {
        if (!hasRemoteData) return true;

        return data != null;
    }

    void loadData(newState) {
        data = newState;
        print('New state: $newState');
    }

    @override
    void dispose() {

        closed = true;

        if (channel != null) {
            channel.sink.close();
            channel = null;
        }

        super.dispose();
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

    reconnect() async {
        if (closed || reconnecting || channel != null) return;
        reconnecting = true;

        print('Reconnect in 3 seconds...');

        await new Future.delayed(const Duration(seconds: 4));

        print('Reconnecting...');

        if (channel == null) {
            listenStream();
        }
    }

    listenStream() async {
        reconnecting = false;

        channel = await IOWebSocketChannel.connect(wsUrl, pingInterval: Duration(milliseconds: 1000));
        print('Connected');

        channel.stream.listen((message) {
            setState(() {
                loadData(json.decode(message)['__state__']);
            });
        }, onDone: () {
            print('Connection terminated');
            channel = null;

            reconnect();

        }, onError: (error) {
            print(error);
            channel = null;

            reconnect();
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
        var token = Cookie.fromSetCookieValue(PageState.cookie).value;

        final response = await http.post(pageUrl, headers: {
            "Content-type": "application/json",
            "Accept": "application/json",
            "Cookie": cookie,
            "X-CSRFToken": token
        }, body: json.encode({'method': method, 'args': args}));

        if (response.headers.containsKey('set-cookie')) {
            PageState.cookie = response.headers['set-cookie'];
        }

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