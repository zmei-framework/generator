import json
import os
import random
import re
import string
import subprocess
from os import unlink
from shutil import copytree, copyfile, rmtree

from zmei_generator.config.domain.collection_set_def import FieldDeclaration, CollectionSetDef
from zmei_generator.config.domain.field_def import FieldDef
from zmei_generator.generator.imports import ImportSet
from zmei_generator.generator.utils import generate_feature, generate_file, generate_urls_file, generate_urls_rest, \
    format_file


def list_apps():
    for filename in os.listdir('.'):
        if os.path.isfile(filename) and filename.endswith('.col'):
            if not re.match('^[a-zA-Z][a-zA-Z0-9_]+\.col$', filename):
                continue

            yield filename[0:-4]


def generate_common_files(target_path, skeleton_dir, apps):
    app_dir = os.path.join(target_path, 'app')
    manage_py = os.path.join(target_path, 'manage.py')

    if os.path.exists(app_dir):
        rmtree(app_dir)

    if os.path.exists(manage_py):
        unlink(manage_py)

    copytree(os.path.join(skeleton_dir, 'app'), app_dir)
    copyfile(os.path.join(skeleton_dir, 'manage.py'), manage_py)

    # config
    has_react = False
    has_flutter = False
    has_crud = False
    has_rest = False
    has_docker = False
    has_celery = False
    has_admin = False
    has_filer = False
    has_suit = False
    has_channels = False
    has_i18n_pages = False
    has_normal_pages = False

    i18n_langs = []

    # urls
    imports = set()
    urls = ['urlpatterns = [']
    urls += [
        "    url(r'^admin/', admin.site.urls),",
    ]
    for app_name, collection_set in apps.items():
        if collection_set.react:
            has_react = True

        if collection_set.celery:
            has_celery = True

        if collection_set.flutter:
            has_flutter = True

        for import_def, url_def in collection_set.get_required_urls():
            urls.append(url_def)
            if import_def:
                imports.add(import_def)

        if collection_set.pages:
            for page in collection_set.pages.values():
                if page.i18n:
                    has_i18n_pages = True
                else:
                    has_normal_pages = True

            if has_normal_pages:
                urls.append(f"    url(r'^', include({app_name}.urls)),")
                imports.add(f'{app_name}.urls')

        if collection_set.admin:
            has_admin = True

        if collection_set.channels:
            has_channels = True

        if collection_set.docker:
            has_docker = True

        if collection_set.react:
            has_react = True

        if collection_set.langs:
            i18n_langs += collection_set.langs.langs

        if collection_set.crud:
            has_crud = True

        if collection_set.suit:
            has_suit = True

        if collection_set.filer:
            has_filer = True

        if collection_set.api:
            has_rest = True
            urls.append(f"    url(r'^api/', include({app_name}.urls_rest)),")
            imports.add(f'{app_name}.urls_rest')

    urls.append(']')

    if has_i18n_pages:
        urls += [
            'urlpatterns += i18n_patterns(',
            f"    url(r'^', include({app_name}.urls_i18n)),",
            ")"
        ]
        imports.add(f'{app_name}.urls_i18n')

    # urls
    with open(os.path.join(target_path, 'app/_urls.py'), 'w') as f:
        f.write('from django.conf.urls import url, include\n')
        f.write('from django.contrib import admin\n')

        f.write('\n')
        f.write('\n'.join([f'import {app_name}' for app_name in imports]))
        if has_i18n_pages:
            f.write('\nfrom django.conf.urls.i18n import i18n_patterns\n')
        f.write('\n\n')
        f.write('\n'.join(urls))

    generate_file(target_path, 'app/urls.py', template_name='urls_main.py.tpl')

    # settings
    req_settings = {}
    installed_apps = [app.app_name for app in apps.values() if len(app.pages) > 0 or len(app.collections) > 0]

    if has_crud:
        installed_apps.append('zmei.crud')

    if has_rest:
        installed_apps.append('rest_framework')

    extra_classes = list()
    for collection_set in sorted(apps.values(), key=lambda x: x.app_name):
        installed_apps.extend(collection_set.get_required_apps())
        req_settings.update(collection_set.get_required_settings())

        for extra in collection_set.extras:
            if type(extra) not in extra_classes:
                extra_classes.append(type(extra))

    # remove duplicates preserving order
    seen = set()
    seen_add = seen.add
    installed_apps = [x for x in installed_apps if not (x in seen or seen_add(x))]

    with open(os.path.join(target_path, 'app/settings.py'), 'r') as fb:
        with open(os.path.join(target_path, 'app/_settings.py'), 'a') as f:
            f.write(fb.read())

            f.write('\nINSTALLED_APPS = [\n')
            f.write("\n    'app',\n")
            f.write('\n'.join([f"    '{app_name}'," for app_name in installed_apps]))
            f.write('\n] + INSTALLED_APPS\n\n')  # settings

            for key, val in req_settings.items():
                f.write(f'{key} = {repr(val)}\n')

            for extra in extra_classes:
                extra.write_settings(apps, f)

    generate_file(target_path, 'app/settings.py', template_name='settings.py.tpl')
    format_file(target_path, 'app/_settings.py')

    for extra in extra_classes:
        extra.generate(apps, target_path)

    # base template
    generate_file(target_path, 'app/templates/base.html', template_name='theme/base.html')

    requirements = [
        'zmei-utils>=0.1.15',
        'wheel',
        'django>2',
    ]

    if has_rest:
        requirements.append('djangorestframework')

    for collection_set in apps.values():
        requirements.extend(collection_set.get_required_deps())

    requirements = list(sorted(set(requirements)))

    # requirements
    with open(os.path.join(target_path, '_requirements.txt'), 'w') as f:
        f.write('\n'.join(requirements))

    generate_file(target_path, 'requirements.txt', template_name='requirements.txt.tpl')

    if i18n_langs:
        for lang in i18n_langs:
            os.makedirs(os.path.join(target_path, f'locale/{lang}'))
            with open(os.path.join(target_path, f'locale/{lang}/readme.txt'), 'w') as f:
                f.write('Collect translations:\n')
                f.write('django-admin makemessages --all\n')
                f.write('\n')
                f.write('Compile translations:\n')
                f.write('django-admin compilemessages\n')

    if has_channels:
        streams = []
        imports = ImportSet()
        for app in apps.values():
            if not app.channels:
                continue
            for page in app.pages.values():
                if page.stream:
                    streams.append((app, page))
                    imports.add(f'{app.app_name}.views', f'{page.view_name}Consumer')

        generate_file(target_path, f'app/routing.py', 'channels.routing_main.tpl', context={
            'streams': streams,
            'imports': imports,
        })

    # react
    if has_react:
        generate_react_configs(target_path, apps)

    # react
    if has_flutter:
        generate_flutter_configs(target_path, apps)

    # theme files
    for collection_set in apps.values():
        for page in collection_set.pages.values():
            for path, template_name in page.themed_files.items():
                generate_file(target_path, f'app/templates/{path}', template_name, raw=True)

    file_mapping = []

    for collection_set in apps.values():
        for name, source in collection_set.files.items():
            file_mapping.append({
                'kind': 'file',
                'path': name,
                'source': source
            })

    with open(os.path.join(target_path, '__files.json'), 'w') as f:
        f.write(json.dumps(file_mapping))

    if has_docker:
        generate_file(target_path, 'requirements.prod.txt', 'docker/requirements.prod.txt.tpl', {
            'req_file': os.environ.get('ZMEI_REQUIREMNETS_FILE', 'requirements.txt')
        })
        generate_file(target_path, 'app/settings_prod.py', 'docker/settings_prod.py.tpl', {
            'has_celery': has_celery
        })
        generate_file(target_path, 'Dockerfile', 'docker/dockerfile.tpl')
        generate_file(target_path, '.dockerignore', 'docker/dockerignore.tpl')
        generate_file(target_path, 'docker-compose.yaml', 'docker/docker-compose.yaml.tpl', {
            'has_celery': has_celery
        })

        generate_file(target_path, 'deploy/init.sh', 'docker/init.sh.tpl', {
            'admin_pass': ''.join(random.choice(
                string.ascii_letters + string.digits + string.punctuation.replace('"', '')) for _ in range(16)),
            'admin_user': 'admin-' + ''.join(random.choice(string.ascii_letters + string.digits) for _ in range(4)),
        })
        generate_file(target_path, 'deploy/nginx.conf', 'docker/nginx.conf.tpl')
        generate_file(target_path, 'deploy/uwsgi.ini', 'docker/uwsgi.ini.tpl')

    for collection_set in apps.values():
        if collection_set.gitlab:
            for file in [
                '.gitlab-ci.yml',
                '.gitignore',
                'README.md'
            ]:
                generate_file(target_path, file, f"gitlab/{file.strip('.')}.tpl", {
                    'gitlab': collection_set.gitlab,
                })
            if collection_set.gitlab.test:
                for file in [
                    'conftest.py',
                    'pytest.ini',
                    'requirements.dev.txt',
                    '.flake8',
                    '.coveragerc'
                ]:
                    generate_file(target_path, file, f"gitlab/{file.strip('.')}.tpl", {
                        'gitlab': collection_set.gitlab,
                    })

                generate_file(target_path, 'app/settings_test.py', template_name='settings.py.tpl')


def generate(target_path, app_name: str, collection_set: CollectionSetDef, features=None):
    features = features or []

    features = type('features', (object,), {x: x in features for x in [
        'cratis', 'django'
    ]})
    collection_set.features = features

    # urls
    pages_i18n = [page for page in collection_set.pages.values() if page.has_uri and page.i18n]
    if len(pages_i18n) > 0:
        generate_urls_file(
            target_path,
            app_name,
            collection_set,
            pages_i18n,
            i18n=True
        )

    # urls i18n
    pages = [page for page in collection_set.pages.values() if page.has_uri and not page.i18n]
    if collection_set.pages:
        generate_urls_file(
            target_path,
            app_name,
            collection_set,
            pages,
            i18n=False
        )

    # urls rest
    if collection_set.api:
        generate_urls_rest(target_path, app_name, collection_set)

    if features.cratis:
        # features
        generate_feature(target_path, app_name, app_name.capitalize(), collection_set, {
            'collection_set': collection_set,
            'pages_i18n': pages_i18n,
            'pages': pages
        })

    # Models

    if len(collection_set.collections.values()) > 0:
        generate_models_py(target_path, app_name, collection_set)

    # translations
    if collection_set.translatable:
        generate_translation_py(target_path, app_name, collection_set)

    # admin
    if collection_set.admin:
        generate_admin_py(target_path, app_name, collection_set)

    # views
    if len(collection_set.pages) > 0 or len(collection_set.collections) > 0:
        generate_file(target_path, '{}/__init__.py'.format(app_name), 'init.py.tpl')

    if collection_set.rest:
        generate_serializers_py(target_path, app_name, collection_set)

    if collection_set.rest or len(collection_set.pages.values()) > 0:
        generate_views_py(target_path, app_name, collection_set)

    if len(collection_set.pages) > 0:
        generate_file(target_path, '{}/templates/{}/base.html'.format(app_name, app_name),
                      template_name='theme/base_app.html', context={
                'collection_set': collection_set,
            })

    # react templates
    if collection_set.react:
        generate_react_jsx(target_path, app_name, collection_set)


def generate_react_configs(target_path, apps):
    entries = {}

    for app_name, collection_set in apps.items():
        if collection_set.react:
            # entries[app_name] = ["babel-polyfill", f'./src/{app_name.capitalize()}/index.jsx']
            entries[app_name] = [f'./src/index.jsx']

    packages = {}

    for app_name, collection_set in apps.items():
        packages.update(collection_set.react_deps)

    generate_file(target_path, 'react/package.json', 'package.json.tpl', {
        'packages': packages
    })
    generate_file(target_path, 'react/webpack.config.js', 'webpack.config.js.tpl', {
        'entries': entries
    })


def to_camel_case_classname(name):
    return ''.join([x.capitalize() for x in name.split('_')])


def to_camel_case(name):
    parts = []

    for idx, part in enumerate(name.split('_')):
        if idx != 0:
            part = part.capitalize()

        parts.append(part)

    return ''.join(parts)


def format_uri(uri):
    return uri.replace('(?P<', ':').replace('>[^\/]+)', '')

def generate_flutter_configs(target_path, apps):
    from zmei_generator.fields.relation import RelationDef
    from zmei_generator.config.domain.reference_field import ReferenceField

    generate_file(target_path, 'flutter/pubspec.yaml', 'flutter.pubspec.yaml.tpl')
    generate_file(target_path, 'flutter/lib/main.dart', 'flutter.main.dart.tpl', {
        'host': os.environ.get('ZMEI_SERVER_HOST')
    })

    for app_name, collection_set in apps.items():

        if collection_set.collections:
            imports = set()
            for col in collection_set.collections.values():
                for field in col.fields.values():

                    if isinstance(field, ReferenceField) and field.target_collection:
                        if field.target_collection.collection_set != collection_set:
                            imports.add(field.target_collection.collection_set.app_name)

                    elif isinstance(field, RelationDef) and field.ref_collection:
                        if field.ref_collection.collection_set != collection_set:
                            imports.add(field.ref_collection.collection_set.app_name)

            generate_file(
                target_path,
                f'flutter/lib/src/models/{app_name}.dart',
                'flutter.model.dart.tpl', {
                    'app_name': app_name,
                    'collection_set': collection_set,
                    'to_camel_case': to_camel_case,
                    'imports': imports
                }
            )

        if collection_set.flutter:
            for name, page in collection_set.pages.items():
                if page.flutter:
                    imports = set()

                    page_items = {}
                    for item_name in page.own_item_names:
                        item = page.page_items[item_name]

                        if item.collection_name:
                            col = collection_set.resolve_collection(item.collection_name)
                            if col.collection_set != collection_set:
                                imports.add(col.collection_set.app_name)

                            page_items[item_name] = (item, col)
                        else:
                            page_items[item_name] = (item, None)

                    generate_file(
                        target_path,
                        f'flutter/lib/src/pages/{app_name}/{name}.dart',
                        'flutter.page.dart.tpl', {
                            'app_name': app_name,
                            'app': collection_set,
                            'page': page,
                            'page_items': page_items,
                            'imports': imports,
                            'format_uri': format_uri,
                            'to_camel_case': to_camel_case,
                            'to_camel_case_classname': to_camel_case_classname,
                        }
                    )
                    generate_file(
                        target_path,
                        f'flutter/lib/src/pages/{app_name}/{name}_ui.dart',
                        'flutter.page.ui.dart.tpl', {
                            'app_name': app_name,
                            'app': collection_set,
                            'page': page,
                            'to_camel_case': to_camel_case,
                            'to_camel_case_classname': to_camel_case_classname,
                        }
                    )
    generate_file(target_path, 'flutter/lib/src/components/menu.dart', 'flutter.cmp.menu.dart.tpl')
    generate_file(target_path, 'flutter/lib/src/state.dart', 'flutter.state.dart.tpl')
    generate_file(target_path, 'flutter/lib/src/utils.dart', 'flutter.utils.dart.tpl')

    generate_file(
        target_path,
        f'flutter/lib/src/app.dart',
        'flutter.app.dart.tpl', {
            'apps': apps,
        }
    )

    max_len = 0
    app_routes = {}
    for app_name, app in apps.items():
        if app.flutter:
            for name, page in app.pages.items():
                if page.flutter and page.uri:
                    uri = format_uri(page.uri)
                    app_routes[uri] = f'{page.view_name}StateUi'
                    max_len = max(max_len, len(uri))

    generate_file(
        target_path,
        f'flutter/lib/src/routes.dart',
        'flutter.routes.dart.tpl', {
            'apps': apps,
            'app_routes': app_routes,
            'max_len': max_len,
            'len': len,
            'format_uri': format_uri,
            'to_camel_case': to_camel_case,
            'to_camel_case_classname': to_camel_case_classname,
        }
    )


def generate_react_jsx(target_path, app_name, collection_set):
    index_imports = ImportSet()

    react_pages = []

    for page in collection_set.pages.values():
        if page.react:
            for name, (imports, body, source) in page.react_components.items():
                generate_file(target_path, 'react/src/{}/Components/{}.jsx'.format(app_name.capitalize(), name),
                              'react.jsx.tpl', {
                                  'imports': imports.import_sting_js(),
                                  'name': name,
                                  'body': body,
                                  'source': source
                              })

            for name, (imports, body, source) in page.react_pages.items():
                index_imports.add(f'./Pages/{name}', '*' + name)
                index_imports.add(f'./Reducers/{name}Reducers', '*' + name + 'Reducer')
                react_pages.append(name)

                generate_file(target_path, 'react/src/{}/Reducers/{}Reducers.js'.format(app_name.capitalize(), name),
                              'react_reducer.js.tpl', {
                                  'name': name,
                              })

                generate_file(target_path, 'react/src/{}/Pages/{}.jsx'.format(app_name.capitalize(), name),
                              'react_page.jsx.tpl', {
                                  'imports': imports.import_sting_js(),
                                  'name': name,
                                  'body': body,
                                  'page': page,
                                  'source': source
                              })

    generate_file(target_path, 'react/src/{}/index.scss'.format(app_name.capitalize()), 'react.index.scss.tpl', {
        'pages': react_pages
    })
    generate_file(target_path, 'react/src/{}/index.jsx'.format(app_name.capitalize()), 'react.index.js.tpl', {
        'imports': index_imports.import_sting_js(),
        'pages': react_pages
    })


def generate_admin_py(target_path, app_name, collection_set):
    imports = ImportSet()
    imports.add('django.contrib', 'admin')
    imports.add('django', 'forms')

    for col in collection_set.collections.values():
        if not col.admin:
            continue

        imports.add('{}.models'.format(app_name), col.class_name)

        for class_import in col.admin.classes:
            imports.add(*class_import)

        if col.polymorphic:
            for child in col.child_collections:
                imports.add('{}.models'.format(app_name), child.class_name)

        # inlines
        for inline in col.admin.inlines:
            for declaration in inline.type_declarations:
                imports.add(*declaration)

            if inline.inline_type == 'polymorphic':
                for target_collection in inline.target_collection.child_collections:

                    if target_collection.translatable:
                        imports.add('cratis_i18n.admin', 'TranslatableInlineModelAdmin')

                    imports.add('{}.models'.format(app_name), target_collection.class_name)

            imports.add('{}.models'.format(app_name), inline.target_collection.class_name)

        for field in col.fields.values():
            if field.get_admin_widget():
                import_data, model_field = field.get_admin_widget()

                for source, what in import_data:
                    imports.add(source, what)

    generate_file(target_path, '{}/admin.py'.format(app_name), 'admin.py.tpl', {
        'imports': imports.import_sting(),
        'collection_set': collection_set,
        'collections': [(name, col) for name, col in collection_set.collections.items() if col.admin]
    })


def generate_translation_py(target_path, app_name, collection_set):
    imports = ImportSet()
    imports.add('modeltranslation.translator', 'translator')
    imports.add('modeltranslation.translator', 'TranslationOptions')

    for col in collection_set.collections.values():
        if not col.translatable:
            continue

        imports.add('{}.models'.format(app_name), col.class_name)

    generate_file(target_path, '{}/translation.py'.format(app_name), 'translation.py.tpl', {
        'imports': imports.import_sting(),
        'collections': [(name, col) for name, col in collection_set.collections.items() if col.translatable]
    })


def generate_serializers_py(target_path, app_name, collection_set):
    imports = ImportSet()
    imports.add('rest_framework', 'serializers')

    for col in collection_set.collections.values():
        if col.rest:
            for name, rest_conf in col.rest_conf.items():
                rest_conf.configure_model_imports(imports)

    generate_file(target_path, '{}/serializers.py'.format(app_name), 'serializers.py.tpl', {
        'imports': imports.import_sting(),
        'collection_set': collection_set,
        'collections': [(name, col) for name, col in collection_set.collections.items() if col.rest],
    })


def generate_views_py(target_path, app_name, collection_set):
    imports = ImportSet()

    for col in collection_set.collections.values():
        imports.add('{}.models'.format(app_name), col.class_name)

        if not col.rest:
            continue

        for rest_conf in col.rest_conf.values():
            rest_conf.configure_imports(imports)

    generated_templates = []
    if len(collection_set.pages.items()) > 0:
        imports.add('django.views.generic', 'TemplateView')

        for page in collection_set.pages.values():
            if collection_set.channels:
                imports.add('channels.layers', 'get_channel_layer')
            if page.stream:
                imports.add('channels.generic.websocket', 'AsyncWebsocketConsumer')
                imports.add('django.db.models.signals', 'post_save', 'm2m_changed', 'post_delete')
                imports.add('django_query_signals', 'post_bulk_create', 'post_delete as post_delete_bulk',
                            'post_get_or_create', 'post_update_or_create', 'post_update')
                imports.add('channels.db', 'database_sync_to_async')
                imports.add('asgiref.sync', 'async_to_sync')
                imports.add('asyncio', 'sleep')
                imports.add('django.dispatch', 'receiver')
                imports.add('zmei.json', 'ZmeiJsonEncoder')

            for import_spec in page.get_imports():
                imports.add(*import_spec)

            for item in page.page_items.values():
                for import_spec in item.get_imports():
                    imports.add(*import_spec)

            if page.template:
                template = page.defined_template_name
                if template:
                    template_name = '{app_name}/templates/{template}'.format(app_name=app_name, template=template, )

                    generate_file(target_path, template_name, 'theme/default.html', {
                        'app_name': app_name,
                        'page': page,
                        'parent': collection_set.resolve_page(page.parent_name) if page.parent_name else None
                    })

                    generated_templates.append(template_name)

    generate_file(target_path, '{}/views.py'.format(app_name), 'views.py.tpl', {
        'imports': imports.import_sting(),
        'collection_set': collection_set,
        'collections': [(name, col) for name, col in collection_set.collections.items() if col.rest],
        'pages': collection_set.pages.values()
    })


def generate_models_py(target_path, app_name, collection_set):
    imports = ImportSet()
    imports.add('django.db', 'models')

    for collection in collection_set.collections.values():  # type: CollectionDef

        for handlers, code in collection.signal_handlers:
            for signal_import in handlers:
                imports.add('django.dispatch', 'receiver')
                imports.add(*signal_import)

        if collection.polymorphic and collection.tree:
            imports.add('polymorphic_tree.models', 'PolymorphicMPTTModel', 'PolymorphicTreeForeignKey')
        else:
            if collection.polymorphic:
                imports.add('polymorphic.models', 'PolymorphicModel')

            if collection.tree:
                imports.add('mptt.models', 'MPTTModel', 'TreeForeignKey')

        if collection.validators:
            imports.add('django.core.exceptions', 'ValidationError')

        if collection.mixin_classes:
            for import_decl in collection.mixin_classes:
                pkg, cls, alias = import_decl
                if alias != cls:
                    cls = '{} as {}'.format(cls, alias)
                imports.add(*(pkg, cls))

        for field in collection.own_fields:  # type: FieldDef
            model_field = field.get_model_field()
            if model_field:
                import_data, model_field = model_field  # type: FieldDeclaration

                for source, what in import_data:
                    imports.add(source, what)

    generate_file(target_path, '{}/models.py'.format(app_name), 'models.py.tpl', {
        'imports': imports.import_sting(),
        'collection_set': collection_set,
        'collections': collection_set.collections.items()
    })
