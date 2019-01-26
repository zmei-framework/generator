
import itertools
import os
import shutil
import sys

import pkg_resources


def collect_items(entry_point, display_name):
    keywords_name_map = {}
    keywords_value_map = {}
    keywords = {}

    for entry_point in pkg_resources.iter_entry_points(entry_point):
        # print(dir(entry_point))

        try:
            data = entry_point.load()

            for name, value in data.items():
                if name in keywords_name_map:
                    print(f'Conflict: can not redefine {display_name} name "{name}"({entry_point.name}). '
                          f'it is already defined by entry point "{keywords_name_map[name]}"')
                if value in keywords_value_map:
                    print(f'Conflict: can not redefine {display_name} value "{value}"({entry_point.name}). '
                          f'it is already defined by entry point "{keywords_value_map[value]}"')

                keywords_name_map[name] = entry_point.name
                keywords_value_map[value] = entry_point.name
                keywords[name] = value

        except ImportError:
            print(entry_point)

    return keywords


def collect_files(entry_point, target_path):
    file_map = {}
    file_2_entry_point = {}

    for entry_point in pkg_resources.iter_entry_points(entry_point):
        try:
            data = entry_point.load()

            base_dir = os.path.dirname(sys.modules[entry_point.module_name].__file__)

            for name, file_path in data.items():
                file_name = os.path.basename(file_path)
                target_file = os.path.join(target_path, file_name)
                source_file = os.path.join(base_dir, file_path)

                if os.path.exists(target_file):
                    print(f'Conflict: file with name {file_name} already exist in target directory {target_path}')
                if file_name in file_2_entry_point:
                    print(f'Conflict: file with name {file_name} already added by entry point {file_2_entry_point[file_name]}')

                file_map[name] = source_file, target_file
                file_2_entry_point[file_name] = entry_point.name

        except ImportError:
            pass

    return file_map

def gen(grammar_path, target_path):

    print(os.getcwd())
    grammar_path = grammar_path
    target_path = target_path

    lexerSrc = f'{grammar_path}/ZmeiLangSimpleLexer.g4'
    parserSrc = f'{grammar_path}/ZmeiLangParser.g4'

    package = 'zmei_generator.parser.gen'

    antlr_jar = 'zmei_generator/lib/antlr/antlr-4.7.2-complete.jar'
    antlr = f'CLASSPATH="{antlr_jar}:." java -jar {antlr_jar}'

    lexer_cmd = f'{antlr}  -Dlanguage=Python3 -o {target_path} -package {package} -lib {os.path.realpath(grammar_path)} -listener {os.path.realpath(lexerSrc)}'
    os.system(lexer_cmd)

    parser_cmd = f'{antlr} -Dlanguage=Python3 -o {target_path} -package {package} -lib {os.path.realpath(target_path)} -listener {os.path.realpath(parserSrc)}'
    os.system(parser_cmd)

    # os.system('env')
def replace_in_file(file, markers):
    with open(file, 'r') as f:
        content = f.read()

    for marker, replacement in markers.items():
        content = content.replace(marker, replacement)

    with open(file, 'w') as f:
        f.write(content)


def build_parser():
    keywords = collect_items('zmei.grammar.keywords', 'keyword')
    tokens = collect_items('zmei.grammar.tokens', 'token')

    source_path = 'zmei_generator/ext/grammar'
    target_path = 'zmei_generator/parser/gen/grammar'

    if os.path.exists(target_path):
        shutil.rmtree(target_path)

    pages = collect_files('zmei.grammar.pages', target_path)
    applications = collect_files('zmei.grammar.app', target_path)
    models = collect_files('zmei.grammar.models', target_path)
    shutil.copytree(source_path, target_path)

    for source_file, target_file in itertools.chain.from_iterable(map(lambda x: x.values(), (pages, models, applications))):
        shutil.copy(source_file, target_file)

    replace_in_file('zmei_generator/parser/gen/grammar/PageExtra.g4', {
        '// {EXTRA_IMPORTS}': ',\n    '.join([os.path.basename(x[0])[:-3] for x in pages.values()]),
        '// {EXTRA_ANNOT}': ' ' + '\n    |'.join(pages.keys()),
    })
    replace_in_file('zmei_generator/parser/gen/grammar/ModelExtra.g4', {
        '// {EXTRA_IMPORTS}': ',\n    '.join([os.path.basename(x[0])[:-3] for x in models.values()]),
        '// {EXTRA_ANNOT}': ' ' + '\n    |'.join(models.keys()),
    })
    replace_in_file('zmei_generator/parser/gen/grammar/AppExtra.g4', {
        '// {EXTRA_IMPORTS}': ',\n    '.join([os.path.basename(x[0])[:-3] for x in applications.values()]),
        '// {EXTRA_ANNOT}': ' ' + '\n    |'.join(applications.keys()),
    })
    replace_in_file('zmei_generator/parser/gen/grammar/ZmeiLangSimpleLexer.g4', {
        '// {KEYWORDS}': '\n'.join([f"{name}: '{val}';" for name, val in keywords.items()]),
        '// {TOKENS}': '\n'.join([f"{name}: '{val}';" for name, val in tokens.items()]),
    })
    replace_in_file('zmei_generator/parser/gen/grammar/Base.g4', {
        '// {KEYWORDS}': '|' + '\n   |'.join(keywords.keys()),
    })

    gen(target_path, os.path.dirname(target_path))

