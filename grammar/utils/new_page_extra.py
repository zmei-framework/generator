import sys

bp = '/Users/aleksandrrudakov/dev/zmei/generator/grammar'
lexer = '/Users/aleksandrrudakov/dev/zmei/generator/grammar/ZmeiLangSimpleLexer.g4'

name = sys.argv[1]


tpl = """
parser grammar {};

options {{ tokenVocab=ZmeiLangSimpleLexer; }}

import Base;

an_{}:
    AN_{}
    (BRACE_OPEN
    BRACE_CLOSE)?
    ;
"""

tpl_py = """
from zmei_generator.config.extras import PageExtra
from zmei_generator.parser.gen.ZmeiLangParser import ZmeiLangParser
from zmei_generator.parser.utils import BaseListener

class {}PageExtra(PageExtra):
    # {}
    pass
    
class {}PageExtraParserListener(BaseListener):

    def enterAn_{}(self, ctx: ZmeiLangParser.An_{}Context):
        self.collection_set.extras.append(
            {}PageExtra(self.page)
        )

"""

cname = ''.join([x.capitalize() for x in name.split('_')])
gr_name = 'PageExtra' + cname

with open(bp + '/' + gr_name + '.g4', 'w+') as f:
    f.write(tpl.format(gr_name, name, name.upper()))

with open('/Users/aleksandrrudakov/dev/zmei/generator/grammar/PageExtra.g4', 'r') as f:
    lines = []
    for line in f.readlines():
        if 'PageExtraHtml' in line:
            lines.append('    ' + gr_name + ',\n')

        lines.append(line)

        if 'an_react' in line:
            lines.append('    |an_' + name + '\n')

with open('/Users/aleksandrrudakov/dev/zmei/generator/grammar/PageExtra.g4', 'w') as f:
    f.write(''.join(lines))

with open('/Users/aleksandrrudakov/dev/zmei/generator/grammar/ZmeiLangSimpleLexer.g4', 'r') as f:
    lines = []
    for line in f.readlines():
        lines.append(line)

        if '// Annotation types' in line:
            lines.append("AN_{}: '@{}';\n".format(name.upper(), name))

with open('/Users/aleksandrrudakov/dev/zmei/generator/grammar/ZmeiLangSimpleLexer.g4', 'w+') as f:
    f.write(''.join(lines))

with open('/Users/aleksandrrudakov/dev/zmei/generator/zmei_generator/parser/populate_page_extras.py', 'r') as f:
    lines = []
    for line in f.readlines():
        lines.append(line)

        if 'import BaseListener' in line:
            lines.append("from zmei_generator.extras.page.{} import {}PageExtraParserListener\n".format(name, cname))

        if 'class PageExtraListener(' in line:
            lines.append("    {}PageExtraParserListener,\n".format(cname))

with open('/Users/aleksandrrudakov/dev/zmei/generator/zmei_generator/parser/populate_page_extras.py', 'w+') as f:
    f.write(''.join(lines))

with open(f'/Users/aleksandrrudakov/dev/zmei/generator/zmei_generator/extras/page/{name}.py', 'w+') as f:
    f.write(tpl_py.format(cname, name, cname, name, name, cname))
