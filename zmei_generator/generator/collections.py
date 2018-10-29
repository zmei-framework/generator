import json
import os
import re
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

    #config
    has_react = False
    has_rest = False
    has_admin = False
    has_filer = False
    has_suit = False

    # urls
    imports = set()
    urls = ['urlpatterns = [']
    urls += [
        "    url(r'^admin/', admin.site.urls),",
    ]
    react = False
    for app_name, collection_set in apps.items():
        if collection_set.react:
            react = True

        for import_def, url_def in collection_set.get_required_urls():
            urls.append(url_def)
            if import_def:
                imports.add(import_def)

        if collection_set.pages:
            urls.append(f"    url(r'^', include({app_name}.urls)),")
            imports.add(f'{app_name}.urls')

        if collection_set.admin:
            has_admin = True

        if collection_set.react:
            has_react = True

        if collection_set.suit:
            has_suit = True

        if collection_set.filer:
            has_filer = True

        if collection_set.api:
            has_rest = True
            urls.append(f"    url(r'^api/', include({app_name}.urls_rest)),")
            imports.add(f'{app_name}.urls_rest')

    urls.append(']')

    # urls
    with open(os.path.join(target_path, 'app/_urls.py'), 'w') as f:
        f.write('from django.conf.urls import url, include\n')
        f.write('from django.contrib import admin\n')

        f.write('\n')
        f.write('\n'.join([f'import {app_name}' for app_name in imports]))
        f.write('\n\n')
        f.write('\n'.join(urls))

    generate_file(target_path, 'app/urls.py', template_name='urls_main.py.tpl')

    # settings
    req_settings = {}
    installed_apps = list(apps.keys())
    if has_rest:
        installed_apps.append('rest_framework')

    extra_classes = set()
    for collection_set in apps.values():
        installed_apps.extend(collection_set.get_required_apps())
        req_settings.update(collection_set.get_required_settings())

        for extra in collection_set.extras:
            extra_classes.add(type(extra))

    installed_apps = list(set(installed_apps))

    with open(os.path.join(target_path, 'app/settings.py'), 'r') as fb:
        with open(os.path.join(target_path, 'app/_settings.py'), 'a') as f:
            f.write(fb.read())

            f.write('\nINSTALLED_APPS = [\n')
            f.write("\n    'app',\n")
            f.write('\n'.join([f"    '{app_name}'," for app_name in installed_apps]))
            f.write('\n] + INSTALLED_APPS\n\n')# settings

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
        'zmei-utils==0.1.9',
        'wheel',
        'django>2',
    ]

    if has_rest:
        requirements.append('djangorestframework')

    for collection_set in apps.values():
        requirements.extend(collection_set.get_required_deps())

    requirements = list(set(requirements))

    # requirements
    with open(os.path.join(target_path, '_requirements.txt'), 'w') as f:
        f.write('\n'.join(requirements))

    generate_file(target_path, 'requirements.txt', template_name='requirements.txt.tpl')

    # react
    if react:
        generate_react_configs(target_path, apps)


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
    generate_file(target_path, '{}/__init__.py'.format(app_name), 'init.py.tpl')

    if collection_set.rest:
        generate_serializers_py(target_path, app_name, collection_set)

    if collection_set.rest or len(collection_set.pages.values()) > 0:
        generate_views_py(target_path, app_name, collection_set)

    generate_file(target_path, '{}/templates/{}/base.html'.format(app_name, app_name), template_name='theme/base_app.html', context={
        'collection_set': collection_set,
    })

    # react templates
    if collection_set.react:
        generate_react_jsx(target_path, app_name, collection_set)


def generate_react_configs(target_path, apps):
    entries = {}

    for app_name, collection_set in apps.items():
        if collection_set.react:
            entries[app_name] = ["babel-polyfill", f'./src/{app_name.capitalize()}/index.jsx']

    packages = {}

    for app_name, collection_set in apps.items():
        packages.update(collection_set.react_deps)

    generate_file(target_path, 'react/package.json', 'package.json.tpl', {
        'packages': packages
    })
    generate_file(target_path, 'react/webpack.config.js', 'webpack.config.js.tpl', {
        'entries': entries
    })


def generate_react_jsx(target_path, app_name, collection_set):
    index_imports = ImportSet()

    react_pages = []

    for page in collection_set.pages.values():
        if page.react:
            for name, (imports, body, source) in page.react_components.items():

                generate_file(target_path, 'react/src/{}/Components/{}.jsx'.format(app_name.capitalize(), name), 'react.jsx.tpl', {
                    'imports': imports.import_sting_js(),
                    'name': name,
                    'body': body,
                    'source': source
                })

            for name, (imports, body, source) in page.react_pages.items():
                index_imports.add(f'./Pages/{name}', '*' + name)
                index_imports.add(f'./Reducers/{name}Reducers', '*' + name + 'Reducer')
                react_pages.append(name)

                generate_file(target_path, 'react/src/{}/Reducers/{}Reducers.js'.format(app_name.capitalize(), name), 'react_reducer.js.tpl', {
                    'name': name,
                })

                generate_file(target_path, 'react/src/{}/Pages/{}.jsx'.format(app_name.capitalize(), name), 'react_page.jsx.tpl', {
                    'imports': imports.import_sting_js(),
                    'name': name,
                    'body': body,
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
            imports.add('.models', col.class_name)

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

            for import_spec in page.get_imports():
                imports.add(*import_spec)

            for item in page.page_items.values():
                for import_spec in item.get_imports():
                    imports.add(*import_spec)

            template = page.defined_template_name
            if template:
                template_name = '{app_name}/templates/{template}'.format(app_name=app_name, template=template, )

                generate_file(target_path, template_name, 'theme/default.html', {
                    'app_name': app_name,
                    'page': page,
                    'parent': collection_set.pages[page.parent_name] if page.parent_name else None
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

        for signal_import, code in collection.signal_handlers:
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



