from zmei_generator.contrib.celery.extensions.application.celery import CeleryAppExtensionParserListener
from zmei_generator.contrib.docker.extensions.application.docker import DockerAppExtensionParserListener
from zmei_generator.contrib.filer.extensions.application.filer import FilerAppExtensionParserListener
from zmei_generator.contrib.gitlab.extensions.application.gitlab import GitlabAppExtensionParserListener
from zmei_generator.contrib.react.extensions.page.react import ReactPageExtensionParserListener
from zmei_generator.contrib.web.extensions.application.file import FileAppExtensionParserListener
from zmei_generator.contrib.web.extensions.application.langs import LangsAppExtensionParserListener
from zmei_generator.contrib.web.extensions.application.theme import ThemeAppExtensionParserListener
from zmei_generator.contrib.web.extensions.page.crud_create import CrudCreatePageExtensionParserListener
from zmei_generator.contrib.web.extensions.page.crud_delete import CrudDeletePageExtensionParserListener
from zmei_generator.contrib.web.extensions.page.crud_detail import CrudDetailPageExtensionParserListener
from zmei_generator.contrib.web.extensions.page.crud_edit import CrudEditPageExtensionParserListener
from zmei_generator.contrib.web.extensions.page.crud_list import CrudListPageExtensionParserListener
from zmei_generator.contrib.web.extensions.page.crud_parser import CrudPageExtensionParserListener
from zmei_generator.contrib.web.extensions.page.html import HtmlPageExtensionParserListener
from zmei_generator.contrib.web.extensions.page.markdown import MarkdownPageExtensionParserListener
from zmei_generator.contrib.web.extensions.page.menu import MenuPageExtensionParserListener
from zmei_generator.contrib.web.extensions.page.placeholder import PlaceholderPageExtensionParserListener

from zmei_generator.contrib.web.parsers.fields import FieldsParserListener
from zmei_generator.contrib.web.parsers.imports import ImportsParserListener
from zmei_generator.contrib.web.parsers.model import ModelParserListener
from zmei_generator.contrib.web.parsers.page import PageParserListener

parsers = [
    FieldsParserListener,
    ImportsParserListener,
    ModelParserListener,
    PageParserListener,


    # extensions
    ThemeAppExtensionParserListener,
    GitlabAppExtensionParserListener,
    DockerAppExtensionParserListener,
    FileAppExtensionParserListener,
    CeleryAppExtensionParserListener,
    LangsAppExtensionParserListener,
    FilerAppExtensionParserListener,

    MenuPageExtensionParserListener,
    MarkdownPageExtensionParserListener,
    PlaceholderPageExtensionParserListener,
    ReactPageExtensionParserListener,
    HtmlPageExtensionParserListener,


    CrudPageExtensionParserListener,
    CrudDetailPageExtensionParserListener,
    CrudDeletePageExtensionParserListener,
    CrudEditPageExtensionParserListener,
    CrudListPageExtensionParserListener,
    CrudCreatePageExtensionParserListener,
]