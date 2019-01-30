import atexit
import os
import signal
from pprint import pprint

import click
import pkg_resources
from termcolor import colored
from time import sleep
from zmei_generator.cli.server import zmei_generate
from zmei_generator.generator.grammar import build_parser, is_parser_declaration_changed
from zmei_generator.generator.utils import StopGenerator
from zmei_generator.parser.errors import ValidationError

from .utils import collect_files, extract_files, collect_app_names, migrate_db, install_deps, remove_db, \
    wait_for_file_changes, run_django, run_webpack, npm_install, get_watch_paths, run_celery, run_livereload, \
    flutter_install

@click.group()
def main(**args):
    pass


def run_command(cmd, show=False):
    print(cmd)
    if not show:
        os.system(cmd)


@main.group()
@click.option('--debug-port', default=None, help='Connect to pydevd port')
@click.option('--src', default='.', help='Sources path')
@click.option('--dst', default='.', help='Target path')
def gen(debug_port, **args):

    if debug_port:
        import pydevd
        pydevd.settrace('localhost', port=int(debug_port), stdoutToServer=True, stderrToServer=True)

    # ensure_logged_in()
    pass


@main.command(help='Generate parser definition')
def build():
    build_parser()


@gen.command(help='Generate and start app')
@click.option('--port', default='8000', help='Django host:port to run on')
@click.option('--ip', default='127.0.0.1', help='Django host:port to run on')
@click.option('--public', is_flag=True, help='Run django on 0.0.0.0')
@click.option('--live', default=False, is_flag=True, help='Reload browser on changes')
@click.option('--celery', default=False, is_flag=True, help='Run with celery')
def up(**args):
    gen(up=True, **args)


@gen.command(help='Run application')
@click.option('--nodejs', is_flag=True, help='Initialize nodejs dependencies')
@click.option('--celery', is_flag=True, help='Run celery worker & beat')
@click.option('--watch', is_flag=True, help='Watch for changes')
@click.option('--webpack', is_flag=True, help='Run webpack with reload when generation ends')
@click.option('--port', default='8000', help='Django host:port to run on')
@click.option('--ip', default=None, help='Django host:port to run on')
@click.option('--public', is_flag=True, help='Run django on 0.0.0.0')
def app_run(**kwargs):
    gen(run=True, **kwargs)


@gen.command(help='Just generate the code')
@click.argument('app', nargs=-1)
@click.option('--public', is_flag=True, help='Run django on 0.0.0.0')
def generate(app=None, **args):
    gen(app=app or [], **args)


@gen.command(help='Install project dependencies')
def install():
    gen(install=True)


@gen.group(help='Database related commands')
def db(**args):
    pass


@db.command(help='Creates database migrations and apply them')
@click.argument('app', nargs=-1)
def migrate(app, **args):
    gen(auto=True, app=app)


@db.command(help='db remove + db migrate')
@click.argument('app', nargs=-1)
def rebuild(app, **args):
    gen(rebuild=True, app=app)


@db.command(help='Rollback all the migrations')
@click.argument('app', nargs=-1)
def remove(app, **args):
    gen(remove=True, app=app)


def gen(auto=False,
        src='.',
        dst='.',
        install=False,
        rebuild=False,
        remove=False,
        app=None,
        run=False,
        live=False,
        webpack=False,
        nodejs=False,
        celery=False,
        public=None,
        ip=None,
        port=8000,
        watch=False,
        up=False
        ):

    if rebuild:
        auto = True
        remove = True

    if public:
        try:
            import socket
            s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
            s.connect(("8.8.8.8", 80))
            ip = s.getsockname()[0]
            s.close()

        except Exception as e:
            print(f'Can not run on public port: {e}')
            return

    elif not ip:
        ip = '127.0.0.1'

    host = '{}:{}'.format(ip, port)

    os.environ.setdefault('ZMEI_SERVER_IP', str(ip))
    os.environ.setdefault('ZMEI_SERVER_PORT', str(port))
    os.environ.setdefault('ZMEI_SERVER_HOST', str(host))

    if up:
        install = True
        auto = True
        watch = True
        run = True

    if not app or len(app) == 0:
        app = collect_app_names()

    # Generate parser if something new is installed
    if is_parser_declaration_changed():
        if not build_parser():
            print('Can not generate parser definition, sorry.')
            return

    src = os.path.realpath(src)
    dst = os.path.realpath(dst)

    livereload_process = None
    django_process = None
    webpack_process = None
    celery_process = None

    def emergency_stop():
        if livereload_process:
            os.killpg(os.getpgid(livereload_process.pid), signal.SIGTERM)
        if django_process:
            os.killpg(os.getpgid(django_process.pid), signal.SIGTERM)
        if webpack_process:
            os.killpg(os.getpgid(webpack_process.pid), signal.SIGTERM)
        if celery_process:
            os.killpg(os.getpgid(celery_process.pid), signal.SIGTERM)

        sleep(1)
        print('\n')

    atexit.register(emergency_stop)

    for i in wait_for_file_changes(get_watch_paths(), watch=watch):
        print('--------------------------------------------')
        print('Generating ...')
        print('--------------------------------------------')

        files = collect_files(src)


        try:
            files = zmei_generate(files, models=app)
        except (NotImplementedError, ValidationError) as e:
            print(e)
            continue

        except StopGenerator as e:
            print(e.description)
            continue

        changed = extract_files(dst, files)

        if up and os.path.exists('react'):
            webpack = True
            nodejs = True

        if nodejs and os.path.exists('react'):
            npm_install()

        if remove:
            remove_db(apps=app)

        if install or rebuild:
            django_process = install_deps(django_process)

        if os.path.exists('flutter'):
            flutter_install()

        if auto and (changed.models or not django_process):
            migrate_db(apps=app)

        if run and live and not livereload_process:
            livereload_process = run_livereload()

        if run and not django_process:
            django_process = run_django(run_host=host)

        # if webpack and not webpack_process:
        #     webpack_process = run_webpack()

        if celery:
            # restart celery process on changes
            if celery_process:
                os.killpg(os.getpgid(celery_process.pid), signal.SIGTERM)

            celery_process = run_celery()

        if watch:
            print(colored('> ', 'white', 'on_blue'), 'Watching for changes...')


def run():
    main()
