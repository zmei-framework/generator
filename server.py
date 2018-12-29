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

import jwt
from elasticsearch import Elasticsearch
from jwt import PyJWTError
from sanic import Sanic
from sanic.response import HTTPResponse, text
from zmei_generator.generator.application import ZmeiAppParser

from zmei_generator.generator.collections import generate, generate_common_files
from zmei_generator.parser.errors import ValidationError
from zmei_generator.generator.utils import StopGenerator
from zmei_generator.parser.parser import ZmeiParser
from zmei_generator.parser.stats import StatsCollector


def maybeAsync(callable, *args, **kwargs):
    """
    Turn a callable into a coroutine if it isn't
    """

    if asyncio.iscoroutine(callable):
        return callable

    return asyncio.coroutine(callable)(*args, **kwargs)


def fire(callable, *args, **kwargs):
    """
    Fire a callable as a coroutine, and return it's future. The cool thing
    about this function is that (via maybeAsync) it lets you treat synchronous
    and asynchronous callables the same, which simplifies code.
    """

    return asyncio.ensure_future(maybeAsync(callable, *args, **kwargs))


async def _call_later(delay, callable, *args, **kwargs):
    """
    The bus stop, where we wait.
    """

    await asyncio.sleep(delay)
    fire(callable, *args, **kwargs)


def call_later(delay, callable, *args, **kwargs):
    """
    After :delay seconds, call :callable with :args and :kwargs; :callable can
    be a synchronous or asynchronous callable (a coroutine). Note that _this_
    function is synchronous - mission accomplished - it can be used from within
    any synchronous or asynchronous callable.
    """

    fire(_call_later, delay, callable, *args, **kwargs)


app = Sanic()

from sanic import response
from aioelasticsearch import Elasticsearch


@app.route('/api/generate', methods=['POST'])
async def api_generate(request):
    with tempfile.TemporaryDirectory() as target_path:

        # target_path = '/Users/aleksandrrudakov/dev/generator/test'

        try:
            with ThreadPoolExecutor(max_workers=100) as executor:
                request_files = await app.loop.run_in_executor(executor, extract_files, target_path, request)

                await do_generate(executor, request, target_path)

                zip = await app.loop.run_in_executor(executor, collect_files, target_path, request_files)

            return HTTPResponse(status=200, content_type='application/binary', body_bytes=zip.getvalue())

        except (NotImplementedError, ValidationError) as e:
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


async def send_data(data):
    async with Elasticsearch() as es:
        print("Indexing thing")
        await es.index(
            index="stats",
            doc_type="generate",
            body=data
        )


async def do_generate(executor, request, target_path):
    stats_listener = StatsCollector()

    features = []
    if request.form.get('features'):
        features = request.form.get('features').split(',')

    app_parser = ZmeiAppParser()

    for app_name in request.form.get('collections').split(','):
        filename = '{}.col'.format(app_name)

        if not os.path.exists(os.path.join(target_path, 'col/' + filename)):
            if not os.path.exists(os.path.join(target_path, filename)):
                raise StopGenerator('File col/{filename} or {filename} do not exist'.format(filename=filename))
        else:
            filename = 'col/' + filename

        # all_apps.append(
        #     app.loop.run_in_executor(executor, generate_app, stats_listener, target_path, app_name, features, filename))

        with open(os.path.join(target_path, filename)) as f:
            app_parser.add_file(filename, f.read())

        # collection_set = parser.populate_collection_set_and_errors(app_name)

    application = app_parser.parse()

    for app_name, collection_set in application.collection_sets.items():
        generate(target_path, app_name, collection_set, features=features)


    # all_apps = {app_name: cs for app_name, cs in await asyncio.gather(*all_apps)}

    skeleton_dir = os.path.join(os.path.realpath(dirname(__file__)), 'skeleton')
    await app.loop.run_in_executor(executor, generate_common_files, target_path, skeleton_dir, application.collection_sets)

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

    data = stats_listener.get_data()
    data['user'] = request['user']['user_id']
    data['files'] = data['features'].get('Col_file', 0)
    data['models'] = data['features'].get('Col', 0)
    data['pages'] = data['features'].get('Page', 0)

    data['features'] = list(data['features'].keys())

    call_later(1, send_data, data)


def generate_app(stats_listener, target_path, app_name, features, filename):
    parser = ZmeiParser()
    parser.parse_file(os.path.join(target_path, filename))
    collection_set = parser.populate_collection_set_and_errors(app_name)

    parser.collect_stats(stats_listener)

    generate(target_path, app_name, collection_set, features=features)

    return app_name, collection_set


def extract_files(target_path, request):
    files = BytesIO(request.files.get('gen').body)
    files = zipfile.ZipFile(files, mode='r', compression=zipfile.ZIP_LZMA)
    files.extractall(path=target_path)

    return set(files.namelist())


def get_user(jwt_token):
    secret = '5%)z2n2io_m7%&=(y6s#s(1#$qx@1!w!2(_s+5(u*78$mh9lye'

    token = jwt.decode(jwt_token, secret, algorithms=['HS256'])
    return token


if __name__ == '__main__':

    if os.environ.get('ZMEI_DEBUG') == '1':
        # Import reloader class
        from aoiklivereload import LiveReloader

        # Create reloader
        reloader = LiveReloader()

        # Start watcher thread
        reloader.start_watcher_thread()


    @app.middleware('request')
    async def auth_request(request):
        auth = request.headers.get('authorization')
        if not auth:
            return text('Missing authentication token.', status=401)

        try:
            token_type, token = auth.split(' ')
        except ValueError:
            return text('Malformed authorization header.', status=401)

        if token_type != 'JWT':
            return text('Unsupported authorization type.', status=401)

        try:
            user = get_user(token)

            if not user:
                return text('Invalid authentication token. Can not authorise user.', status=403)

            request['user'] = user

        except PyJWTError as e:
            return text(str(e), status=403)


    app.run(host='0.0.0.0', port=9000)
