import hashlib
import io
import json
import os
import re
import signal
import sys
import zipfile
from glob import glob
from contextlib import contextmanager
import subprocess
from io import BytesIO
from shutil import rmtree
from tarfile import TarFile

from termcolor import colored
from time import sleep

from genius_cli.blocks import render_blocks


@contextmanager
def chdir(path):
    cwd = os.getcwd()
    os.chdir(path)
    yield
    os.chdir(cwd)


PACKAGE_JSON_TOKEN = '__generated__'


def write_generated_file(path, source):
    # special hack for settings.py->SECRET_KEY
    if path.endswith('app/settings.py'):
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

    if path.endswith('.py') or path.endswith('requirements.txt') or path.endswith('Dockerfile'):
        source_prefix = f"# {tag}\n\n"

    elif path.endswith('.js') or path.endswith('.jsx'):
        source_prefix = f"//# {tag}\n\n"

    elif path.endswith('package.json'):
        chksum = source_hash(json.dumps(json.loads(source), indent=4))
        source = json.dumps({**json.loads(source), **{PACKAGE_JSON_TOKEN: chksum}}, indent=4)

    elif ('/templates/' in path or '/themes/' in path) and path.endswith('.html'):
        source_prefix = f"{{# {tag} #}}\n\n"

    if os.path.exists(path):
        generated, changed, file_checksum = is_generated_file(path)

        if generated:
            if changed:
                print(colored(' ! ', 'red', 'on_yellow'), ' ', path)
                return  # checksum failed. Changed by hands?
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


def is_generated_file(path):
    """
    Checks if file is generated, and is it changed
    :param path:

    :return: generated, changed, checksum
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
            file_chk_expected = data.get(PACKAGE_JSON_TOKEN)
        except KeyError:
            return False, False, None

        data = json.loads(content)
        if PACKAGE_JSON_TOKEN in data:
            del data[PACKAGE_JSON_TOKEN]
        real_source = json.dumps(data, indent=4)

    else:
        match = re.match('^({|//)?# generated: ([a-f0-9]{32})( #})?\n\n', content)
        if not match:
            return False, False, None

        file_chk_expected = match.group(2)
        real_source = content[len(match.group(0)):]

    file_chk_real = source_hash(real_source)

    if file_chk_expected != file_chk_real:
        return True, True, file_chk_real  # checksum failed. Changed by hands?
    else:
        return True, False, file_chk_real


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
        if file == 'node_modules':
            continue

        fullpath = os.path.join(path, file)

        if os.path.isdir(fullpath):
            clean_up_generated_files(fullpath, file_list, remove_root=True)
        else:
            if file[0] != '.' and file.split('.')[-1] in ('js', 'jsx', 'py', 'html'):
                generated, changed, file_checksum = is_generated_file(fullpath)

                if generated and (fullpath not in file_list):
                    if changed:
                        print(colored('skip:', 'red', 'on_yellow'), ' ', fullpath)
                    else:
                        print(colored(' - ', 'white', 'on_red'), ' ', fullpath)
                        os.unlink(fullpath)

    if len(os.listdir(path)) == 0 and remove_root:
        os.rmdir(path)
        print(colored('delete:', 'white', 'on_red'), ' ', path)


def extract_files(dst, file_bytes):
    files = zipfile.ZipFile(BytesIO(file_bytes), mode='r', compression=zipfile.ZIP_LZMA)

    for path in files.namelist():
        full_path = os.path.join(dst, path)
        write_generated_file(full_path, files.read(path).decode())

    file_list = [f"./{x}" for x in files.namelist()]
    clean_up_generated_files('.', file_list)


def collect_files(src):
    with chdir(src):
        f = io.BytesIO()
        files = zipfile.ZipFile(f, mode='w', compression=zipfile.ZIP_LZMA)

        for path in get_collect_paths():
            generated, changed, checksum = is_generated_file(path)

            if not generated or changed:
                files.write(path)
        files.close()

        f.seek(0)

    return f


def get_collect_paths():
    paths = []
    paths += list(glob('*.col'))
    # paths += list(glob('react/src/**/*.js', recursive=True))
    # paths += list(glob('react/src/**/*.jsx', recursive=True))
    # paths += list(glob('react/*.js'))
    # paths += list(glob('react/*.json'))

    return set(paths)


def get_watch_paths():
    paths = []
    paths += list(glob('*.col'))
    # paths += list(glob('react/src/**/*.js', recursive=True))
    # paths += list(glob('react/src/**/*.jsx', recursive=True))
    # paths += list(glob('react/*.js'))
    paths += list(glob('react/*.json'))

    return set(paths)


def collect_app_names():
    collections = []
    for filename in os.listdir('.'):
        if os.path.isfile(filename) and filename.endswith('.col'):
            if not re.match('^[a-zA-Z][a-zA-Z0-9_]+\.col$', filename):
                print('Collection file has incorrect name: {}'.format(filename))
            app_name = filename[0:-4]
            collections.append(app_name)
    return collections


def migrate_db(apps, features=None):
    print(colored('> ', 'white', 'on_blue'), 'Migrating database')
    django_command = get_django_command(features)

    for app_name in apps:
        subprocess.run('{} makemigrations {}'.format(django_command, app_name), shell=True, check=True)
        try:
            subprocess.run('{} migrate'.format(django_command), shell=True, check=True)
            # subprocess.run('{} migrate {}'.format(django_command, app_name), shell=True, check=True)
        except subprocess.CalledProcessError:
            pass

        # if cratis
        if django_command == 'django':
            subprocess.run('{} sync_translation_fields_safe'.format(django_command), shell=True, check=True)


def run_django(features=None, run_host='127.0.0.1:8000'):
    print(colored('> ', 'white', 'on_blue'), 'Starting django')
    django_command = get_django_command(features, )
    full_command = '{} runserver {}'.format(django_command, run_host)
    print(full_command)
    return subprocess.Popen(full_command, preexec_fn=os.setsid, shell=True)


def run_webpack():
    print(colored('> ', 'white', 'on_blue'), 'Starting webpack')

    webpack_command = './node_modules/.bin/webpack -w'
    print(webpack_command)
    return subprocess.Popen('{}'.format(webpack_command), shell=True, cwd='react', preexec_fn=os.setsid)


def npm_install():
    if is_req_file_changed('react/package.json'):
        print(colored('> ', 'white', 'on_blue'), 'Installing nodejs dependencies ...')
        cmd = 'npm install'
        print(cmd)
        if subprocess.run('{}'.format(cmd), shell=True, cwd='react', check=True):
            mark_req_file_installed('react/package.json')


def remove_db(apps, features=None):
    django_command = get_django_command(features)

    for app_name in apps:
        filename = '{}.col'.format(app_name)
        if not os.path.exists(filename):
            print('No such collection: {}'.format(app_name))
        app_name = app_name

        print(colored('> ', 'white', 'on_blue'), 'Unapplying migrations')
        subprocess.run('{} migrate {} zero'.format(django_command, app_name), shell=True, check=True)

        print(colored('> ', 'white', 'on_blue'), 'Removing migrations')
        rmtree('{}/migrations'.format(app_name))


def get_django_command(features):
    is_cratis = features and 'cratis' in features
    if is_cratis:
        django_command = 'django'
    else:
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
    if is_req_file_changed('requirements.txt'):
        if django_process:
            os.killpg(os.getpgid(django_process.pid), signal.SIGTERM)
            django_process = None

        print(colored('> ', 'white', 'on_blue'), 'Installing pip dependencies...')
        if subprocess.run('pip install -r requirements.txt', shell=True, check=True):
            mark_req_file_installed('requirements.txt')

    return django_process


def wait_for_file_changes(paths, initial=True, watch=True):
    if initial:
        yield

    if watch:
        initial_hash = files_hash(paths)

        while True:
            sleep(1.0)
            new_hash = files_hash(paths)
            if initial_hash != new_hash:
                initial_hash = new_hash
                yield


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
