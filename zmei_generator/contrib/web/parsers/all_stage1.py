from zmei_generator.contrib.celery.extras.application.celery import CeleryAppExtraParserListener
from zmei_generator.contrib.docker.extras.application.docker import DockerAppExtraParserListener
from zmei_generator.contrib.filer.extras.application.filer import FilerAppExtraParserListener
from zmei_generator.contrib.gitlab.extras.application.gitlab import GitlabAppExtraParserListener
from zmei_generator.contrib.react.extras.page.react import ReactPageExtraParserListener
from zmei_generator.contrib.web.extras.application.file import FileAppExtraParserListener
from zmei_generator.contrib.web.extras.application.langs import LangsAppExtraParserListener
from zmei_generator.contrib.web.extras.application.theme import ThemeAppExtraParserListener
from zmei_generator.contrib.web.extras.page.crud_create import CrudCreatePageExtraParserListener
from zmei_generator.contrib.web.extras.page.crud_delete import CrudDeletePageExtraParserListener
from zmei_generator.contrib.web.extras.page.crud_detail import CrudDetailPageExtraParserListener
from zmei_generator.contrib.web.extras.page.crud_edit import CrudEditPageExtraParserListener
from zmei_generator.contrib.web.extras.page.crud_list import CrudListPageExtraParserListener
from zmei_generator.contrib.web.extras.page.crud_parser import CrudPageExtraParserListener
from zmei_generator.contrib.web.extras.page.html import HtmlPageExtraParserListener
from zmei_generator.contrib.web.extras.page.markdown import MarkdownPageExtraParserListener
from zmei_generator.contrib.web.extras.page.menu import MenuPageExtraParserListener
from zmei_generator.contrib.web.extras.page.placeholder import PlaceholderPageExtraParserListener

from zmei_generator.contrib.web.parsers.fields import FieldsParserListener
from zmei_generator.contrib.web.parsers.imports import ImportsParserListener
from zmei_generator.contrib.web.parsers.model import ModelParserListener
from zmei_generator.contrib.web.parsers.page import PageParserListener

parsers = [
    FieldsParserListener,
    ImportsParserListener,
    ModelParserListener,
    PageParserListener,


    # extras
    ThemeAppExtraParserListener,
    GitlabAppExtraParserListener,
    DockerAppExtraParserListener,
    FileAppExtraParserListener,
    CeleryAppExtraParserListener,
    LangsAppExtraParserListener,
    FilerAppExtraParserListener,

    MenuPageExtraParserListener,
    MarkdownPageExtraParserListener,
    PlaceholderPageExtraParserListener,
    ReactPageExtraParserListener,
    HtmlPageExtraParserListener,


    CrudPageExtraParserListener,
    CrudDetailPageExtraParserListener,
    CrudDeletePageExtraParserListener,
    CrudEditPageExtraParserListener,
    CrudListPageExtraParserListener,
    CrudCreatePageExtraParserListener,
]