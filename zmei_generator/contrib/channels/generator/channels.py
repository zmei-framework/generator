from zmei_generator.generator.imports import ImportSet
from zmei_generator.generator.utils import generate_file


def generate(target_path, app):
    streams = []
    imports = ImportSet()
    for app in app.applications.values():
        if not app.channels:
            continue
        for page in app.pages.values():
            if page.stream:
                streams.append((app, page))
                imports.add(f'{app.app_name}.views', f'{page.view_name}Consumer')

    generate_file(target_path, f'app/routing.py', 'channels.routing_main.tpl', context={
        'streams': streams,
        'imports': imports,
    })
