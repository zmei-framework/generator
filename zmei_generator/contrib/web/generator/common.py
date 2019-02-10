import os

from zmei_generator.generator.utils import generate_file, format_file, generate_package


def generate(target_path, project):

    # config
    has_rest = False
    has_i18n_pages = False
    has_normal_pages = False

    i18n_langs = []

    # urls
    imports = set()
    urls = ['urlpatterns = [']
    urls += [
        "    url(r'^admin/', admin.site.urls),",
    ]
    for app_name, application in project.applications.items():
        generate_package(app_name, path=target_path)

    for app_name, application in project.applications.items():
        for import_def, url_def in application.get_required_urls():
            urls.append(url_def)
            if import_def:
                imports.add(import_def)

        if application.pages:
            for page in application.pages.values():
                if page.i18n:
                    has_i18n_pages = True
                else:
                    has_normal_pages = True

            if has_normal_pages:
                urls.append(f"    url(r'^', include({app_name}.urls)),")
                imports.add(f'{app_name}.urls')

    urls.append(']')

    for app_name, application in project.applications.items():
        if any([page.i18n for page in application.pages.values()]):
            urls += [
                'urlpatterns += i18n_patterns(',
                f"    url(r'^', include({app_name}.urls_i18n)),",
                ")"
            ]
            imports.add(f'{app_name}.urls_i18n')

    # urls
    with open(os.path.join(target_path, 'app/_urls.py'), 'w') as f:
        f.write('from django.conf.urls import url, include\n')
        f.write('from django.contrib import admin\n')

        f.write('\n')
        f.write('\n'.join([f'import {app_name}' for app_name in imports]))
        if has_i18n_pages:
            f.write('\nfrom django.conf.urls.i18n import i18n_patterns\n')
        f.write('\n\n')
        f.write('\n'.join(urls))

    generate_file(target_path, 'app/urls.py', template_name='urls_main.py.tpl')

    # settings
    req_settings = {}
    installed_apps = [app.app_name for app in project.applications.values() if len(app.pages) > 0 or len(app.models) > 0]

    extension_classes = list()
    for application in sorted(project.applications.values(), key=lambda x: x.app_name):
        installed_apps.extend(application.get_required_apps())
        req_settings.update(application.get_required_settings())

        for extension in application.extensions:
            if type(extension) not in extension_classes:
                extension_classes.append(type(extension))

    # remove duplicates preserving order
    seen = set()
    seen_add = seen.add
    installed_apps = [x for x in installed_apps if not (x in seen or seen_add(x))]

    with open(os.path.join(target_path, 'app/settings.py'), 'r') as fb:
        with open(os.path.join(target_path, 'app/_settings.py'), 'a') as f:
            f.write(fb.read())

            f.write('\nINSTALLED_APPS = [\n')
            f.write("\n    'app',\n")
            f.write('\n'.join([f"    '{app_name}'," for app_name in installed_apps]))
            f.write('\n] + INSTALLED_APPS\n\n')  # settings

            for key, val in req_settings.items():
                f.write(f'{key} = {repr(val)}\n')

            for extension in extension_classes:
                extension.write_settings(project.applications, f)

    generate_file(target_path, 'app/settings.py', template_name='settings.py.tpl')
    format_file(target_path, 'app/_settings.py')

    for extension in extension_classes:
        extension.generate(project.applications, target_path)

    # base template
    generate_file(target_path, 'app/templates/base.html', template_name='theme/base.html')

    requirements = [
        'wheel',
        'django>2',
    ]

    for application in project.applications.values():
        requirements.extend(application.get_required_deps())

    requirements = list(sorted(set(requirements)))

    # requirements
    with open(os.path.join(target_path, '_requirements.txt'), 'w') as f:
        f.write('\n'.join(requirements))

    generate_file(target_path, 'requirements.txt', template_name='requirements.txt.tpl')

    if i18n_langs:
        for lang in i18n_langs:
            os.makedirs(os.path.join(target_path, f'locale/{lang}'))
            with open(os.path.join(target_path, f'locale/{lang}/readme.txt'), 'w') as f:
                f.write('Collect translations:\n')
                f.write('django-admin makemessages --all\n')
                f.write('\n')
                f.write('Compile translations:\n')
                f.write('django-admin compilemessages\n')


