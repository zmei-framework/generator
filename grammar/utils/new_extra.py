import sys

bp = '/Users/aleksandrrudakov/dev/generator/grammar'
lexer = '/Users/aleksandrrudakov/dev/generator/grammar/ZmeiLangSimpleLexer.g4'

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
from zmei_generator.config.domain.collection_set_extra import CollectionSetExtra
from zmei_generator.parser.gen.ZmeiLangParser import ZmeiLangParser
from zmei_generator.parser.utils import BaseListener

class {}CsExtra(CollectionSetExtra):
    def get_name(cls):
        return '{}'
    

class {}CsExtraParserListener(BaseListener):

    def enterAn_{}(self, ctx: ZmeiLangParser.An_{}Context):
        self.collection_set.extras.append(
            {}CsExtra(self.collection_set)
        )

"""

cname = ''.join([x.capitalize() for x in name.split('_')])
gr_name = 'CsExtra' + cname

with open(bp + '/' + gr_name + '.g4', 'w+') as f:
    f.write(tpl.format(gr_name, name, name.upper()))

with open('/Users/aleksandrrudakov/dev/generator/grammar/CsExtra.g4', 'r') as f:
    lines = []
    for line in f.readlines():
        if 'CsExtraSuit' in line:
            lines.append('    ' + gr_name + ',\n')

        lines.append(line)

        if 'an_suit' in line:
            lines.append('    |an_' + name + '\n')

with open('/Users/aleksandrrudakov/dev/generator/grammar/CsExtra.g4', 'w') as f:
    f.write(''.join(lines))

with open('/Users/aleksandrrudakov/dev/generator/grammar/ZmeiLangSimpleLexer.g4', 'r') as f:
    lines = []
    for line in f.readlines():
        lines.append(line)

        if '// Annotation types' in line:
            lines.append("AN_{}: '@{}';\n".format(name.upper(), name))

with open('/Users/aleksandrrudakov/dev/generator/grammar/ZmeiLangSimpleLexer.g4', 'w+') as f:
    f.write(''.join(lines))

with open('/Users/aleksandrrudakov/dev/generator/zmei_generator/parser/populate.py', 'r') as f:
    lines = []
    for line in f.readlines():
        lines.append(line)

        if 'import ZmeiLangParserListener' in line:
            lines.append("from zmei_generator.extras.collection_set.{} import {}CsExtraParserListener\n".format(name, cname))

        if 'PartsCollectorListener(' in line:
            lines.append("    {}CsExtraParserListener,\n".format(cname))

with open('/Users/aleksandrrudakov/dev/generator/zmei_generator/parser/populate.py', 'w+') as f:
    f.write(''.join(lines))

with open(f'/Users/aleksandrrudakov/dev/generator/zmei_generator/extras/collection_set/{name}.py', 'w+') as f:
    f.write(tpl_py.format(cname, name, cname, name, name, cname))
