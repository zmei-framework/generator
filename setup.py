from setuptools import setup, find_packages

setup(
    name='cratis-gen',
    version='1.0.22',
    packages=find_packages(),

    url='',
    license='Private',
    author='Alex Rudakov',
    author_email='ribozz@gmail.com',
    description='Cratis generator.',
    long_description='',

    package_data={
        'zmei_generator': [
            'templates/*.tpl',
            'templates/cratis/*.tpl',
            'templates/django/*.tpl',
            'templates/theme/*.html',
        ]
    },

    install_requires=[
        "termcolor",
        "markdown",
        "autopep8",
        "django",
        'pip>8.0.0',
        'tree-format',
        'python-dateutil',
        'wheel',
        'click',
        'jinja2',
        'sanic',
        'termcolor==1.1.0',
        'autopep8',
        'jinja2',
        'pyjwt',
        'defusedxml',
        'django',
        'antlr4-python3-runtime',
        'AoikLiveReload',
        'aioelasticsearch',
    ],

    entry_points={
        'console_scripts': [
            'zmei = zmei_generator.cli:django_gen',
        ]
    },
)

