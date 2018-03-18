import string

import random

import shlex

import argparse
import os
import re

from dateutil.tz import tzlocal

from .config.domain import ValidationException
from .config.parser import Parser
from .generator.collections import generate
from .generator.utils import StopGenerator, fill_file
import subprocess

import sys
import click
from shutil import rmtree


def django_gen(**kwargs):

    parser = argparse.ArgumentParser(description='Django generator')

    parser.add_argument('app', default='all', nargs='?')
    parser.add_argument('--auto', action='store_true')
    parser.add_argument('--init', action='store_true')
    parser.add_argument('--uml', action='store_true')
    parser.add_argument('--rebuild')
    parser.add_argument('--remove')

    args = parser.parse_args()

    handle(**vars(args))




def new_project(auto=False):
    def auto_prompt(message, variable_name, default=None):
        if variable_name:
            default = os.environ.get(variable_name, default)

        if auto and default:
            return default

        return click.prompt('{} ({}): '.format(message, variable_name), default=default)

    if not os.environ.get('VIRTUAL_ENV'):
        click.confirm('You are not in Virtual environment are you sure you want to istall project here?', abort=True)

    template_repo = auto_prompt(
        'Initial project structure', 'DJANGO_GEN_TEMPLATE', default='git@gitlab.com:negativespace/django-app.git',
    )

    project_key = auto_prompt('Project name (slug):', None, default=os.path.basename(os.getcwd()))

    db_user = auto_prompt('DB User', 'DJANGO_GEN_DB_USER', default=os.environ.get('DJANGO_GEN_DB_USER', 'root'))
    db_pass = auto_prompt('DB User', 'DJANGO_GEN_DB_PASS', default=os.environ.get('DJANGO_GEN_DB_PASS', '123123'))
    db_name = auto_prompt('DB Name:', None, default=project_key)

    os.system('rm -rf .tmp_git_dir')
    os.system('git clone --depth 1 {} .tmp_git_dir'.format(shlex.quote(template_repo)))
    os.system('rm -rf .tmp_git_dir/.git')
    os.system('cp -rf .tmp_git_dir/* ./')
    os.system('rm -rf .tmp_git_dir')

    fill_file('app.py', {
        'secret_key': ''.join(random.choices(string.ascii_lowercase + string.ascii_uppercase + string.digits, k=40)),
        'project_key': project_key,
        'time_zone': auto_prompt('Time zone', 'DJANGO_GEN_TIMEZONE', tzlocal()),
        'project_name': project_key.capitalize(),
        'db_user': db_user,
        'db_pass': db_pass,
        'db_name': db_name,
    })

    def mysql_command(commmand, supress_output=False):
        print('-'* 100)
        print(commmand)

        cmd = 'mysql -u {} -p{} -e "{}"'.format(shlex.quote(db_user), shlex.quote(db_pass), commmand,
                                                      ' >/dev/null 2>&1' if supress_output else '')
        print(cmd)
        print('-' * 100)
        ret = os.system(cmd)
        print('-' * 100)
        return ret

    cratis_lib_path = auto_prompt('Cratis home', 'DJANGO_GEN_CRATIS_LIB')

    # os.system('ln -s {} lib'.format(cratis_lib_path))

    os.system('pip install -e {}'.format(shlex.quote(cratis_lib_path)))

    # os.chdir('app')

    os.system('django install')

    db_exists = mysql_command('use {};'.format(db_name), supress_output=True) == 0

    if db_exists:
        recreate_db = click.confirm('Database already exist, recreate?')
    else:
        recreate_db = False

    if not db_exists or recreate_db:
        if db_exists:
            mysql_command('DROP DATABASE {};'.format(db_name))
        mysql_command('CREATE DATABASE {} CHARACTER SET utf8 COLLATE utf8_general_ci;'.format(db_name))

    os.system('django migrate')

    if not db_exists or recreate_db:
        print('-' * 100)
        print('Creating superuser')
        print('-' * 100)

        username = auto_prompt('New superuser username', 'USER', 'admin')
        email = auto_prompt('New superuser email', 'CRATIS_NEW_USER_EMAIL', 'example@example.com')

        os.system('django createsuperuser --username {} --email {}'.format(username, email))

    os.system('django-gen')

    print('\n\nOK: completed successfully')


def handle(app='all', path='data', auto=False, uml=False, rebuild=None, remove=None, init=None, *args, **kwargs):

    try:
        if init:
            if os.path.exists('app/app.py'):
                if click.confirm('There is already app.py, should we reinitialize it?', abort=True):
                    return new_project(auto=auto)
            else:
                return new_project(auto=auto)

        ror = rebuild or remove

        # django_command = sys.argv[0]
        django_command = 'django'
        if ror:

            filename = '{}.col'.format(ror)
            if not os.path.exists(filename):
                print('No such collection: {}'.format(ror))
            app_name = ror

            print('Unapplying migrations')
            subprocess.run('{} migrate {} zero'.format(django_command, app_name), shell=True, check=True)

            print('Removing migrations')
            rmtree('{}/migrations'.format(app_name))

            if rebuild:
                print('Generating new migrations')
                subprocess.run('{} makemigrations {}'.format(django_command, app_name), shell=True, check=True)

                print('Applying migrations')
                subprocess.run('{} migrate {}'.format(django_command, app_name), shell=True, check=True)

                print('Syncing translation fields')
                subprocess.run('{} sync_translation_fields_safe'.format(django_command), shell=True, check=True)

        else:
            if app == 'all':
                collections = []
                for filename in os.listdir('.'):
                    if os.path.isfile(filename) and filename.endswith('.col'):
                        if not re.match('^[a-zA-Z][a-zA-Z0-9_]+\.col$', filename):
                            print('Collection file has incorrect name: {}'.format(filename))

                        app_name = filename[0:-4]

                        collections.append(app_name)
            else:
                collections = [x.strip() for x in app.split(',')]

            for app_name in collections:
                print('Application {}'.format(app_name))

                filename = '{}.col'.format(app_name)
                if not os.path.exists('col/' + filename):
                    if not os.path.exists(filename):
                        print('File col/{filename} or {filename} do not exist'.format(filename=filename))
                        raise StopGenerator
                else:
                    filename = 'col/' + filename
                collection_set = Parser().parse_file(filename, app_name=app_name)

                generate(app_name, collection_set)

                if auto:
                    subprocess.run('{} makemigrations {}'.format(django_command, app_name), shell=True, check=True)
                    try:
                        subprocess.run('{} migrate {}'.format(django_command, app_name), shell=True, check=True)
                    except subprocess.CalledProcessError:
                        pass

                    if collection_set.translatable:
                        subprocess.run('{} sync_translation_fields_safe'.format(django_command), shell=True, check=True)

    except click.exceptions.Abort as e:
        print('Aborted.')

    except ValidationException as e:
        print(e)
        print('Generator has been stopped, due errors.')

    except StopGenerator as e:
        print(e)
        print(e.description)
        print('Generator has been stopped, due errors.')
