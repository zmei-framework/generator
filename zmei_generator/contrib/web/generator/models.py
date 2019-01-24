



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
