from setuptools import setup, find_packages

setup(
    name='zmei-cli',
    version='1.2.2',
    packages=find_packages(),

    url='',
    license='Private',
    author='Alex Rudakov',
    author_email='alex@negative.ee',
    description='Genius generator.',
    long_description='',

    install_requires=[
        'click',
        'requests',
        'termcolor',
        'terminaltables',
        'PyYaml',
        'PyJWT',
    ],

    entry_points={
        'console_scripts': [
            'zmei = zmei_cli.main:run',
        ]
    },
)

