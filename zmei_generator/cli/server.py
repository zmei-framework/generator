import io
import os
import subprocess
import tempfile
import zipfile
from glob import glob
from io import BytesIO
from os.path import dirname
from shutil import rmtree

from zmei_generator.generator.application import ZmeiAppParser
from zmei_generator.generator.collections import generate, generate_common_files
from zmei_generator.generator.utils import StopGenerator
from zmei_generator.parser.parser import ZmeiParser


def zmei_generate(zip_bytes, collections):

    with tempfile.TemporaryDirectory() as target_path:
        request_files = extract_files(target_path, zip_bytes)

        do_generate(target_path, collections)

        zip_file = collect_files(target_path, request_files)

        return zip_file.getvalue()


def collect_files(target_path, request_files):
    paths = set(glob(f'{target_path}/**/*.*', recursive=True))
    paths.update(glob(f'{target_path}/**/.*', recursive=True))
    paths.update(glob(f'{target_path}/**/Dockerfile', recursive=True))
    paths.update(glob(f'{target_path}/**/.babelrc', recursive=True))
    paths.update(glob(f'{target_path}/**/.dockerignore', recursive=True))

    paths = [x for x in paths if '__pycache__' not in x]

    # # remove prefix
    tpl = len(f'{target_path}/')
    paths = set([x[tpl:] for x in paths])

    f = io.BytesIO()

    files = zipfile.ZipFile(f, mode='w', compression=zipfile.ZIP_LZMA)
    for path in (paths - request_files):
        files.write(f'{target_path}/{path}', arcname=path)
    files.close()
    #
    f.seek(0)

    return f


def do_generate(target_path, collections):
    app_parser = ZmeiAppParser()

    for app_name in collections:
        filename = '{}.col'.format(app_name)

        if not os.path.exists(os.path.join(target_path, 'col/' + filename)):
            if not os.path.exists(os.path.join(target_path, filename)):
                raise StopGenerator('File col/{filename} or {filename} do not exist'.format(filename=filename))
        else:
            filename = 'col/' + filename

        with open(os.path.join(target_path, filename)) as f:
            app_parser.add_file(filename, f.read())

        # collection_set = parser.populate_collection_set_and_errors(app_name)

    application = app_parser.parse()

    for app_name, collection_set in application.collection_sets.items():
        generate(target_path, app_name, collection_set)

    # all_apps = {app_name: cs for app_name, cs in await asyncio.gather(*all_apps)}

    skeleton_dir = os.path.join(os.path.realpath(dirname(__file__)), 'skeleton')

    generate_common_files(target_path, skeleton_dir, application.collection_sets)

    flutter_dir = os.path.join(target_path, 'flutter')
    if os.path.exists(flutter_dir):
        subprocess.check_call(['dartfmt', '-w', '-l', '120', flutter_dir], stdout=subprocess.DEVNULL)


def generate_app(stats_listener, target_path, app_name, features, filename):
    parser = ZmeiParser()
    parser.parse_file(os.path.join(target_path, filename))
    collection_set = parser.populate_collection_set_and_errors(app_name)

    parser.collect_stats(stats_listener)

    generate(target_path, app_name, collection_set, features=features)

    return app_name, collection_set


def extract_files(target_path, zip_data):
    files = BytesIO(zip_data)
    files = zipfile.ZipFile(files, mode='r', compression=zipfile.ZIP_LZMA)
    files.extractall(path=target_path)

    return set(files.namelist())
