
if has_channels:
    streams = []
    imports = ImportSet()
    for app in apps.values():
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
