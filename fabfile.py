from fabric.operations import local, run, sudo
from fabric.context_managers import cd
from fabric.state import env


env.hosts = ['root@ng.genius-project.io']


def deploy():

    with cd('/var/www/app'):
        local('rsync -rv ./ root@ng.genius-project.io:/var/www/app/')
        run('/var/www/app/.pyvenv/bin/pip install -e .')
        run('systemctl restart zmei')