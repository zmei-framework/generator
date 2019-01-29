from textwrap import dedent

from zmei_generator.contrib.docker.extensions.application.docker import DockerAppExtension
from zmei_generator.parser.parser import ZmeiParser


def _(code):
    parser = ZmeiParser()
    parser.parse_string(dedent(code))
    return parser.populate_application('example')


def test_docker_enabled():
    app = _("""

        @docker
    """)

    assert app.supports(DockerAppExtension)

