import json
import os
import random
import re
import string
from os import unlink
from shutil import copytree, copyfile, rmtree

from zmei_generator.domain.collection_set_def import FieldDeclaration, CollectionSetDef
from zmei_generator.domain.field_def import FieldDef
from zmei_generator.generator.imports import ImportSet
from zmei_generator.generator.utils import generate_feature, generate_file, generate_urls_file, generate_urls_rest, \
    format_file



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




def generate(target_path, app_name: str, collection_set: CollectionSetDef, features=None):
    features = features or []

    features = type('features', (object,), {x: x in features for x in [
        'cratis', 'django'
    ]})
    collection_set.features = features
