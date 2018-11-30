import os

from fabric.operations import local, run, sudo
from fabric.context_managers import cd
from fabric.state import env


env.hosts = ['root@ng.genius-project.io']

def tunnel():
    local('ssh root@zmei-framework.com -L 9200:127.0.0.1:9200 -L 9300:127.0.0.1:9300 -L 5601:127.0.0.1:5601')

def deploy():

    with cd('/var/www/app'):
        local('rsync -rv --exclude .git --exclude .idea ./ root@ng.genius-project.io:/var/www/app/')
        run('/var/www/app/.pyvenv/bin/pip install -e .')
        run('systemctl restart zmei')


def gen():
    lib = os.path.realpath('grammar')
    lexerSrc = '{lib}/ZmeiLangSimpleLexer.g4'.format(**locals())
    parserSrc = '{lib}/ZmeiLangParser.g4'.format(**locals())

    dst = 'zmei_generator/parser/gen'

    package = 'zmei_generator.parser.gen'

    local('antlr4 -Dlanguage=Python3 -o {dst} -package {package} -lib {lib} -listener {lexerSrc}'.format(**locals()))
    local('antlr4 -Dlanguage=Python3 -o {dst} -package {package} -lib {lib} -listener {parserSrc}'.format(**locals()))

def coverage():
    local('py.test tests/unit/ --cov=zmei_generator  --cov-report=html')
