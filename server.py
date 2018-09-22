import asyncio
import io
import os
import tempfile
import zipfile
from asyncio import create_subprocess_exec
from concurrent.futures import ThreadPoolExecutor
from glob import glob
from io import BytesIO
from os.path import dirname

from zmei_generator.config.domain.exceptions import ValidationException
from zmei_generator.config.parser import Parser
from zmei_generator.generator.collections import generate, generate_common_files
from zmei_generator.generator.utils import StopGenerator

from sanic.exceptions import InvalidUsage

from sanic import Sanic
from sanic.response import HTTPResponse

app = Sanic()

from sanic import response


@app.route('/api/generate', methods=['POST'])
async def api_generate(request):

    with tempfile.TemporaryDirectory() as target_path:

        # target_path = '/Users/aleksandrrudakov/dev/generator/test'

        try:
            with ThreadPoolExecutor(max_workers=1) as executor:
                request_files = await app.loop.run_in_executor(executor, extract_files, target_path, request)

                await do_generate(executor, request, target_path)

                zip = await app.loop.run_in_executor(executor, collect_files, target_path, request_files)

            return HTTPResponse(status=200, content_type='application/binary', body_bytes=zip.getvalue())

        except (NotImplementedError, ValidationException) as e:
            return response.json({'detail': str(e).replace(target_path, '')}, status=400)

        except StopGenerator as e:
            return response.json({'detail': str(e.description).replace(target_path, '')}, status=400)


def collect_files(target_path, request_files):
    paths = set(glob(f'{target_path}/**/*.*', recursive=True))
    paths.update(glob(f'{target_path}/**/Dockerfile', recursive=True))
    paths.update(glob(f'{target_path}/**/.babelrc', recursive=True))
    paths.update(glob(f'{target_path}/**/.dockerignore', recursive=True))

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


async def do_generate(executor, request, target_path):
    features = []
    if request.form.get('features'):
        features = request.form.get('features').split(',')

    all_apps = []

    for app_name in request.form.get('collections').split(','):
        filename = '{}.col'.format(app_name)
        if not os.path.exists(os.path.join(target_path, 'col/' + filename)):
            if not os.path.exists(os.path.join(target_path, filename)):
                raise StopGenerator('File col/{filename} or {filename} do not exist'.format(filename=filename))
        else:
            filename = 'col/' + filename

        all_apps.append(app.loop.run_in_executor(executor, generate_app, target_path, app_name, features, filename))

    all_apps = {app_name: cs for app_name, cs in await asyncio.gather(*all_apps)}

    skeleton_dir = os.path.join(os.path.realpath(dirname(__file__)), 'skeleton')
    await app.loop.run_in_executor(executor, generate_common_files, target_path, skeleton_dir, all_apps)

    if 'react' in features and os.path.exists(os.path.join(target_path, 'react/package.json')):
        webpack_home = os.path.join(os.path.realpath(dirname(__file__)), 'webpack')
        react_app_home = os.path.join(target_path, 'react')
        node_modules = os.path.join(react_app_home, 'node_modules')
        webpack = os.path.join(node_modules, '.bin/webpack')

        if os.path.exists(node_modules):
            os.unlink(node_modules)

        os.symlink(os.path.join(webpack_home, 'node_modules'), node_modules)
        proc = await create_subprocess_exec(webpack, cwd=react_app_home, env=os.environ.copy(), loop=app.loop)

        await proc.wait()

        os.unlink(node_modules)


def generate_app(target_path, app_name, features, filename):
    collection_set = Parser().parse_file(os.path.join(target_path, filename), app_name=app_name)
    generate(target_path, app_name, collection_set, features=features)
    return app_name, collection_set


def extract_files(target_path, request):
    files = BytesIO(request.files.get('gen').body)
    files = zipfile.ZipFile(files, mode='r', compression=zipfile.ZIP_LZMA)
    files.extractall(path=target_path)

    return set(files.namelist())


if __name__ == '__main__':

    if os.environ.get('ZMEI_DEBUG') == '1':
        # Import reloader class
        from aoiklivereload import LiveReloader

        # Create reloader
        reloader = LiveReloader()

        # Start watcher thread
        reloader.start_watcher_thread()

    app.run(host='0.0.0.0', port=9000)