import os
from glob import glob

from setuptools import setup, find_packages


def find_package_data(*allowed_extensions):
    package_data = {}

    for ext in allowed_extensions:
        for file in glob(f'**/*.{ext}', recursive=True):
            pos = -1
            parts = file.split('/')
            while True:
                prefix = '/'.join(parts[0:pos])
                package = '.'.join(parts[0:pos])
                data_file = '/'.join(parts[pos:])

                if prefix == '':
                    break

                if os.path.exists(os.path.join(prefix, '__init__.py')):
                    break

                pos -= 1

            if prefix != '':
                if package not in package_data:
                    package_data[package] = []

                package_data[package].append(data_file)

    return package_data


setup(
    name='zmei-cli',
    version='2.1.8',
    packages=find_packages(),

    url='',
    license='GPLv3',
    author='Alex Rudakov',
    author_email='ribozz@gmail.com',
    description='Zmei-generator',
    long_description='',

    package_data=find_package_data('g4', 'jar', 'tpl', 'html'),

    install_requires=[
        "markdown",
        "readchar",
        "autopep8",
        "django",
        'pip>8.0.0',
        'tree-format',
        'python-dateutil',
        'wheel',
        'click',
        'jinja2',
        'termcolor==1.1.0',
        'jinja2',
        'defusedxml',
        'django',
        'antlr4-python3-runtime'
    ],

    entry_points={
        'console_scripts': [
            'zmei = zmei_generator.cli.main:run'
        ],
        'zmei.grammar.tokens': [
            'zmei_docker = zmei_generator.contrib.docker.grammar.tokens:tokens',
            'zmei_gitlab = zmei_generator.contrib.gitlab.grammar.tokens:tokens',
            'zmei_web = zmei_generator.contrib.web.grammar.tokens:tokens',
            'zmei_admin = zmei_generator.contrib.admin.grammar.tokens:tokens',
            'zmei_drf = zmei_generator.contrib.drf.grammar.tokens:tokens',
            'zmei_filer = zmei_generator.contrib.filer.grammar.tokens:tokens',
            'zmei_celery = zmei_generator.contrib.celery.grammar.tokens:tokens',
            'zmei_react = zmei_generator.contrib.react.grammar.tokens:tokens',
            'zmei_channels = zmei_generator.contrib.channels.grammar.tokens:tokens'
        ],
        'zmei.grammar.keywords': [
            'zmei_web = zmei_generator.contrib.web.grammar.tokens:keywords',
            'zmei_drf = zmei_generator.contrib.drf.grammar.tokens:keywords',
        ],
        'zmei.grammar.pages': [
            'zmei_docker = zmei_generator.contrib.docker.grammar.struct:pages',
            'zmei_gitlab = zmei_generator.contrib.gitlab.grammar.struct:pages',
            'zmei_web = zmei_generator.contrib.web.grammar.struct:pages',
            'zmei_admin = zmei_generator.contrib.admin.grammar.struct:pages',
            'zmei_drf = zmei_generator.contrib.drf.grammar.struct:pages',
            'zmei_filer = zmei_generator.contrib.filer.grammar.struct:pages',
            'zmei_celery = zmei_generator.contrib.celery.grammar.struct:pages',
            'zmei_react = zmei_generator.contrib.react.grammar.struct:pages',
            'zmei_channels = zmei_generator.contrib.channels.grammar.struct:pages'
        ],
        'zmei.grammar.models': [
            'zmei_docker = zmei_generator.contrib.docker.grammar.struct:models',
            'zmei_gitlab = zmei_generator.contrib.gitlab.grammar.struct:models',
            'zmei_web = zmei_generator.contrib.web.grammar.struct:models',
            'zmei_admin = zmei_generator.contrib.admin.grammar.struct:models',
            'zmei_drf = zmei_generator.contrib.drf.grammar.struct:models',
            'zmei_filer = zmei_generator.contrib.filer.grammar.struct:models',
            'zmei_celery = zmei_generator.contrib.celery.grammar.struct:models',
            'zmei_react = zmei_generator.contrib.react.grammar.struct:models',
            'zmei_channels = zmei_generator.contrib.channels.grammar.struct:models'
        ],
        'zmei.grammar.app': [
            'zmei_docker = zmei_generator.contrib.docker.grammar.struct:application',
            'zmei_gitlab = zmei_generator.contrib.gitlab.grammar.struct:application',
            'zmei_web = zmei_generator.contrib.web.grammar.struct:application',
            'zmei_admin = zmei_generator.contrib.admin.grammar.struct:application',
            'zmei_drf = zmei_generator.contrib.drf.grammar.struct:application',
            'zmei_filer = zmei_generator.contrib.filer.grammar.struct:application',
            'zmei_celery = zmei_generator.contrib.celery.grammar.struct:application',
            'zmei_react = zmei_generator.contrib.react.grammar.struct:application',
            'zmei_channels = zmei_generator.contrib.channels.grammar.struct:application'
        ],
        'zmei.parser.stage1': [
            'zmei_web = zmei_generator.contrib.web.parsers.all_stage1:parsers',
            'zmei_admin = zmei_generator.contrib.admin.parsers.all_stage1:parsers',
            'zmei_channels = zmei_generator.contrib.channels.parsers.all_stage1:parsers'
        ],
        'zmei.parser.stage2': [
            'zmei_web = zmei_generator.contrib.web.parsers.all_stage2:parsers'
        ],
        'zmei.parser.stage3': [
            'zmei_web = zmei_generator.contrib.web.parsers.all_stage3:parsers',
            'zmei_channels = zmei_generator.contrib.channels.parsers.all_stage3:parsers'
        ],
        'zmei.generator': [
            'zmei_web_common = zmei_generator.contrib.web.generator.common:generate',
            'zmei_web_models = zmei_generator.contrib.web.generator.models:generate',
            'zmei_web_translation = zmei_generator.contrib.web.generator.translation:generate',
            'zmei_web_views = zmei_generator.contrib.web.generator.views:generate',

            'zmei_docker_docker = zmei_generator.contrib.docker.generator.docker:generate',
            'zmei_gitlab_gitlab = zmei_generator.contrib.gitlab.generator.gitlab:generate',
            'zmei_admin_admin = zmei_generator.contrib.admin.generator.admin:generate',
            'zmei_drf_serializers = zmei_generator.contrib.drf.generator.serializers:generate',
            'zmei_react_react = zmei_generator.contrib.react.generator.react:generate',
            'zmei_channels_channels = zmei_generator.contrib.channels.generator.channels:generate'
        ],

        'zmei.templates': [
            'zmei_docker = zmei_generator.contrib.docker.templates',
            'zmei_gitlab = zmei_generator.contrib.gitlab.templates',
            'zmei_web = zmei_generator.contrib.web.templates',
            'zmei_admin = zmei_generator.contrib.admin.templates',
            'zmei_drf = zmei_generator.contrib.drf.templates',
            'zmei_celery = zmei_generator.contrib.celery.templates',
            'zmei_react = zmei_generator.contrib.react.templates',
            'zmei_channels = zmei_generator.contrib.channels.templates',
            'zmei_theme_bluma = zmei_generator.contrib.themes.bluma.templates',
            'zmei_theme_default = zmei_generator.contrib.themes.default.templates',
        ]

    }
)
