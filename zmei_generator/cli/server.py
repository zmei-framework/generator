import io
import os
import tempfile
import zipfile
from glob import glob
from io import BytesIO
from os.path import dirname
from shutil import rmtree, copytree, copyfile

import pkg_resources


def zmei_generate(zip_bytes, models):
    # TODO: remove zip packing/unpacking. It comes from old remote protocol.
    # TODO: NOw it is not needed anymore.

    with tempfile.TemporaryDirectory() as target_path:
        request_files = extract_files(target_path, zip_bytes)

        do_generate(target_path, models)

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


def do_generate(target_path, app_names):
    from zmei_generator.generator.application import ZmeiProjectParser
    from zmei_generator.generator.utils import StopGenerator

    app_parser = ZmeiProjectParser()

    for app_name in app_names:
        filename = '{}.col'.format(app_name)

        if not os.path.exists(os.path.join(target_path, 'col/' + filename)):
            if not os.path.exists(os.path.join(target_path, filename)):
                raise StopGenerator('File col/{filename} or {filename} do not exist'.format(filename=filename))
        else:
            filename = 'col/' + filename

        with open(os.path.join(target_path, filename)) as f:
            app_parser.add_file(filename, f.read())

        # application = parser.populate_application_and_errors(app_name)

    application = app_parser.parse()

    copy_skeleton_files(target_path)

    for entry_point in pkg_resources.iter_entry_points('zmei.generator'):
        generate = entry_point.load()
        generate(target_path, application)


def copy_skeleton_files(target_path):
    skeleton_dir = os.path.join(os.path.realpath(dirname(__file__)), 'skeleton')
    app_dir = os.path.join(target_path, 'app')
    manage_py = os.path.join(target_path, 'manage.py')
    if os.path.exists(app_dir):
        rmtree(app_dir)
    if os.path.exists(manage_py):
        os.unlink(manage_py)
    copytree(os.path.join(skeleton_dir, 'app'), app_dir)
    copyfile(os.path.join(skeleton_dir, 'manage.py'), manage_py)
    return skeleton_dir


def extract_files(target_path, zip_data):
    files = BytesIO(zip_data)
    files = zipfile.ZipFile(files, mode='r', compression=zipfile.ZIP_LZMA)
    files.extractall(path=target_path)

    return set(files.namelist())
