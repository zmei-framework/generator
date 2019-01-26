import os
import subprocess

from zmei_generator.contrib.web.fields.relation import RelationDef
from zmei_generator.domain.reference_field import ReferenceField
from zmei_generator.generator.utils import generate_file, to_camel_case, format_uri, to_camel_case_classname


def generate(target_path, app):
    apps = app.collection_sets
    # for app_name, collection_set in app.collection_sets.items():

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


    flutter_dir = os.path.join(target_path, 'flutter')
    if os.path.exists(flutter_dir):
        subprocess.check_call(['dartfmt', '-w', '-l', '120', flutter_dir], stdout=subprocess.DEVNULL)

