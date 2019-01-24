from zmei_generator.contrib.celery.extras.collection_set.celery import CeleryCsExtraParserListener
from zmei_generator.contrib.channels.extras.collection_set.channels import ChannelsCsExtraParserListener
from zmei_generator.contrib.docker.extras.collection_set.docker import DockerCsExtraParserListener
from zmei_generator.contrib.filer.extras.collection_set.filer import FilerCsExtraParserListener
from zmei_generator.contrib.gitlab.extras.collection_set.gitlab import GitlabCsExtraParserListener
from zmei_generator.contrib.react.extras.page.react import ReactPageExtraParserListener
from zmei_generator.contrib.web.extras.collection_set.file import FileCsExtraParserListener
from zmei_generator.contrib.web.extras.collection_set.langs import LangsCsExtraParserListener
from zmei_generator.contrib.web.extras.collection_set.theme import ThemeCsExtraParserListener
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
    ThemeCsExtraParserListener,
    GitlabCsExtraParserListener,
    DockerCsExtraParserListener,
    FileCsExtraParserListener,
    ChannelsCsExtraParserListener,
    CeleryCsExtraParserListener,
    LangsCsExtraParserListener,
    FilerCsExtraParserListener,

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