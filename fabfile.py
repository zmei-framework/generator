import os

from fabric.operations import local, run, sudo
from fabric.context_managers import cd
from fabric.state import env


env.hosts = ['root@ng.genius-project.io']

def gen():
    lib = os.path.realpath('zmei_generator/parser/gen/grammar')
    lexerSrc = '{lib}/ZmeiLangSimpleLexer.g4'.format(**locals())
    parserSrc = '{lib}/ZmeiLangParser.g4'.format(**locals())

    dst = 'zmei_generator/parser/gen'

    package = 'zmei_generator.parser.gen'

    antlr_jar = 'zmei_generator/lib/antlr/antlr-4.7.2-complete.jar'
    antlr = 'CLASSPATH="%s:." java -jar %s' % (antlr_jar, antlr_jar)

    local('{antlr} -Dlanguage=Python3 -o {dst} -package {package} -lib {lib} -listener {lexerSrc}'.format(**locals()))
    local('{antlr} -Dlanguage=Python3 -o {dst} -package {package} -lib {lib} -listener {parserSrc}'.format(**locals()))

def coverage():
    local('py.test tests/unit/ --cov=zmei_generator  --cov-report=html')
