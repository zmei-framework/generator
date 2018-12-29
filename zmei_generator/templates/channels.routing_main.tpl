
from channels.auth import AuthMiddlewareStack
from channels.routing import ProtocolTypeRouter, URLRouter
from django.conf.urls import url
{{ imports.import_sting() }}

application = ProtocolTypeRouter({
    # (http->django views is added by default)

    'websocket': AuthMiddlewareStack(
        URLRouter([{% for app, page in streams %}
            url(r'^ws/pages/{{ page.urls_line.strip('^') }}', {{ page.streaming_page.view_name }}Consumer),
        {% endfor %}])
    ),
})
