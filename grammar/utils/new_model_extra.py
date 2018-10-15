import sys

bp = '/Users/aleksandrrudakov/dev/generator/grammar'
lexer = '/Users/aleksandrrudakov/dev/generator/grammar/ZmeiLangSimpleLexer.g4'

etype = sys.argv[1]
name = sys.argv[2]


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
from zmei_generator.config.extras import ModelExtra
from zmei_generator.parser.gen.ZmeiLangParser import ZmeiLangParser
from zmei_generator.parser.utils import BaseListener

class {}ModelExtra(ModelExtra):
    # {}
    pass
    
class {}ModelExtraParserListener(BaseListener):

    def enterAn_{}(self, ctx: ZmeiLangParser.An_{}Context):
        self.collection_set.extras.append(
            {}ModelExtra(self.model)
        )

"""

if etype == 'model':
    cname = ''.join([x.capitalize() for x in name.split('_')])
    gr_name = 'ModelExtra' + cname

    with open(bp + '/' + gr_name + '.g4', 'w+') as f:
        f.write(tpl.format(gr_name, name, name.upper()))

    with open('/Users/aleksandrrudakov/dev/generator/grammar/ModelExtra.g4', 'r') as f:
        lines = []
        for line in f.readlines():
            if 'ModelExtraAdmin' in line:
                lines.append('    ' + gr_name + ',\n')

            lines.append(line)

            if 'an_admin' in line:
                lines.append('    |an_' + name + '\n')

    with open('/Users/aleksandrrudakov/dev/generator/grammar/ModelExtra.g4', 'w') as f:
        f.write(''.join(lines))

    with open('/Users/aleksandrrudakov/dev/generator/grammar/ZmeiLangSimpleLexer.g4', 'r') as f:
        lines = []
        for line in f.readlines():
            lines.append(line)

            if '// Annotation types' in line:
                lines.append("AN_{}: '@{}';\n".format(name.upper(), name))

    with open('/Users/aleksandrrudakov/dev/generator/grammar/ZmeiLangSimpleLexer.g4', 'w+') as f:
        f.write(''.join(lines))

    with open('/Users/aleksandrrudakov/dev/generator/zmei_generator/parser/populate_model_extras.py', 'r') as f:
        lines = []
        for line in f.readlines():
            lines.append(line)

            if 'import BaseListener' in line:
                lines.append("from zmei_generator.extras.model.{} import {}ModelExtraParserListener\n".format(name, cname))

            if 'class ModelExtraListener(' in line:
                lines.append("    {}ModelExtraParserListener,\n".format(cname))

    with open('/Users/aleksandrrudakov/dev/generator/zmei_generator/parser/populate_model_extras.py', 'w+') as f:
        f.write(''.join(lines))

    with open(f'/Users/aleksandrrudakov/dev/generator/zmei_generator/extras/model/{name}.py', 'w+') as f:
        f.write(tpl_py.format(cname, name, cname, name, name, cname))
