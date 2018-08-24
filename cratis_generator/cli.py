import string

import random

import shlex

import argparse
import os
import re

from dateutil.tz import tzlocal

from .config.domain import ValidationException
from .config.parser import Parser
from .generator.collections import generate, generate_common_files
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


def handle(app='all', auto=False, rebuild=None, remove=None, *args, **kwargs):

    try:
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

            all_apps = {}
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

                generate(app_name, collection_set, features=['cratis'])

                all_apps[app_name] = collection_set

                if auto:
                    subprocess.run('{} makemigrations {}'.format(django_command, app_name), shell=True, check=True)
                    try:
                        subprocess.run('{} migrate {}'.format(django_command, app_name), shell=True, check=True)
                    except subprocess.CalledProcessError:
                        pass

                    if collection_set.translatable:
                        subprocess.run('{} sync_translation_fields_safe'.format(django_command), shell=True, check=True)

            generate_common_files(apps=all_apps, features=['cratis'])

    except click.exceptions.Abort as e:
        print('Aborted.')

    except ValidationException as e:
        print(e)
        print('Generator has been stopped, due errors.')

    except StopGenerator as e:
        print(e)
        print(e.description)
        print('Generator has been stopped, due errors.')
