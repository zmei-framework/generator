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
    def cli():
        pass

    @click.command()
    @click.option('--auto', is_flag=True, help='Generate and run migrations')
    @click.option('--install', is_flag=True, help='Install dependencies')
    @click.option('--watch', is_flag=True, help='Watch for changes')
    @click.option('--up', is_flag=True, help='--with=django_process + --install + --auto + --watch + --run')
    @click.option('--run', is_flag=True, help='Run django_process with reload when generation ends')
    @click.option('--webpack', is_flag=True, help='Run webpack with reload when generation ends')
    @click.option('--nodejs', is_flag=True, help='Initialize nodejs dependencies')
    @click.option('--port', default='8000', help='Django host:port to run on')
    @click.option('--host', default=None, help='Django host:port to run on')
    @click.option('--rebuild', help='Rebuild application migrations')
    @click.option('--remove', help='Remove application migrations')
    @click.option('--full-clean', is_flag=True, help='Remove everything except col files')
    @click.option('--src', default='.', help='Sources path')
    @click.option('--dst', default='.', help='Target path')
    @click.option('--name', help='Request name (for debug purposes)')
    @click.option('--with', default='', help='Extra features to use (coma separated)')
    @click.argument('app', nargs=-1)
    def gen(auto, src, dst, name, install, rebuild, remove, app, run, webpack, nodejs, host, port, watch, up,
            full_clean,
            **kwargs):

        if rebuild:
            auto = True
            remove = True

        if not host:
            host = '127.0.0.1:{}'.format(port)

        features = kwargs.get('with', features_env)

        if not features:
            features = []
        else:
            features = features.split(',')

        if up:
            install = True
            auto = True
            watch = True
            run = True

        if len(app) == 0:
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
                files = genius.generate(files, name=name, collections=app, features=features)

                extract_files(dst, files)

                if up and os.path.exists('react'):
                    webpack = True
                    nodejs = True

                if nodejs and os.path.exists('react'):
                    npm_install()

                if remove:
                    remove_db(apps=app, features=features)

                if install or rebuild:
                    django_process = install_deps(django_process)

                if auto:
                    migrate_db(apps=app, features=features)

                if run and not django_process:
                    django_process = run_django(features=features, run_host=host)

                if webpack and not webpack_process:
                    webpack_process = run_webpack()

            except ApiError:
                pass

            if watch:
                print(colored('> ', 'white', 'on_blue'), 'Watching for changes...')

    gen()


