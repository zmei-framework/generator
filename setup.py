from setuptools import setup, find_packages

setup(
    name='zmei-gen',
    version='1.1.0',
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
            'templates/django/*.tpl',
            'templates/theme/*.html',
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
        'sanic',
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

