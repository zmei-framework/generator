import atexit
import os
import signal
import sys
from glob import glob

import click
from termcolor import colored

from genius_cli.client import GeniusClient, ApiError
from genius_cli.utils import collect_files, extract_files, collect_app_names, migrate_db, install_deps, remove_db, \
    wait_for_file_changes, run_django, run_webpack, npm_install, get_watch_paths


def run():
    api_token = os.environ.get('GENIUS_TOKEN', None)
    features_env = os.environ.get('GENIUS_FEATURES', None)

    # if not api_token:
    #     print('No genius api token. Add GENIUS_TOKEN variable to your profile.')
    #     sys.exit(1)

    genius = GeniusClient(
        api_url=os.environ.get('ZMEI_URL', 'http://ng.genius-project.io:9000/api/'),
        token=api_token,
    )

    @click.group()
    @click.option('--src', default='.', help='Sources path')
    @click.option('--dst', default='.', help='Target path')
    def cli(**args):
        pass

    @cli.command(help='Deploy to hyper.sh')
    def config(**args):
        print('Deploy!')
        pass

    @cli.command(help='Deploy to hyper.sh')
    def deploy(**args):
        print('Deploy!')

    @cli.command(help='Generate and start app')
    def up(**args):
        print('Up!')
        gen(up=True, **args)

    @cli.command(help='Run application')
    @click.option('--nodejs', is_flag=True, help='Initialize nodejs dependencies')
    @click.option('--watch', is_flag=True, help='Watch for changes')
    @click.option('--webpack', is_flag=True, help='Run webpack with reload when generation ends')
    @click.option('--port', default='8000', help='Django host:port to run on')
    @click.option('--host', default=None, help='Django host:port to run on')
    def run(**kwargs):
        print('Run!')
        gen(run=True, **kwargs)

    @cli.command(help='Just generate the code')
    @click.argument('app', nargs=-1)
    def generate(app=None, **args):
        print('generate!')
        gen(install=True, app=app or [])

    @cli.command(help='Install project dependencies')
    def install():
        print('Install!')
        gen(install=True)

    @cli.group(help='Database related commands')
    def db(**args):
        pass

    @db.command(help='Creates database migrations and apply them')
    @click.argument('app', nargs=-1)
    def migrate(app, **args):
        print('Db migrate!', app)
        gen(auto=True, app=app)

    @db.command(help='db remove + db migrate')
    @click.argument('app', nargs=-1)
    def rebuild(app, **args):
        print('Db rebuild!', app)
        gen(rebuild=True, app=app)

    @db.command(help='Rollback all the migrations')
    @click.argument('app', nargs=-1)
    def remove(app, **args):
        print('Db remove!', app)

        gen(remove=True, app=app)

    def gen(auto=False,
            src='.',
            dst='.',
            install=False,
            rebuild=False,
            remove=False,
            app=None,
            run=False,
            webpack=False,
            nodejs=False,
            host=None,
            port=8000,
            watch=False,
            up=False
            ):

        if rebuild:
            auto = True
            remove = True

        if not host:
            host = '127.0.0.1:{}'.format(port)

        if up:
            install = True
            auto = True
            watch = True
            run = True

        if not app or len(app) == 0:
            app = collect_app_names()

        src = os.path.realpath(src)
        dst = os.path.realpath(dst)

        django_process = None
        webpack_process = None

        def emergency_stop():
            if django_process:
                os.killpg(os.getpgid(django_process.pid), signal.SIGTERM)
            if webpack_process:
                os.killpg(os.getpgid(webpack_process.pid), signal.SIGTERM)

        atexit.register(emergency_stop)

        for i in wait_for_file_changes(get_watch_paths(), watch=watch):
            print('--------------------------------------------')
            print('Generating ...')
            print('--------------------------------------------')

            files = collect_files(src)

            try:
                files = genius.generate(files, collections=app)

                extract_files(dst, files)

                if up and os.path.exists('react'):
                    webpack = True
                    nodejs = True

                if nodejs and os.path.exists('react'):
                    npm_install()

                if remove:
                    remove_db(apps=app)

                if install or rebuild:
                    django_process = install_deps(django_process)

                if auto:
                    migrate_db(apps=app)

                if run and not django_process:
                    django_process = run_django(run_host=host)

                if webpack and not webpack_process:
                    webpack_process = run_webpack()

            except ApiError:
                pass

            if watch:
                print(colored('> ', 'white', 'on_blue'), 'Watching for changes...')

    cli()
