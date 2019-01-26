
import os

from fabric.operations import local, run, sudo
from fabric.context_managers import cd
from fabric.state import env


env.hosts = ['root@zmei-framework.com']

# def build():
#     loc


def deploy():
    local('gmake clean')
    local('gmake html')
    local('rsync --delete -rv _build/html/ root@zmei-framework.com:/var/www/html/generator/')
