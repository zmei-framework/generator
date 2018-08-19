import os
import re
import sys
from glob import glob

files = {
    'config/extras.py': 'ee.negative.genius.domain',
    'config/fields.py': 'ee.negative.genius.ext.fields',
    'config/domain.py': 'ee.negative.genius.domain',
    # 'config/grammar.py': 'ee.negative.genius.domain',
    'config/parser.py': 'ee.negative.genius.domain',
    'generator/imports.py': 'ee.negative.genius.domain',
    'generator/collections.py': 'ee.negative.genius.generator',
    'generator/utils.py': 'ee.negative.genius.generator',
    'fields/relation.py': 'ee.negative.genius.ext.fields',
    'fields/filer.py': 'ee.negative.genius.ext.fields',
    'fields/bool.py': 'ee.negative.genius.ext.fields',
    'fields/number.py': 'ee.negative.genius.ext.fields',
    'fields/text.py': 'ee.negative.genius.ext.fields',
    'fields/expression.py': 'ee.negative.genius.ext.fields',
    'fields/date.py': 'ee.negative.genius.ext.fields',
    'fields/image.py': 'ee.negative.genius.ext.fields',
    'extras/tree.py': 'ee.negative.genius.ext.extras',
    'extras/clean.py': 'ee.negative.genius.ext.extras',
    'extras/mixin.py': 'ee.negative.genius.ext.extras',
    'extras/rest.py': 'ee.negative.genius.ext.extras',
    'extras/sortable.py': 'ee.negative.genius.ext.extras',
    'extras/admin.py': 'ee.negative.genius.ext.extras',
    'extras/document.py': 'ee.negative.genius.ext.extras',
    'extras/dates.py': 'ee.negative.genius.ext.extras',
    'extras/db_signals.py': 'ee.negative.genius.ext.extras',
    'extras/page/auth.py': 'ee.negative.genius.ext.page_extras',
    'extras/page/block.py': 'ee.negative.genius.ext.page_extras',
    'extras/page/crud.py': 'ee.negative.genius.ext.page_extras',
    'extras/page/form.py': 'ee.negative.genius.ext.page_extras',
    'extras/page/menu.py': 'ee.negative.genius.ext.page_extras',
    'extras/page/merge.py': 'ee.negative.genius.ext.page_extras',
    'extras/page/page_handlers.py': 'ee.negative.genius.ext.page_extras',
    'extras/page/post.py': 'ee.negative.genius.ext.page_extras',
    'extras/page/rss.py': 'ee.negative.genius.ext.page_extras',
}

for file, package in files.items():
    source = f'/Users/aleksandrrudakov/dev/generator/cratis_generator/{file}'
    target = f'/Users/aleksandrrudakov/dev/genius-core/generator/src/main/kotlin/{package.replace(".", "/")}'

    if not os.path.exists(target):
        os.makedirs(target)


    def dump_class(name, parent, body):
        if not name:
            return

        with open(f'{target}/{name}.kt', 'w') as f:
            f.write(f"""
package {package}

class {name}{': ' + parent + '()' if parent and parent != 'object' else '' } {{
{ body }
}}
            """)

    with open(source) as f:
        cls = None
        parent = None
        body = ''

        is_property = False

        ident_levels = []

        for line in f.readlines():

            ident_amt = len(re.match('(\s*)', line).group(1))

            if line.strip() != '' and len(ident_levels):
                while len(ident_levels) and ident_levels[-1] >= ident_amt:
                    body += '    }\n\n'
                    ident_levels.pop()


            m = re.match('^class\s+([\w0-9]+)\(([^\)]+)\)\s*:\s*', line)
            if m:
                dump_class(cls, parent, body)
                body = ''

                cls = m.group(1).strip()
                parent = m.group(2).strip()
            else:
                if not cls:
                    continue

                code = line.strip()

                if code == 'pass':
                    continue

                m = re.match('^def\s+([\w0-9]+)\(\s*self\s*,?\s*([^\)]+)?\)(\s*->\s*([^:]+)\s*)?\s*:\s*$', code)
                if m:

                    func_name = m.group(1).strip()
                    func_args = m.group(2)
                    func_ret = m.group(4)

                    if func_args:
                        func_args = func_args.strip()

                    if func_ret:
                        func_ret = func_ret.strip()


                    # if not func_ret:
                    #     func_ret = ':Any'
                    # else:
                    #     if func_ret == 'None':
                    #         func_ret = 'Any'
                    # func_ret = ': ' + func_ret
                    func_ret = ''

                    if func_name == '__init__':
                        func_name = 'init'

                    if func_args:
                        func_args = ', '.join([f'{x.strip()}: Any' for x in func_args.split(',')])
                    else:
                        func_args = ''

                    if is_property:
                        body += f'    val {func_name}{func_ret}\n        get() {{\n'
                    else:
                        body += f'    fun {func_name}({func_args}){func_ret} {{\n'

                    is_property = False

                    ident_levels.append(ident_amt)

                    continue


                if code == '@property':
                    is_property = True
                    continue

                if code.startswith('#'):
                    continue

                line = line.replace('False', 'false')
                line = line.replace('True', 'true')
                line = line.replace('None', 'null')
                line = line.replace('raise ', 'throw ')
                line = line.replace('self.', '')
                line = line.replace('{}', 'mutableMapOf<String, Any>()')
                line = line.replace('[]', 'mutableListOf<Any>()')

                m = re.match('^\s*(for|try|except|if|else|elif)\s*([^:]+)?\s*:\s*$', line)
                if m:
                    con = m.group(1)
                    if con == 'elif':
                        con = 'else if'
                    if con == 'except':
                        con = 'catch'

                    expr = m.group(2)
                    if expr:
                        expr = f' ({expr})'
                    else:
                        expr = ''

                    body += f'        {con}{expr} {{\n'

                    ident_levels.append(ident_amt)
                    continue

                body += '    ' + line

        dump_class(cls, parent, body)

        # parts =
        #
        # for part in parts:
        #
        #     print('>>' * 200)
        #     print(part)