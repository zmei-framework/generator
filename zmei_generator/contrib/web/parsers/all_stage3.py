from zmei_generator.contrib.web.extras.page.auth import AuthPageExtraParserListener
from zmei_generator.contrib.web.extras.page.error import ErrorPageExtraParserListener
from zmei_generator.contrib.web.extras.page.get import GetPageExtraParserListener
from zmei_generator.contrib.web.extras.page.post import PostPageExtraParserListener

parsers = [
    GetPageExtraParserListener,
    PostPageExtraParserListener,
    ErrorPageExtraParserListener,
    AuthPageExtraParserListener,
]