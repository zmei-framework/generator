
import 'dart:io';
import 'dart:convert';
import 'package:shared_preferences/shared_preferences.dart';

const COOKIE_KEY = 'http-cookies-v1';

httpRequest(String url, {bool post=false, dynamic body}) async {
    SharedPreferences prefs = await SharedPreferences.getInstance();
    HttpClient client = new HttpClient();

    var requestMethod = post ? client.postUrl : client.getUrl;

    var request = await (requestMethod)(Uri.parse(url));

    if (post) {
        request.headers.set(HttpHeaders.contentTypeHeader, "application/json");
    }
    request.headers.set(HttpHeaders.acceptHeader, "application/json");

    request.headers.contentType = new ContentType("application", "json", charset: "utf-8");

    List<Cookie> oldCookies = [];
    if (prefs.getString(COOKIE_KEY) != null) {
        for (var cookieStr in prefs.getString(COOKIE_KEY).split('|')) {
            try {
                var cookie = Cookie.fromSetCookieValue(cookieStr);

                request.cookies.add(cookie);
                oldCookies.add(cookie);

                if (cookie.name == 'csrftoken') {
                    request.headers.set("X-CSRFToken", cookie.value);
                }

            } catch(e) {
                // Invalid
                if (!(e is RangeError)) {
                    throw e;
                }
            }

        }
    }

    if (post && body != null) {
        var data = json.encode(body);
        request.headers.set(HttpHeaders.contentLengthHeader, data.length);

        request.write(data);
    }
    var response = await request.close();

    Map<String, Cookie> newCookies = {};
    for(var cookie in oldCookies) {
        newCookies[cookie.name] = cookie;
    }
    for(var cookie in response.cookies) {
        newCookies[cookie.name] = cookie;
    }

    var newCookie = newCookies.values.map((c) => c.toString()).join('|');
    if (newCookie != '') {
        await prefs.setString(COOKIE_KEY, newCookie);
    }

    if (response.statusCode == 200) {
        var res = await response.transform(utf8.decoder).join();

        return json.decode(res);

    } else {
        // If that response was not OK, throw an error.
        throw Exception('Ошибка: ${response.statusCode}');
    }
}