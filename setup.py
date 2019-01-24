from glob import glob

from setuptools import setup, find_packages

prefix = 'zmei_generator/contrib/'
suffix = '/grammar'
extensions = [x[len(prefix):-len(suffix)] for x in glob(f'{prefix}*{suffix}')]

setup(
    name='zmei-cli',
    version='2.0.11',
    packages=find_packages(),

    url='',
    license='GPLv3',
    author='Alex Rudakov',
    author_email='ribozz@gmail.com',
    description='Zmei-generator',
    long_description='',

    install_requires=[
        "markdown",
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
            'zmei = zmei_generator.cli.main:run',
        ],
        'zmei.grammar.tokens': [f'zmei_{x} = zmei_generator.contrib.{x}.grammar.tokens:tokens' for x in extensions],
        'zmei.grammar.keywords': [f'zmei_{x} = zmei_generator.contrib.{x}.grammar.tokens:keywords' for x in extensions],

        'zmei.grammar.pages': [f'zmei_{x} = zmei_generator.contrib.{x}.grammar.struct:pages' for x in extensions],
        'zmei.grammar.models': [f'zmei_{x} = zmei_generator.contrib.{x}.grammar.struct:models' for x in extensions],
        'zmei.grammar.cs': [f'zmei_{x} = zmei_generator.contrib.{x}.grammar.struct:collection_set' for x in extensions],


        'zmei.parser.stage1': [
            f'zmei_web = zmei_generator.contrib.web.parsers.all_stage1:parsers'
        ],
    },
)

