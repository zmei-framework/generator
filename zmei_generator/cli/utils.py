import _thread
import hashlib
import io
import json
import os
import re
import signal
import subprocess
import sys
import threading
import zipfile

from contextlib import contextmanager
from difflib import Differ
from glob import glob
from io import BytesIO
from select import select

import click
import readchar
from itertools import chain
from shutil import rmtree

from termcolor import colored
from time import sleep


@contextmanager
def chdir(path):
    cwd = os.getcwd()
    os.chdir(path)
    yield
    os.chdir(cwd)


PACKAGE_JSON_TOKEN = '__generated__'


def expand__files_json(file_mapping):
    realpath = os.getcwd()
    for record in file_mapping:
        if record['kind'] == 'file':
            pathname = os.path.realpath(record['path'])
            if not pathname.startswith(realpath):
                print(colored(f"Attempt to write file out of working "
                              f"directory: {record['path']}", 'white', 'on_red'), ' ')
                return

            if not os.path.exists(pathname):
                with open(pathname, 'w') as f:
                    f.write(record['source'])
                    print(colored(' + ', 'blue', 'on_green'), ' ', record['path'])

            yield record['path']

        else:
            print(colored(f"Unsupported file record: {record['kind']}", 'red', 'on_yellow'), ' ')


def write_generated_file(path, source):
    # special hack for settings.py->SECRET_KEY
    if path.endswith('app/_settings.py'):
        if os.path.exists(path):
            with open(path, 'r') as f:
                found = re.search('^SECRET_KEY\s*=.*$', f.read(), flags=re.MULTILINE)
                if found:
                    current_key = found.group(0)
                    new_key = re.search('^\s*SECRET_KEY\s*=.*$', source, flags=re.MULTILINE).group(0)
                    source = source.replace(new_key, current_key)

    dirname = os.path.dirname(path)
    if dirname and len(dirname) and not os.path.exists(dirname):
        os.makedirs(dirname)

    chksum = source_hash(source)

    tag = f"generated: {chksum}"

    source_prefix = ''

    if path.endswith('.py') or path.endswith('.yaml') or path.endswith('.yml') or path.endswith('_requirements.txt')\
            or path.endswith('requirements.prod.txt') or path.endswith('Dockerfile') or path.endswith('nginx.conf') \
            or path.endswith('.ini'):
        # settings.py is specially designed to be overriden
        if not path.endswith('app/settings.py') \
                and not path.endswith('app/tasks.py') \
                and not path.endswith('app/urls.py'):
            source_prefix = f"# {tag}\n\n"

    elif path.endswith('.js') or path.endswith('.jsx') or path.endswith('.dart'):
        source_prefix = f"//# {tag}\n\n"

    elif path.endswith('.md'):
        source_prefix = f"<!-- # {tag} -->\n\n"

    elif path.endswith('package.json'):
        chksum = source_hash(json.dumps(json.loads(source), indent=4))
        source = json.dumps({**json.loads(source), **{PACKAGE_JSON_TOKEN: chksum}}, indent=4)

    elif ('/templates/' in path or '/themes/' in path) and path.endswith('.html'):
        source_prefix = f"{{# {tag} #}}\n\n"

    if os.path.exists(path):
        real_source, generated, changed, file_checksum = is_generated_file(path)

        if generated:
            if changed:
                if sys.stdout.isatty():
                    parts = path.split('/')
                    print_path = colored(' ? ', 'white', 'on_red') + '   ' + '/'.join(parts[:-1]) + '/'
                    print_path += colored(parts[-1], 'yellow')

                    valid = False
                    answer = None
                    while not valid:
                        print(f'{print_path}\nFile is modified. Should I remove "generated" marker? \n'
                              f'(o = overwrite, d = show diff, a = abort, i = ignore, y = remove marker) [i]: ', end='')
                        answer = readchar.readchar()
                        if answer == 'd':
                            for line in Differ().compare(
                                real_source.splitlines(keepends=True),
                                source.splitlines(keepends=True)
                            ):
                                if line[0] in ('+', '-'):
                                    line = {'+': colored(line, 'green'), '-': colored(line, 'red')}[line[0]]

                                sys.stdout.write(line)

                        valid = answer in ['o', 'i', 'y']

                        if answer == 'a' or ord(answer) in (3, 4):
                            raise KeyboardInterrupt

                        if answer.strip() == '':
                            answer = 'i'
                            valid = True

                        if not valid and answer != 'd':
                            print(ord(answer))
                            print('Invalid input.')
                        print('\n')

                    if answer == 'o':
                        pass  # overwrite
                    elif answer == 'y':
                        source = real_source
                        source_prefix = ''
                    else:
                        return
                else:
                    print(colored(' ! ', 'white', 'on_red'), ' ', path)
                    return

            else:
                if file_checksum == chksum:
                    return  # already up to date
        else:
            # print(f'skip: {path}')
            return  # file intentionally overridden. Do not overwrite!

    if not os.path.exists(path):
        print(colored(' + ', 'blue', 'on_green'), ' ', path)
    else:
        print(colored(' ~ ', 'blue', 'on_cyan'), ' ', path)
    with open(path, 'w') as f:
        if source_prefix:
            f.write(source_prefix)
        f.write(source)
        # print(f'write: {path}')

    return True


def is_generated_file(path):
    """
    Checks if file is generated, and is it changed
    :param path:

    :return: real_source, generated, changed, checksum
    """
    with open(path, 'r') as f:
        content = f.read()

    if path.endswith('package.json'):
        try:
            data = json.loads(content)
        except Exception as e:
            print('Can not read package.json. That\'s shouldn\'t happen as file is auto-generated.', e)
            data = {}

        try:
            file_chk_expected = data[PACKAGE_JSON_TOKEN]
        except KeyError:
            return content, False, False, None

        data = json.loads(content)
        if PACKAGE_JSON_TOKEN in data:
            del data[PACKAGE_JSON_TOKEN]
        real_source = json.dumps(data, indent=4)

    else:
        match = re.match('^(<!--\s*)?({|//)?# generated: ([a-f0-9]{32})( #})?(\s*-->)?\n\n', content)
        if not match:
            return content, False, False, None

        file_chk_expected = match.group(3)
        real_source = content[len(match.group(0)):]

    file_chk_real = source_hash(real_source)

    if file_chk_expected != file_chk_real:
        return real_source, True, True, file_chk_real  # checksum failed. Changed by hands?
    else:
        return real_source, True, False, file_chk_real


def source_hash(source):
    hash_md5 = hashlib.md5()
    source = source.strip()
    hash_md5.update(source.encode())

    return hash_md5.hexdigest()


def copy_generated_tree(source_path, target_path, glob_expr="**/*"):
    files = []

    with chdir(source_path):
        for file in glob(glob_expr, recursive=True):
            with open(file, 'r') as f:
                files.append((file, f.read()))

    with chdir(target_path):
        for path, source in files:
            write_generated_file(path, source)


def clean_up_generated_files(path, file_list, remove_root=False):
    for file in os.listdir(path):
        if file.startswith('.'):
            continue

        if file == 'node_modules':
            continue

        fullpath = os.path.join(path, file)

        if os.path.isdir(fullpath):
            clean_up_generated_files(fullpath, file_list, remove_root=True)
        else:
            if file[0] != '.' and file.split('.')[-1] in ('js', 'jsx', 'py', 'html', 'dart'):
                real_source, generated, changed, file_checksum = is_generated_file(fullpath)

                if generated and (fullpath not in file_list):
                    if changed:
                        print(colored('skip:', 'red', 'on_yellow'), ' ', fullpath)
                    else:
                        print(colored(' - ', 'white', 'on_red'), ' ', fullpath)
                        os.unlink(fullpath)

    if len(os.listdir(path)) == 0 and remove_root:
        os.rmdir(path)
        print(colored('delete:', 'white', 'on_red'), ' ', path)


class FileChangeSet(object):
    def __init__(self):
        self.changed_files = []
        self.models = False
        self.templates = False
        self.requirements = False
        self.other = False

    def append(self, path):
        req_file = os.environ.get('ZMEI_REQUIREMENTS_FILE', 'requirements.txt')
        self.changed_files.append(path)

        if path.endswith('models.py'):
            self.models = True
            return

        if path.endswith('.html'):
            self.templates = True
            return

        # both 'requirements.txt' and '_requirements.txt'
        if path.endswith(req_file):
            self.requirements = True
            return

        self.other = True


def extract_files(dst, file_bytes):
    req_file = os.environ.get('ZMEI_REQUIREMENTS_FILE', 'requirements.txt')

    changed_files = FileChangeSet()

    files = zipfile.ZipFile(BytesIO(file_bytes), mode='r', compression=zipfile.ZIP_LZMA)

    file_mapping = None

    for path in files.namelist():
        if path == 'requirements.txt':
            path = req_file

        if path == '__files.json':
            file_mapping = json.loads(files.read(path).decode())
            continue

        full_path = os.path.join(dst, path)
        if write_generated_file(full_path, files.read(path).decode()):
            changed_files.append(full_path)

    file_list = [f"./{x}" for x in files.namelist()]
    if file_mapping:
        file_list += [f"./{x}" for x in expand__files_json(file_mapping)]

    clean_up_generated_files('.', file_list)

    return changed_files


def collect_files(src):
    with chdir(src):
        f = io.BytesIO()
        files = zipfile.ZipFile(f, mode='w', compression=zipfile.ZIP_LZMA)

        for path in get_collect_paths():
            real_source, generated, changed, checksum = is_generated_file(path)

            if not generated or changed:
                files.write(path)
        files.close()

        f.seek(0)

    return f.getvalue()


def get_collect_paths():
    paths = []
    paths += list(glob('*.col'))
    paths += list(glob('col/*.col'))
    paths += list(glob('col/**/*.col', recursive=True))
    # paths += list(glob('react/src/**/*.jsx', recursive=True))
    # paths += list(glob('react/*.js'))
    # paths += list(glob('react/*.json'))

    return set(paths)


def get_watch_paths():
    paths = []
    paths += list(glob('*.col'))
    paths += list(glob('col/*.col'))
    paths += list(glob('col/**/*.col', recursive=True))
    paths += list(glob('col/**/*.html', recursive=True))
    # paths += list(glob('react/src/**/*.js', recursive=True))
    # paths += list(glob('react/src/**/*.jsx', recursive=True))
    # paths += list(glob('react/*.js'))
    paths += list(glob('react/*.json'))

    return set(paths)


def collect_app_names():
    models = []

    for filename in get_collect_paths():
        if os.path.isfile(filename) and filename.endswith('.col'):
            if not re.match('^(col/)?[a-zA-Z][a-zA-Z0-9_]+\.col$', filename):
                print('Model file has incorrect name: {}'.format(filename))
            if filename.startswith('col/'):
                filename = filename[4:]
            app_name = filename[0:-4]

            models.append(app_name)
    return models


def migrate_db(apps, features=None):
    print(colored('> ', 'white', 'on_blue'), 'Migrating database')
    django_command = get_django_command(features)

    db_apps = [app for app in apps if os.path.exists(f'{app}/models.py')]

    try:
        subprocess.run('{} makemigrations {}'.format(django_command, ' '.join(db_apps)), shell=True, check=True)
    except subprocess.CalledProcessError:
        pass

    try:
        subprocess.run('{} migrate'.format(django_command), shell=True, check=True)
    except subprocess.CalledProcessError:
        pass


def run_django(features=None, run_host='127.0.0.1:8000'):
    print(colored('> ', 'white', 'on_blue'), 'Starting django')

    if os.path.exists('flutter/'):
        if run_host.startswith('127.0.0.1:'):
            print(colored('NB! you have a flutter application, but running django on a '
                          f'local interface {run_host}. Flutter application is '
                          f'not able to connect to api! use "--public": zmei gen up --public', 'white', 'on_red'))
        else:
            print(colored(f'Flutter api is accessible on {run_host}. Make sure to connect '
                          f'phone to the same wifi network as your computer, if running on a real device.', 'white',
                          'on_blue')),

    django_command = get_django_command(features, )
    options = ''
    if os.path.exists('app/settings_dev.py'):
        options = ' --settings app.settings_dev'

    full_command = '{} runserver {}{}'.format(django_command, run_host, options)
    print(full_command)
    return subprocess.Popen(full_command, preexec_fn=os.setsid, shell=True)


def run_livereload():
    if not os.path.exists('app/settings_dev.py'):
        with open('app/settings_dev.py', 'w') as f:
            f.write("""
from .settings import *

INSTALLED_APPS += [
    'livereload',
]

MIDDLEWARE += [
    'livereload.middleware.LiveReloadScript',
]
            """)

    os.system('pip install django-livereload-server')

    print(colored('> ', 'white', 'on_blue'), 'Starting livereload server')
    return subprocess.Popen('python manage.py livereload --settings app.settings_dev', preexec_fn=os.setsid, shell=True)


def run_webpack():
    print(colored('> ', 'white', 'on_blue'), 'Starting webpack')

    webpack_command = './node_modules/.bin/webpack -w'
    print(webpack_command)
    return subprocess.Popen('{}'.format(webpack_command), shell=True, cwd='react', preexec_fn=os.setsid)


def run_celery():
    print(colored('> ', 'white', 'on_blue'), 'Starting celery')

    webpack_command = 'celery -A app worker -B -E -l info'
    print(webpack_command)
    return subprocess.Popen('{}'.format(webpack_command), shell=True, preexec_fn=os.setsid)


def npm_install():
    if is_req_file_changed('react/package.json'):
        print(colored('> ', 'white', 'on_blue'), 'Installing nodejs dependencies ...')
        cmd = 'npm install'
        print(cmd)
        if subprocess.run('{}'.format(cmd), shell=True, cwd='react', check=True):
            mark_req_file_installed('react/package.json')


def flutter_install():
    if not os.path.exists('flutter/.metadata'):
        os.system('flutter create --project-name app flutter/')


def remove_db(apps, features=None):
    django_command = get_django_command(features)

    for app_name in apps:
        if not os.path.exists(f'{app_name}/migrations'):
            continue

        filename = '{}.col'.format(app_name)
        if not os.path.exists(filename):
            print('No such model: {}'.format(app_name))
        app_name = app_name

        print(colored('> ', 'white', 'on_blue'), 'Unapplying migrations')
        subprocess.run('{} migrate {} zero'.format(django_command, app_name), shell=True, check=True)

        print(colored('> ', 'white', 'on_blue'), 'Removing migrations')
        rmtree('{}/migrations'.format(app_name))


def get_django_command(features):
    django_command = 'python manage.py'
    return django_command


def is_req_file_changed(filename):
    hash = files_hash([filename])
    cache_filename = f'.zmei-cache/{filename}'
    if os.path.exists(cache_filename):
        with open(cache_filename) as f:
            stored_hash = f.read()
            if stored_hash == hash:
                return False
    return True


def mark_req_file_installed(filename):
    hash = files_hash([filename])
    cache_filename = f'.zmei-cache/{filename}'

    dirname = os.path.dirname(cache_filename)
    if not os.path.exists(dirname):
        os.makedirs(dirname)

    with open(cache_filename, 'w') as f:
        f.write(hash)


def install_deps(django_process):
    req_file = os.environ.get('ZMEI_REQUIREMNETS_FILE', 'requirements.txt')
    if is_req_file_changed(req_file) or is_req_file_changed('_requirements.txt'):
        if django_process:
            os.killpg(os.getpgid(django_process.pid), signal.SIGTERM)
            django_process = None

        print(colored('> ', 'white', 'on_blue'), 'Installing pip dependencies...')
        if subprocess.run(f'pip install -r {req_file}', shell=True, check=True):
            mark_req_file_installed(req_file)
            mark_req_file_installed('_requirements.txt')

    return django_process


def wait_for_file_changes(paths, initial=True, watch=True):
    if initial:
        yield

    if watch:
        initial_hash = files_hash(paths)

        while True:
            # try:
            sleep(3)
            new_hash = files_hash(paths)
            if initial_hash != new_hash:
                initial_hash = new_hash
                yield
            # except KeyboardInterrupt:
            #     print('Reloading ... (hit ctrl+c twice to stop process)')
            #     yield


def files_hash(paths):
    hash_md5 = hashlib.md5()

    for filename in paths:
        try:
            with open(filename, "rb") as f:
                for chunk in iter(lambda: f.read(2 ** 20), b""):
                    hash_md5.update(chunk)
        except (FileNotFoundError, IOError):
            pass

    return hash_md5.hexdigest()
