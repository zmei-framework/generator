from zmei_generator.contrib.web.extensions.page.auth import AuthPageExtensionParserListener
from zmei_generator.contrib.web.extensions.page.error import ErrorPageExtensionParserListener
from zmei_generator.contrib.web.extensions.page.get import GetPageExtensionParserListener
from zmei_generator.contrib.web.extensions.page.post import PostPageExtensionParserListener

parsers = [
    GetPageExtensionParserListener,
    PostPageExtensionParserListener,
    ErrorPageExtensionParserListener,
    AuthPageExtensionParserListener,
]