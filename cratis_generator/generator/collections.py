from glob import glob
from shutil import copytree, rmtree

import os
import re
from subprocess import Popen

import tempfile

from cratis_generator.config.domain import CollectionSetDef, CollectionDef, FieldDef, FieldDeclaration, NoModelField
from cratis_generator.generator.imports import ImportSet
from cratis_generator.generator.utils import generate_feature, generate_file, is_file_generated, \
    generate_urls_file, generate_urls_rest, chdir, fill_file


def list_apps():
    for filename in os.listdir('.'):
        if os.path.isfile(filename) and filename.endswith('.col'):
            if not re.match('^[a-zA-Z][a-zA-Z0-9_]+\.col$', filename):
                continue

            yield filename[0:-4]


def generate_common_files(apps, features=None):
    features = type('features', (object,), {x: x in features for x in [
        'cratis', 'django'
    ]})

    if features.django:
        env = os.environ.copy()
        del env['DJANGO_SETTINGS_MODULE']

        Popen(['django-admin', 'startproject', 'app'], env=env).wait()
        os.system('mv app tmp')
        os.system('mv tmp/* .')
        os.system('rm -rf tmp')

        #config
        has_rest = False
        has_admin = False

        # urls
        imports = set()
        urls = ['urlpatterns = [']
        urls += [
            "    url(r'^admin/', admin.site.urls),",
        ]
        for app_name, collection_set in apps.items():
            if collection_set.pages:
                urls.append(f"    url(r'^', include({app_name}.urls)),")
                imports.add(f'{app_name}.urls')

            if collection_set.admin:
                has_admin = True

            if collection_set.rest:
                has_rest = True
                urls.append(f"    url(r'^api/', include({app_name}.urls_rest)),")
                imports.add(f'{app_name}.urls_rest')

        urls.append(']')

        # urls
        with open('app/urls.py', 'w') as f:
            f.write('from django.conf.urls import url, include\n')
            f.write('from django.contrib import admin\n')

            f.write('\n')
            f.write('\n'.join([f'import {app_name}' for app_name in imports]))
            f.write('\n\n')
            f.write('\n'.join(urls))

        # settings
        installed_apps = list(apps.keys())
        if has_rest:
            installed_apps.append('rest_framework')
        if has_admin:
            if features.cratis:
                installed_apps.append('django_select2')

        with open('app/settings.py', 'a') as f:
            f.write('\nINSTALLED_APPS += [\n')
            f.write("\n    'app',\n")
            f.write('\n'.join([f"    '{app_name}'," for app_name in installed_apps]))
            f.write('\n]\n')# settings

        # base template
        generate_file('app/templates/base.html', template_name='theme/base.html')

        # requirements
        with open('requirements.txt', 'w') as f:
            f.write('django\n')
            if has_rest:
                f.write('djangorestframework\n')
            if has_admin:
                if features.cratis:
                    f.write('django-select2\n')


def generate(app_name: str, collection_set: CollectionSetDef, features=None):
    features = features or []
    features = type('features', (object,), {x: x in features for x in [
        'cratis', 'django'
    ]})
    collection_set.features = features

    # urls
    pages_i18n = [page for page in collection_set.pages.values() if page.has_uri and page.i18n]
    if len(pages_i18n) > 0:
        generate_urls_file(
            app_name,
            collection_set,
            pages_i18n,
            i18n=True
        )
    else:
        if os.path.exists('{}/urls_i18n.py'.format(app_name)):
            os.unlink('{}/urls_i18n.py'.format(app_name))

    # urls i18n
    pages = [page for page in collection_set.pages.values() if page.has_uri and not page.i18n]
    if len(pages) > 0:
        generate_urls_file(
            app_name,
            collection_set,
            pages,
            i18n=False
        )
    else:
        if os.path.exists('{}/urls.py'.format(app_name)):
            os.unlink('{}/urls.py'.format(app_name))

    # urls rest
    if collection_set.rest:
        generate_urls_rest(app_name, collection_set)
    else:
        if os.path.exists('{}/urls_rest.py'.format(app_name)):
            os.unlink('{}/urls_rest.py'.format(app_name))

    if features.cratis:
        # features
        generate_feature(app_name, app_name.capitalize(), {
            'collection_set': collection_set,
            'pages_i18n': pages_i18n,
            'pages': pages
        })

    # Models

    if len(collection_set.collections.values()) > 0:
        generate_models_py(app_name, collection_set)
    else:
        if os.path.exists('{}/models.py'.format(app_name)):
            os.unlink('{}/models.py'.format(app_name))

    # translations

    if collection_set.translatable:
        generate_translation_py(app_name, collection_set)
    else:
        if os.path.exists('{}/translation.py'.format(app_name)):
            os.unlink('{}/translation.py'.format(app_name))

    # admin

    if collection_set.admin:
        generate_admin_py(app_name, collection_set)
    else:
        if os.path.exists('{}/admin.py'.format(app_name)):
            os.unlink('{}/admin.py'.format(app_name))

    # views

    generate_file('{}/__init__.py'.format(app_name), 'init.py.tpl')

    if collection_set.rest or len(collection_set.pages.values()) > 0:
        generate_views_py(app_name, collection_set)
    else:
        if os.path.exists('{}/views.py'.format(app_name)):
            os.unlink('{}/views.py'.format(app_name))



def generate_admin_py(app_name, collection_set):
    imports = ImportSet()
    imports.add('django.contrib', 'admin')
    imports.add('django', 'forms')

    for col in collection_set.collections.values():
        if not col.admin:
            continue

        imports.add('{}.models'.format(app_name), col.class_name)

        for class_import in col.admin_classes:
            imports.add(*class_import)

        if col.polymorphic:
            for child in col.child_collections:
                imports.add('{}.models'.format(app_name), child.class_name)

        # inlines
        for inline in col.admin_inlines:
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

    generate_file('{}/admin.py'.format(app_name), 'admin.py.tpl', {
        'imports': imports.import_sting(),
        'collection_set': collection_set,
        'collections': [(name, col) for name, col in collection_set.collections.items() if col.admin]
    })

def generate_translation_py(app_name, collection_set):
    imports = ImportSet()
    imports.add('modeltranslation.translator', 'translator')
    imports.add('modeltranslation.translator', 'TranslationOptions')

    for col in collection_set.collections.values():
        if not col.translatable:
            continue

        imports.add('{}.models'.format(app_name), col.class_name)

    generate_file('{}/translation.py'.format(app_name), 'translation.py.tpl', {
        'imports': imports.import_sting(),
        'collections': [(name, col) for name, col in collection_set.collections.items() if col.translatable]
    })


def generate_views_py(app_name, collection_set):
    imports = ImportSet()

    if collection_set.rest:
        imports.add('rest_framework', 'serializers')
        # imports.add('cratis_api.api_filter', 'AnyFilterBackend')
        # imports.add('cratis_api.views', 'Pagination')



    for col in collection_set.collections.values():
        if not col.rest:
            continue

        imports.add('{}.models'.format(app_name), col.class_name)

        col.rest_conf.configure_imports(imports)

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

                generate_file(template_name, 'theme/default.html', {
                    'page': page,
                    'parent': collection_set.pages[page.parent_name] if page.parent_name else None
                })

                generated_templates.append(template_name)

    for template in glob(f'{app_name}/templates/**/*.html', recursive=True):
        if template not in generated_templates and is_file_generated(template):
            os.unlink(template)


    generate_file('{}/views.py'.format(app_name), 'views.py.tpl', {
        'imports': imports.import_sting(),
        'collection_set': collection_set,
        'collections': [(name, col) for name, col in collection_set.collections.items() if col.rest],
        'pages': collection_set.pages.values()
    })


def generate_models_py(app_name, collection_set):
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
            model_field = field.get_model_field(collection)
            if model_field:
                import_data, model_field = model_field  # type: FieldDeclaration

                for source, what in import_data:
                    imports.add(source, what)

    generate_file('{}/models.py'.format(app_name), 'models.py.tpl', {
        'imports': imports.import_sting(),
        'collection_set': collection_set,
        'collections': collection_set.collections.items()
    })



