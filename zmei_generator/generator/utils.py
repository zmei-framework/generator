import os
import re

import autopep8
import jinja2
from jinja2 import Environment, FileSystemBytecodeCache
from jinja2 import PackageLoader
from termcolor import colored

from zmei_generator.generator.imports import ImportSet


def indent_text(nr, text):
    inds = (' ' * nr)
    return inds + ('\n' + inds).join(text.splitlines())


def package_to_path(package_name):
    """
    Convert package name to relative directory name

    :param package_name:
    :return:
    """
    return package_name.replace('.', os.path.sep)


def render_local_template(tpl_path, context):
    path, filename = os.path.split(tpl_path)
    return jinja2.Environment(
        loader=jinja2.FileSystemLoader(path or './')
    ).get_template(filename).render(context)


def fill_file(file_path, context, template=None):
    data = render_local_template(template or file_path, context)

    with open(file_path, 'w') as f:
        f.write(data)


def field_names(fields, admin=False):
    names = []
    for field in fields:
        if admin and field.admin_list_renderer:
            names.append('get_{}'.format(field.name))
        else:
            names.append(field.name)

    return format_names(names)


def format_names(names):
    if not names:
        return ''
    return "'{}'".format("', '".join(names))


def to_name(ref):
    return ' '.join([x.capitalize() for x in ref.split('_')])


def include_block(block):
    template = block_env.get_template(block.template_name)
    return template.render(**block.fields)


loader = PackageLoader('zmei_generator', 'templates')

block_env = Environment(loader=loader,
                        variable_start_string='<{',
                        variable_end_string='}>',
                        block_start_string='<%',
                        block_end_string='%>'
                        )

bcc = FileSystemBytecodeCache()

env = Environment(
    loader=loader,
    bytecode_cache=bcc
)
env.filters['field_names'] = field_names
env.filters['format_names'] = format_names
env.filters['to_name'] = to_name
env.filters['repr'] = repr
env.globals['include_block'] = include_block


def generate_file(target_path, filename, template_name, context=None, raw=False):
    """
    Generates a new file using Jinja2 template

    :param dirname:
    :param template_name:
    :param context:
    :return:
    """
    filename = os.path.join(target_path, filename)

    dirname = os.path.dirname(filename)
    if len(dirname) and not os.path.exists(dirname):
        os.makedirs(dirname)

    with open(filename, 'w') as f:
        if not raw:
            rendered = render_template(template_name, context=context)
        else:
            rendered = render_file(template_name)

        if filename.endswith('.py'):
            rendered = autopep8.fix_code(rendered)

        f.write(rendered)


def render_template(template_name, context=None):
    context = context or {}

    template = env.get_template(template_name)

    return template.render(**context)


def render_file(template_name):
    return loader.get_source(env, template_name)[0]


def format_file(target_path, filename):
    filename = os.path.join(target_path, filename)

    with open(filename, 'r') as f:
        code = f.read()
    with open(filename, 'w') as f:
        f.write(autopep8.fix_code(code))


def generate_feature(target_path, package_name: str, feature_name: str, collection_set, extra_context=None):
    """
    Generates new feature

    :param package_name:
    :param name:
    :return:
    """
    assert feature_name

    sitemap_imports = ImportSet()

    for page in collection_set.pages.values():
        if page.has_sitemap:
            sitemap_imports.add(f'{package_name}.views', page.view_name)

    generate_package(package_name, path=target_path)

    filepath = os.path.join(package_to_path(package_name), 'features.py')

    context = {
        'feature_name': feature_name,
        'package_name': package_name,
        'sitemap_imports': sitemap_imports.import_sting(),
        'collection_set': None,
    }
    if extra_context:
        context.update(extra_context)

    generate_file(target_path, filepath, 'cratis/feature.py.tpl', context)


def generate_urls_file(target_path, app_name, collection_set, pages, i18n=False):
    url_imports = ImportSet()
    url_imports.add('django.conf.urls', 'url')

    for page in pages:
        url_imports.add('.views', page.view_name)

    context = {
        'i18n': i18n,
        'package_name': app_name,
        'collection_set': collection_set,
        'pages': pages,
        'url_imports': url_imports.import_sting(),
    }

    filepath = os.path.join(package_to_path(app_name), 'urls_i18n.py' if i18n else 'urls.py')

    generate_file(target_path, filepath, 'urls.py.tpl', context)


def generate_urls_rest(target_path, app_name, collection_set):
    url_imports = ImportSet()
    url_imports.add('django.conf.urls', 'url')
    url_imports.add('django.conf.urls', 'include')
    url_imports.add('rest_framework', 'routers')

    for name, collection in collection_set.collections.items():
        if collection.api:
            for rest_conf in collection.published_apis.values():
                url_imports.add('.views', f'{rest_conf.serializer_name}ViewSet')

    context = {
        'package_name': app_name,
        'collection_set': collection_set,
        'url_imports': url_imports.import_sting(),
    }

    filepath = os.path.join(package_to_path(app_name), 'urls_rest.py')
    generate_file(target_path, filepath, 'urls_rest.py.tpl', context)


def generate_package(package_name, path=None):
    if not path:
        path = os.getcwd()

    if not isinstance(package_name, list):
        parts = package_name.split('.')
    else:
        parts = package_name

    dirname = os.path.join(path, parts[0])

    if not os.path.exists(dirname):
        os.mkdir(dirname)

    if not os.path.exists(os.path.join(dirname, '__init__.py')):
        with open(os.path.join(dirname, '__init__.py'), 'w+') as f:
            f.write('\n\n')

    if len(parts) > 1:
        generate_package(parts[1:], dirname)


class StopGenerator(Exception):
    def __init__(self, description=None, *args) -> None:
        super().__init__(*args)

        self.description = description or 'Unknown fail'


def handle_parse_exception(e, parsed_string, subject):
    out = []
    # out.append(str(type(e)))
    out.append(colored('{}, error: {}'.format(subject, e), 'white', 'on_red'))
    out.append('-' * 100)
    for nr, line in enumerate(parsed_string.splitlines()):
        if nr < e.lineno - 5:
            if out[-1] != '...':
                out.append('...')
            continue
        if nr > e.lineno + 5:
            if out[-1] != '...':
                out.append('...')
            continue

        if (nr + 1) == e.lineno:
            try:
                before = line[:e.col]
                char = line[e.col]
                after = line[e.col + 1:]
            except IndexError:
                out.append(colored('{0:04d}| {1}'.format(nr + 1, line), 'white', 'on_red'))

                continue

            line = before + colored(char, 'white', 'on_blue') + after

            out.append(colored('{0:04d}| {1}'.format(nr + 1, line), 'white', 'on_red'))
        else:
            out.append('{0:04d}| {1}'.format(nr + 1, line))

    out.append('-' * 100)
    raise StopGenerator('\n'.join(out))


def gen_args(args, raw_args=None):
    if not raw_args:
        raw_args = []
    _args = []
    for key, val in args.items():
        if key == '_':
            _args.append(val)
        else:
            if key not in raw_args:
                val = repr(val)
            if key in ('verbose_name', 'help_text'):
                val = '_({})'.format(val)

            _args.append('{}={}'.format(key, val))

    return ', '.join(_args)
