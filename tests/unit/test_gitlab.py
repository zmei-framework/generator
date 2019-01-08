from textwrap import dedent

from zmei_generator.extras.collection_set.gitlab import GitlabCsExtra
from zmei_generator.parser.parser import ZmeiParser


def _(code):
    parser = ZmeiParser()
    parser.parse_string(dedent(code))
    return parser.populate_collection_set('example')


def test_gitlab_full_config():
    cs = _("""

    @gitlab(
        develop => dev(dev.foo.example.com, SERVER_PORT=3000 FOO=322)
        master => prod(example.com)
    )

    """)

    assert isinstance(cs.gitlab, GitlabCsExtra)

    assert len(cs.gitlab.configs) == 2

    develop = cs.gitlab.configs[0]
    assert develop.branch == 'develop'
    assert develop.deployment == 'dev'
    assert develop.hostname == 'dev.foo.example.com'
    assert develop.vars == {'SERVER_PORT': "3000", 'FOO': "322"}

    master = cs.gitlab.configs[1]
    assert master.branch == 'master'
    assert master.deployment == 'prod'
    assert master.hostname == 'example.com'
    assert master.vars == {}

