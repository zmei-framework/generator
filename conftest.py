from subprocess import Popen

import os
from pytest_boxed import forked_run_report
from shutil import rmtree, copy

import pytest

# from django.core.management import call_command
# from pytest_forked import forked_run_report

from cratis_generator.config.parser import Parser
from cratis_generator.generator.collections import generate

samples_dir = os.path.join(os.path.dirname(__file__), 'tests/samples')
work_dir_prefix = os.path.join(os.path.dirname(__file__), 'tests/gen_result')
files_dir = os.path.join(os.path.dirname(__file__), 'tests/files')


def pytest_sessionstart(session):
    if os.path.exists(work_dir_prefix):
        rmtree(work_dir_prefix)
    os.mkdir(work_dir_prefix)


def pytest_addoption(parser):
    parser.addoption("--django-gen", action="store_true", help="only run tests that are market with col().")


def pytest_configure(config):
    config.addinivalue_line("markers",
                            "django_gen(collection_name): test requires generated django application from .col file")


def pytest_runtest_teardown(item):
    os.chdir('/Users/alex/dev/cratis-cmp/lib/_gen')


def pytest_runtest_setup(item):
    import sys
    import os

    before = item.get_marker("django_gen_before")
    if before:
        commands_before = before.args
    else:
        commands_before = []

    colmarker = item.get_marker("django_gen")
    django_gen = item.config.getoption("--django-gen")

    if django_gen and not colmarker:
        pytest.skip("Running only django-gen tests")

    if colmarker:
        os.environ['DJANGO_SETTINGS_MODULE'] = 'app'
        os.environ['APP'] = 'Dev'

        # prepare workdir
        work_dir = os.path.join(work_dir_prefix, item.name)
        if os.path.exists(work_dir):
            rmtree(work_dir)
        os.mkdir(work_dir)

        collection_set_name = colmarker.args[0]
        if len(colmarker.args) > 1:
            collection_set = Parser().parse_config(colmarker.args[1], app_name=collection_set_name)
        else:
            col_file = '{}/{}.col'.format(samples_dir, collection_set_name)
            collection_set = Parser().parse_file(col_file, app_name=collection_set_name)

        with open('{}/app.py.tpl'.format(files_dir)) as src:
            with open('{}/app.py'.format(work_dir), 'w+') as dst:
                dst.write(src.read().format(name=collection_set_name, class_name=collection_set_name.capitalize()))

        copy('{}/dev.db'.format(files_dir), '{}/dev.db'.format(work_dir, collection_set_name))

        os.chdir(work_dir)
        generate(collection_set_name, collection_set)

        sys.path.append(work_dir)

        import django
        django.setup()

        for command in commands_before:
            if command == 'migrate':
                call_django_command('makemigrations {}'.format(collection_set_name), work_dir)

            call_django_command(command, work_dir)


def call_django_command(django_command, work_dir):
    import sys
    from cratis import cli
    cmd = cli.__file__
    env = os.environ.copy()

    env.update({
        "PYTHONPATH": ":".join([x for x in sys.path if x != '']),
    })
    # print(os.environ)
    p1 = Popen([sys.executable, cmd] + django_command.split(' '), env=env, cwd=work_dir)
    p1.wait()


#


@pytest.mark.tryfirst
def pytest_runtest_protocol(item):
    colmarker = item.get_marker("django_gen")

    if colmarker:
        reports = forked_run_report(item)
        for rep in reports:
            item.ihook.pytest_runtest_logreport(report=rep)
        return True

# def pytest_runtest_setup(item):
#     envmarker = item.get_marker("env")
#     if envmarker is not None:
#         envname = envmarker.args[0]
#         if envname != item.config.getoption("-E"):
#             pytest.skip("test requires env %r" % envname)
#
