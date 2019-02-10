from zmei_generator.generator.imports import ImportSet
from zmei_generator.generator.utils import generate_file, generate_urls_file, ThemeConfig, generate_package


def generate(target_path, project):
    has_views = False

    for app_name, application in project.applications.items():
        if not len(application.pages):  # and not application.rest:
            continue
        has_views = True

        imports = ImportSet()

        for col in application.models.values():
            imports.add('{}.models'.format(app_name), col.class_name)

        generated_templates = []
        if len(application.pages.items()) > 0:
            imports.add('django.views.generic', 'TemplateView')

            for page in application.pages.values():

                if not page.parent_name:
                    imports.add('app.utils.views', 'Data')

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

    if has_views:
        generate_package('app.utils', path=target_path)
        generate_file(target_path, 'app/utils/views.py', template_name='views.utils.py.tpl')

