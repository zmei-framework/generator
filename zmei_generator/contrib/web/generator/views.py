



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

    if len(collection_set.pages) > 0:
        generate_file(target_path, '{}/templates/{}/_base.html'.format(app_name, app_name),
                      template_name='theme/base_app.html', context={
                'collection_set': collection_set,
            })

