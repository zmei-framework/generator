


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

