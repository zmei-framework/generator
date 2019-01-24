from textwrap import dedent

from zmei_generator.contrib.docker.extras.collection_set.docker import DockerCsExtra
from zmei_generator.parser.parser import ZmeiParser


def _(code):
    parser = ZmeiParser()
    parser.parse_string(dedent(code))
    return parser.populate_collection_set('example')


def test_docker_enabled():
    cs = _("""

        @docker
    """)

    assert isinstance(cs.docker, DockerCsExtra)

