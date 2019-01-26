from zmei_generator.generator.imports import ImportSet
from zmei_generator.generator.utils import generate_file


def generate(target_path, app):
    for app_name, collection_set in app.collection_sets.items():
        index_imports = ImportSet()

        react_pages = []

        for page in collection_set.pages.values():
            if page.react:
                for name, (imports, body, source) in page.react_components.items():
                    generate_file(target_path, 'react/src/{}/Components/{}.jsx'.format(app_name.capitalize(), name),
                                  'react.jsx.tpl', {
                                      'imports': imports.import_sting_js(),
                                      'name': name,
                                      'body': body,
                                      'source': source
                                  })

                for name, (imports, body, source) in page.react_pages.items():
                    index_imports.add(f'./Pages/{name}', '*' + name)
                    index_imports.add(f'./Reducers/{name}Reducers', '*' + name + 'Reducer')
                    react_pages.append(name)

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

        for app_name, collection_set in app.collection_sets.items():
            if collection_set.react:
                # entries[app_name] = ["babel-polyfill", f'./src/{app_name.capitalize()}/index.jsx']
                entries[app_name] = [f'./src/index.jsx']

        packages = {}

        for app_name, collection_set in app.collection_sets.items():
            packages.update(collection_set.react_deps)

        generate_file(target_path, 'react/package.json', 'package.json.tpl', {
            'packages': packages
        })
        generate_file(target_path, 'react/webpack.config.js', 'webpack.config.js.tpl', {
            'entries': entries
        })
