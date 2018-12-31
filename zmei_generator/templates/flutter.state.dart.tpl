
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

class PageStream {
    String streamUrl;
    List<PageState> streamListeners;

    bool reconnecting = false;
    bool closed = false;
    IOWebSocketChannel channel;

    PageStream(this.streamUrl) {
        streamListeners = List<PageState>();
    }

    subscribe(PageState page) {
        if (channel == null) {
            listenStream();
        }
        if (!streamListeners.contains(page)) {
            streamListeners.add(page);
        }
    }

    unsubscribe(PageState page) {
        if (streamListeners.contains(page)) {
            streamListeners.remove(page);
        }
    }

    cleanUp() {
        if (streamListeners.length == 0) {
            closeStream();
        }
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

        print("Connecting to: $streamUrl");

        channel = await IOWebSocketChannel.connect(
            streamUrl, pingInterval: Duration(milliseconds: 1000));

        print('Connected: $streamUrl');

        channel.stream.listen((message) {

            for(PageState page in streamListeners) {
                page.onRemoteUpdate(json.decode(message));
            }
        }, onDone: () {
            print('Connection terminated: $streamUrl"');
            channel = null;

            reconnect();
        }, onError: (error) {
            print('Connection error: $streamUrl"');
            print(error);
            channel = null;

            reconnect();
        });
    }

    closeStream() async {
        print('Connection close: $streamUrl"');
        closed = true;

        if (channel != null) {
            await channel.sink.close();
            channel = null;
        }
    }
}

class PageStateProvider {
    static PageStateProvider _instance;

    static PageStateProvider setup(String baseUrl) {
        if (_instance != null) {
            throw Exception('PageStateProvider already configured!');
        }
        _instance = PageStateProvider._(baseUrl);
        return _instance;
    }
    static PageStateProvider getInstance() {
        if (_instance == null) {
            throw Exception('PageStateProvider is not configured yet!');
        }
        return _instance;
    }

    String baseUrl;
    Map<String, PageStream> streams;

    PageStateProvider._(this.baseUrl) {
        streams = Map<String, PageStream>();
    }

    String formatStreamUrl(String streamUrl) {
        return "${baseUrl.replaceFirst('http', 'ws')}$streamUrl";
    }

    subscribeStream(String streamUrl, PageState page) {
        if (!streams.containsKey(streamUrl)) {
            streams[streamUrl] = PageStream(formatStreamUrl(streamUrl));
        }
        streams[streamUrl].subscribe(page);
    }

    closeUnusedStreams() {
        streams.forEach((url, stream) => stream.cleanUp());
    }

    unsubscribeStream(String streamUrl, PageState page) {
        if (streams.containsKey(streamUrl)) {
            streams[streamUrl].unsubscribe(page);
        }
    }

    loadRemoteState(PageState page) async {
        print("Loading data from: $baseUrl${page.getPageUrl()}");
        var result = await httpRequest("$baseUrl${page.getPageUrl()}");

        page.onRemoteUpdate(result);

        return result;
    }

    callRemoteFunction(PageState page, String method, List<dynamic> args) async {
        var data = await httpRequest("$baseUrl${page.getPageUrl()}", post: true, body: {
            'method': method,
            'args': args
        });

        if (data is Map) {
            if (data.containsKey('__error__')) throw Exception(
                data['__error__']);
            if (data.containsKey('__state__')) {
                page.onRemoteUpdate(data['__state__']);

                return data['__state__'];
            }
        }

        return data;
    }
}

abstract class PageState extends State<PageStatefulWidget> {

    dynamic data;

    Widget asWidget() {
        return PageStatefulWidget(this);
    }

    String getPageUrl() {
        throw Exception("Page has no remote url!");
    }

    bool hasRemoteData() {
        return false;
    }



    @override
    void initState() {
        print('Init: $this');
        super.initState();

        if (hasRemoteData()) {
            loadRemoteState();
        }
    }


    @override
    void dispose() {
        super.dispose();
        print('Dispose: $this');

        PageStateProvider.getInstance().closeUnusedStreams();
    }

    bool isDataReady() {
        if (!hasRemoteData()) return true;

        return data != null;
    }

    loadData(newState) {
        data = newState;
        print('New state: $newState');
    }

    subscribeStream(String streamUrl) {
        PageStateProvider.getInstance().subscribeStream(streamUrl, this);
    }

    unsubscribeStream(String streamUrl) {
        PageStateProvider.getInstance().unsubscribeStream(streamUrl, this);
    }

    onRemoteUpdate(data) {
        setState(() {
            loadData(data);
        });
    }

    loadRemoteState() async {
        return PageStateProvider.getInstance().loadRemoteState(this);
    }

    callRemote(String method, List<dynamic> args) async {
        return PageStateProvider.getInstance().callRemoteFunction(this, method, args);
    }
}