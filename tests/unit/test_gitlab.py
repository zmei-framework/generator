from textwrap import dedent

from zmei_generator.extras.collection_set.gitlab import GitlabCsExtra, SeleniumPytestConfig
from zmei_generator.parser.parser import ZmeiParser


def _(code):
    parser = ZmeiParser()
    parser.parse_string(dedent(code))
    return parser.populate_collection_set('example')


def test_gitlab_full_config():
    cs = _("""

    @gitlab(
        develop => dev(dev.foo.example.com: SERVER_PORT=3000, FOO=322)
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


def test_gitlab_deploy_type():
    cs = _("""

    @gitlab(
        develop => dev(dev.foo.example.com: SERVER_PORT=3000, FOO=322)
        master ~> prod(example.com)
    )

    """)

    assert isinstance(cs.gitlab, GitlabCsExtra)

    assert len(cs.gitlab.configs) == 2

    develop = cs.gitlab.configs[0]
    assert develop.manual_deploy is False
    assert develop.branch == 'develop'
    assert develop.deployment == 'dev'
    assert develop.hostname == 'dev.foo.example.com'
    assert develop.vars == {'SERVER_PORT': "3000", 'FOO': "322"}

    master = cs.gitlab.configs[1]
    assert master.manual_deploy is True
    assert master.branch == 'master'
    assert master.deployment == 'prod'
    assert master.hostname == 'example.com'
    assert master.vars == {}


def test_wildcard():
    cs = _("""

    @gitlab(
        feature/lala-* => hello-review/*(
            *.hello.dev.negative.ee:
    
            key=DOCKER_CERT_DEV
            docker="tcp://dev.negative.ee:2376"
        )
    )

    """)

    assert isinstance(cs.gitlab, GitlabCsExtra)

    assert len(cs.gitlab.configs) == 1

    develop = cs.gitlab.configs[0]
    assert develop.manual_deploy is False
    assert develop.branch == '/^feature\/lala-.*$/'
    assert develop.deployment == 'hello-review-*'
    assert develop.environment == 'hello-review/*'
    assert develop.hostname == '*.hello.dev.negative.ee'


def test_artifacts():
    cs = _("""

    @gitlab(
        develop => dev(dev.foo.example.com: coverage="lala", SERVER_PORT=3000, FOO=322)
        master ~> prod(example.com)
    )

    """)

    assert isinstance(cs.gitlab, GitlabCsExtra)

    assert len(cs.gitlab.configs) == 2

    develop = cs.gitlab.configs[0]
    assert develop.coverage is True
    assert develop.vars['coverage'] == 'lala/'

    master = cs.gitlab.configs[1]
    assert master.coverage is False


def test_gitlab_with_tests():
    cs = _("""

    @gitlab(
        selenium_pytest(
            services(rabbitmq, redis(image="ololo/test:123"), influxdb)
    
            SOME_INFLUX_HOST=influxdb
            SOME_RABBITMQ_HOST=rabbitmq
            SOME_REDIS_HOST=redis
        )
    
        master => prod(example.com)
    )

    """)

    assert isinstance(cs.gitlab, GitlabCsExtra)

    assert len(cs.gitlab.configs) == 1

    master = cs.gitlab.configs[0]
    assert master.branch == 'master'
    assert master.deployment == 'prod'
    assert master.hostname == 'example.com'
    assert master.vars == {}

    assert isinstance(cs.gitlab.test, SeleniumPytestConfig)

    assert list(cs.gitlab.test.services.keys()) == ['rabbitmq', 'redis', 'influxdb']
    assert cs.gitlab.test.services['redis'].vars == {'image': '"ololo/test:123"'}
    assert cs.gitlab.test.vars == {
        'SOME_INFLUX_HOST': "influxdb",
        'SOME_RABBITMQ_HOST': "rabbitmq",
        'SOME_REDIS_HOST': "redis",
    }

def test_can_parse_full_config():
    cs = _("""

    @docker
    @gitlab(
        selenium_pytest(
            services(rabbitmq, redis, influxdb)
    
            XTRAX_INFLUX_HOST=influxdb
            XTRAX_RABBITMQ_HOST=rabbitmq
            XTRAX_REDIS_HOST=redis
        )
    
        develop => dev(
            dev.xtrax1.negative.ee:
    
            key=DOCKER_CERTS
            docker="tcp://xtrax1.negative.ee:2376"
        )
    
        master => staging(
            staging.xtrax1.negative.ee:
    
            key=DOCKER_CERTS
            docker="tcp://xtrax1.negative.ee:2376"
        )
    
        master ~> prod(
            xtrax1.negative.ee:
    
            key=DOCKER_CERTS
            docker="tcp://xtrax1.negative.ee:2376"
        )
    )

    """)

    assert isinstance(cs.gitlab, GitlabCsExtra)
