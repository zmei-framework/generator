from zmei_generator.contrib.channels.extras.pages.stream import StreamPageExtraParserListener
from zmei_generator.contrib.web.extras.page.auth import AuthPageExtraParserListener
from zmei_generator.contrib.web.extras.page.error import ErrorPageExtraParserListener
from zmei_generator.contrib.flutter.extras.page.flutter import FlutterPageExtraParserListener
from zmei_generator.contrib.web.extras.page.get import GetPageExtraParserListener
from zmei_generator.contrib.web.extras.page.post import PostPageExtraParserListener

parsers = [
    FlutterPageExtraParserListener,
    StreamPageExtraParserListener,
    GetPageExtraParserListener,
    PostPageExtraParserListener,
    ErrorPageExtraParserListener,
    AuthPageExtraParserListener,
]