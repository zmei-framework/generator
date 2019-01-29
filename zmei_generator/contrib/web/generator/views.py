from zmei_generator.generator.imports import ImportSet
from zmei_generator.generator.utils import generate_file, generate_urls_file, ThemeConfig


def generate(target_path, project):
    for app_name, application in project.applications.items():
        if not len(application.pages):  # and not application.rest:
            continue

        imports = ImportSet()

        for col in application.models.values():
            imports.add('{}.models'.format(app_name), col.class_name)

        #
        # todo get rest working back
        #     if not col.rest:
        #         continue
        #
        #     for rest_conf in col.rest_conf.values():
        #         rest_conf.configure_imports(imports)

        generated_templates = []
        if len(application.pages.items()) > 0:
            imports.add('django.views.generic', 'TemplateView')

            for page in application.pages.values():
                # TODO: get channels & router working back
                # if application.channels:
                #     imports.add('channels.layers', 'get_channel_layer')
                # if page.stream:
                #     imports.add('channels.generic.websocket', 'AsyncWebsocketConsumer')
                #     imports.add('django.db.models.signals', 'post_save', 'm2m_changed', 'post_delete')
                #     imports.add('django_query_signals', 'post_bulk_create', 'post_delete as post_delete_bulk',
                #                 'post_get_or_create', 'post_update_or_create', 'post_update')
                #     imports.add('channels.db', 'database_sync_to_async')
                #     imports.add('asgiref.sync', 'async_to_sync')
                #     imports.add('asyncio', 'sleep')
                #     imports.add('django.dispatch', 'receiver')
                #     imports.add('zmei.json', 'ZmeiJsonEncoder')

                for import_spec in page.get_imports():
                    imports.add(*import_spec)

                for item in page.page_items.values():
                    for import_spec in item.get_imports():
                        imports.add(*import_spec)

                if page.template:
                    template = page.defined_template_name
                    if template:
                        template_name = f'{app_name}/templates/{template}'

                        generate_file(target_path, template_name, 'theme/default.html', {
                            'app_name': app_name,
                            'page': page,
                            'parent': application.resolve_page(page.parent_name) if page.parent_name else None
                        })

                        generated_templates.append(template_name)

        generate_file(target_path, '{}/views.py'.format(app_name), 'views.py.tpl', {
            'imports': imports.import_sting(),
            'application': application,
            # 'models': [(name, col) for name, col in application.models.items() if col.rest],
            'pages': application.pages.values()
        })


        # urls
        pages_i18n = [page for page in application.pages.values() if page.has_uri and page.i18n]
        if len(pages_i18n) > 0:
            generate_urls_file(
                target_path,
                app_name,
                application,
                pages_i18n,
                i18n=True
            )

        # urls i18n
        pages = [page for page in application.pages.values() if page.has_uri and not page.i18n]
        if application.pages:
            generate_urls_file(
                target_path,
                app_name,
                application,
                pages,
                i18n=False
            )

        if len(application.pages) > 0:
            generate_file(target_path, '{}/templates/{}/_base.html'.format(app_name, app_name),
                          template_name='theme/base_app.html', context={
                    'application': application,
                })

