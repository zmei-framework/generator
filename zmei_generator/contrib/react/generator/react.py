from zmei_generator.contrib.react.extensions.page.react import ReactPageExtension
from zmei_generator.generator.imports import ImportSet
from zmei_generator.generator.utils import generate_file


def generate(target_path, project):
    for app_name, application in project.applications_with(ReactPageExtension):

        index_imports = ImportSet()

        react_components = {}
        react_pages = {}

        react_pages = []

        for page in application.pages_with(ReactPageExtension):
            name = f'Page{page.name.capitalize()}'
            page_component_name = f'Page{page.name.capitalize()}Component'

            react_components_imports = ImportSet()
            react_components_imports.add('react', 'React')
            # react_components_imports.add(f'../Components/{el.tag}', '*' + el.tag)

            imports = ImportSet()
            imports.add('react', 'React')

            react_components_imports.add(f'../Reducers/{page_component_name}Reducers',
                                              f'*reloadPageDataAction')

            # self.react_components_imports.add(f'./{self.parent_component}', f'{{{self.parent_component}}}')

            var_names = ', '.join(page.page_item_names_with_parents)
            body = '\nconst {store, dispatch, children} = this.props;' \
                   '\nconst {%s} = store;\n\n' % var_names

            # react_components.update(react_components)

            # page.react_pages.update({page.page_component_name: (react_components_imports, body, 'lala')})

            # return '<div id="reactEl-%s">{{ react_page_%s|default:""|safe }}</div>' % (
            #     page_component_name,
            #     page_component_name
            # )
            source = ''

            generate_file(target_path, 'react/src/{}/Components/{}.jsx'.format(app_name.capitalize(), name),
                          'react.jsx.tpl', {
                              'imports': imports.import_sting_js(),
                              'name': name,
                              'body': body,
                              'source': source
                          })

            index_imports.add(f'./Pages/{name}', '*' + name)
            index_imports.add(f'./Reducers/{name}Reducers', '*' + name + 'Reducer')
            # react_pages.append(name)

            generate_file(target_path, 'react/src/{}/Reducers/{}Reducers.js'.format(app_name.capitalize(), name),
                          'react_reducer.js.tpl', {
                              'name': name,
                          })

            generate_file(target_path, 'react/src/{}/Pages/{}.jsx'.format(app_name.capitalize(), name),
                          'react_page.jsx.tpl', {
                              'imports': imports.import_sting_js(),
                              'name': name,
                              'body': body,
                              'page': page,
                              'source': source
                          })

        generate_file(target_path, 'react/src/{}/index.scss'.format(app_name.capitalize()), 'react.index.scss.tpl', {
            'pages': react_pages
        })
        generate_file(target_path, 'react/src/{}/index.jsx'.format(app_name.capitalize()), 'react.index.js.tpl', {
            'imports': index_imports.import_sting_js(),
            'pages': react_pages
        })

        entries = {}

        for app_name, application in project.applications.items():
            if application.react:
                # entries[app_name] = ["babel-polyfill", f'./src/{app_name.capitalize()}/index.jsx']
                entries[app_name] = [f'./src/index.jsx']

        packages = {}

        for app_name, application in project.applications.items():
            packages.update(application.react_deps)

        generate_file(target_path, 'react/package.json', 'package.json.tpl', {
            'packages': packages
        })
        generate_file(target_path, 'react/webpack.config.js', 'webpack.config.js.tpl', {
            'entries': entries
        })
