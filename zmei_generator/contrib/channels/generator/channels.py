from zmei_generator.contrib.channels.extensions.application.channels import ChannelsAppExtension
from zmei_generator.contrib.channels.extensions.pages.stream import StreamPageExtension
from zmei_generator.generator.imports import ImportSet
from zmei_generator.generator.utils import generate_file


def generate(target_path, project):
    if not project.applications_support(ChannelsAppExtension):
        return

    streams = []
    imports = ImportSet()
    for app in project.applications.values():
        for page in app.pages_with(StreamPageExtension):
            streams.append((app, page))
            imports.add(f'{app.app_name}.views', f'{page.view_name}Consumer')

    generate_file(target_path, f'app/routing.py', 'channels.routing_main.tpl', context={
        'streams': streams,
        'imports': imports,
    })

    for app in project.applications.values():
        if app.pages_support(StreamPageExtension):
            imports = ImportSet()
            imports.add('channels.layers', 'get_channel_layer')
            imports.add('channels.generic.websocket', 'AsyncWebsocketConsumer')
            imports.add('django.db.models.signals', 'post_save', 'm2m_changed', 'post_delete')
            imports.add('django_query_signals', 'post_bulk_create', 'post_delete as post_delete_bulk',
                        'post_get_or_create', 'post_update_or_create', 'post_update')
            imports.add('channels.db', 'database_sync_to_async')
            imports.add('asgiref.sync', 'async_to_sync')
            imports.add('asyncio', 'sleep')
            imports.add('django.dispatch', 'receiver')
            imports.add('zmei.json', 'ZmeiJsonEncoder')

            generate_file(target_path, f'{app.app_name}/views_channels.py', 'channels.py.tpl', context={
                'pages': app.pages_with(StreamPageExtension),
                'ext': StreamPageExtension,
                'imports': imports,
            })
