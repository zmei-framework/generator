from zmei_generator.contrib.channels.extensions.application.channels import ChannelsAppExtension
from zmei_generator.generator.imports import ImportSet
from zmei_generator.generator.utils import generate_file


def generate(target_path, project):
    if not project.applications_support(ChannelsAppExtension):
        return

    streams = []
    imports = ImportSet()
    for app in project.applications_with(ChannelsAppExtension):
        for page in app.pages.values():
            if page.stream:
                streams.append((app, page))
                imports.add(f'{app.app_name}.views', f'{page.view_name}Consumer')

    generate_file(target_path, f'app/routing.py', 'channels.routing_main.tpl', context={
        'streams': streams,
        'imports': imports,
    })
