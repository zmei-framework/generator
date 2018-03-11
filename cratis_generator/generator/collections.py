from glob import glob

import os
import re

from cratis_generator.config.domain import CollectionSetDef, CollectionDef, FieldDef, FieldDeclaration, NoModelField
from cratis_generator.generator.imports import ImportSet
from cratis_generator.generator.utils import generate_feature, generate_file, is_file_generated


def list_apps():
    for filename in os.listdir('.'):
        if os.path.isfile(filename) and filename.endswith('.col'):
            if not re.match('^[a-zA-Z][a-zA-Z0-9_]+\.col$', filename):
                continue

            yield filename[0:-4]


def generate(app_name: str, collection_set: CollectionSetDef):
    url_imports = ImportSet()
    url_imports.add('django.conf.urls', 'url')

    for page in collection_set.pages.values():
        url_imports.add('.views', page.view_name)

        if page.i18n:
            url_imports.add('django.conf.urls.i18n', 'i18n_patterns')

    generate_feature(app_name, app_name.capitalize(), {
        'collection_set': collection_set,
        'url_imports': url_imports.import_sting()
    })

    # urls


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
        imports.add('cratis_api.api_filter', 'AnyFilterBackend')
        imports.add('cratis_api.views', 'Pagination')
        imports.add('rest_framework.permissions', 'AllowAny')

    for col in collection_set.collections.values():
        if not col.rest:
            continue

        imports.add('{}.models'.format(app_name), col.class_name)
        imports.add(*col.rest_class)

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
        if collection.polymorphic and collection.tree:
            imports.add('polymorphic_tree.models', 'PolymorphicMPTTModel', 'PolymorphicTreeForeignKey')
        else:
            if collection.polymorphic:
                imports.add('polymorphic.models', 'PolymorphicModel')

            if collection.tree:
                imports.add('mptt.models', 'MPTTModel', 'TreeForeignKey')

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



