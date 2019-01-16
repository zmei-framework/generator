from setuptools import setup, find_packages

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

    package_data={
        'zmei_generator': [
            'templates/*.tpl',
            'templates/django/*.tpl',
            'templates/docker/*.tpl',
            'templates/gitlab/*.tpl',
            'templates/theme/*.html',
        ],
        'zmei_generator.parser.gen': [
            '*.interp',
            '*.tokens',
        ]
    },

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
        ]
    },
)

