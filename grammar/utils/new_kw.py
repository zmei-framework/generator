import sys

name = sys.argv[1]

with open('/Users/aleksandrrudakov/dev/generator/grammar/ZmeiLangSimpleLexer.g4', 'r') as f:
    lines = []
    for line in f.readlines():
        lines.append(line)

        if 'KW_THEME' in line:
            lines.append("KW_{}: '{}';\n".format(name.upper(), name))

with open('/Users/aleksandrrudakov/dev/generator/grammar/ZmeiLangSimpleLexer.g4', 'w+') as f:
    f.write(''.join(lines))


with open('/Users/aleksandrrudakov/dev/generator/grammar/Base.g4', 'r') as f:
    lines = []
    for line in f.readlines():
        lines.append(line)

        if 'KW_THEME' in line:
            lines.append("   |KW_{}\n".format(name.upper()))

with open('/Users/aleksandrrudakov/dev/generator/grammar/Base.g4', 'w+') as f:
    f.write(''.join(lines))
