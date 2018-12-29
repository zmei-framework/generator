import 'package:flutter/material.dart';
import 'package:my_app/src/utils.dart';

import 'dart:convert';
import 'package:web_socket_channel/io.dart';


class PageStatefulWidget extends StatefulWidget {
    final PageState state;

    PageStatefulWidget(this.state);

    @override
    PageState createState() => state;
}


abstract class PageState extends State<PageStatefulWidget> {

    static String cookie;

    bool hasRemoteData = false;
    bool hasStreams = false;
    bool reconnecting = false;
    bool closed = false;
    IOWebSocketChannel channel;

    dynamic data;
    String pageUrl = "";
    String wsUrl = "";

    @override
    void initState() {
        super.initState();
    }

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

        channel = await IOWebSocketChannel.connect(
            wsUrl, pingInterval: Duration(milliseconds: 1000));
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
        var result = await httpRequest(pageUrl);

        setState(() {
            loadData(result);
        });
    }

    callRemote(String method, args) async {
        var data = await httpRequest(pageUrl, post: true, body: {
            'method': method,
            'args': args
        });

        if (data is Map) {
            if (data.containsKey('__error__')) throw Exception(
                data['__error__']);
            if (data.containsKey('__state__')) {
                setState(() {
                    loadData(data['__state__']);
                });

                return data['__state__'];
            }
        }

        return data;
    }
}