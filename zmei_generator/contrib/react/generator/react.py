import re
import sys
from textwrap import indent, dedent

from zmei_generator.contrib.channels.extensions.pages.stream import StreamPageExtension
from zmei_generator.contrib.react.extensions.page.react import ReactPageExtension
from zmei_generator.generator.imports import ImportSet
from zmei_generator.generator.utils import generate_file, format_uri

REACT_IMPORT_RX = re.compile('^import\s+((\*\s+as\s+)?[a-zA-Z0-9_]+)?\s*,?\s*({\s*([a-zA-Z0-9_]+\s*(,\s*[a-zA-Z0-9_]+)*)\s*})?\s+from\s+"([^;]+)";$', re.MULTILINE)


def to_camel_case(name):
    return ''.join([x.capitalize() for x in name.split('_')])

def generate(target_path, project):
    has_react = False

    react_pages = []
    react_pages_by_app = {}
    index_imports = ImportSet()

    for app_name, application in project.applications.items():
        if not application.pages_support(ReactPageExtension):
            continue

        has_react = True

        react_pages_by_app[app_name] = {}

        app_cmp_name = to_camel_case(app_name)

        for name, page in application.pages.items():
            ext = page.get_own_or_parent_extension(ReactPageExtension)
            if not ext:
                continue

            page_cmp_name = to_camel_case(page.name)

            name = f'{page_cmp_name}Page'
            name_ui = f'{page_cmp_name}Ui'

            if page.uri:
                react_pages.append((app_cmp_name, name_ui, format_uri(page.uri)))
                react_pages_by_app[app_name][page.name] = format_uri(page.uri)

            page_component_name = f'Page{page_cmp_name}'

            react_components_imports = ImportSet()
            react_components_imports.add('react', 'React')
            # react_components_imports.add(f'../Components/{el.tag}', '*' + el.tag)

            imports = ImportSet()
            imports.add('react', 'React')
            imports.add(f'../../layout', 'BaseLayout')
            imports.add(f'../layouts/{app_cmp_name}Layout', f'{app_cmp_name}Layout')

            react_components_imports.add(f'../Reducers/{page_component_name}Reducers',
                                         f'*reloadPageDataAction')

            index_imports.add(f'./pages/{name}', '*' + name)

            wrappers = [
                f'PageContextProvider',
                f'BaseLayout',
                f'{app_cmp_name}Layout'
            ]

            def wrap(source, cmp_list):
                source = indent(source, '    ')

                if not len(cmp_list):
                    return dedent(source)

                w = cmp_list.pop()

                return wrap(f'<{w} {{...this.props}} page={{this}}>\n{source}\n</{w}>', wrappers)

            blocks_rendered = {}
            for area, blocks in page.get_blocks(platform=ReactPageExtension).items():
                blocks_rendered[area] = []
                for index, block in enumerate(blocks):

                    rendered = block.render(area=area, index=index)

                    import_section, rendered = rendered.split('<', maxsplit=1)

                    for im in REACT_IMPORT_RX.findall(import_section):
                        what = ['*' + x.strip() for x in im[3].split(',') if x != '']
                        def_what = im[0].strip(' ,')

                        if len(def_what):
                            what.append(def_what)
                        src = im[5]

                        imports.add(src, *what)

                    rendered = '<' + rendered

                    blocks_rendered[area].append((block.ref, rendered))

            streams = page.list_own_or_parent_extensions(StreamPageExtension)
            generate_file(target_path, 'react/src/{}/pages/{}.jsx'.format(app_name, name),
                          'react/page.jsx.tpl', {
                              'imports': imports.import_sting_js(),
                              'name': name,
                              'page': page,
                              'blocks': blocks_rendered,
                              'ext': ReactPageExtension,
                              'app_name': app_name,
                              'streams': streams,
                              'to_camel_case': to_camel_case,
                              'source': wrap('{this.renderContent()}', wrappers)
                          })

            ui_imports = ImportSet()
            ui_imports.add('react', 'React')
            ui_imports.add(f'../pages/{name}', name)

            generate_file(target_path, f'react/src/{app_name}/ui/{name_ui}.jsx',
                          'react/ui.jsx.tpl', {
                              'imports': ui_imports.import_sting_js(),
                              'parent': name,
                              'name': name_ui
                          })

        generate_file(target_path, f'react/src/{app_name}/layouts/{app_cmp_name}Layout.jsx',
                      'react/cmp.jsx.tpl', {
                          'name': f'{app_cmp_name}Layout',
                          'source': '<>{children}</>'
                      })

        if not len(react_pages_by_app[app_name]):
            del react_pages_by_app[app_name]

    if has_react:
        generate_file(target_path, f'react/src/layout.jsx',
                      'react/cmp.jsx.tpl', {
                          'name': f'BaseLayout',
                          'source': '<>{children}</>'
                      })
        generate_file(target_path, f'react/src/index.scss', 'react/index.scss.tpl', {
            'pages': react_pages
        })
        generate_file(target_path, 'app/utils/react.py', 'react/utils.py.tpl')
        generate_file(target_path, 'react/src/index.jsx', 'react/index.jsx.tpl')
        generate_file(target_path, 'react/src/state.jsx', 'react/state.js.tpl')
        generate_file(target_path, 'react/src/streams.jsx', 'react/streams.js.tpl')
        generate_file(target_path, 'react/src/reducer.jsx', 'react/reducer.js.tpl', {
            'name': 'Root'
        })
        generate_file(target_path, 'react/src/router.jsx', 'react/router.jsx.tpl', {
            'name': 'Root',
            'pages': react_pages,
            'pages_index': react_pages_by_app,
            'to_camel_case': to_camel_case
        })

        generate_file(target_path, 'react/package.json', 'react/package.json.tpl', {
            'packages': {}
        })
        generate_file(target_path, 'react/webpack.config.js', 'react/webpack.config.js.tpl', {
            'entries': {'all': f'./src/index.jsx'}
        })
