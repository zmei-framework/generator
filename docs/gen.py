import pprint

import os
import re

section = None
page = None
pages = {}

with open('topics.txt') as f:
    lines = f.readlines()


    for line in lines:
        m = re.match('^(\s*)(.*)', line)
        if not m or m.group(2).strip() == '':
            continue

        level = len(m.group(1)) // 4
        text = m.group(2).strip()
        slug = re.sub('\s+', '_', text)

        if level == 0:
            section = slug
            if not section in pages:
                pages[section] = {}
        elif level == 1:
            page = slug

            if not page in pages[section]:
                pages[section][page] = {
                    'name': text.capitalize(),
                    'topics': [
                        (0, text.strip().capitalize())
                    ]
                }
        else:

            if slug not in pages[section][page]['topics']:
                pages[section][page]['topics'].append(
                    (level - 1, text)
                )


levels = [
    '#',
    '=',
    '-',
    '^',
    '"',
    '*',
]

for folder, folder_pages in pages.items():
    if not os.path.exists(folder):
        os.makedirs(folder)

    i = 0
    for page_ref, page in folder_pages.items():
        i += 1
        page_text = ''

        for level, text in page['topics']:
            page_text += text.capitalize() + "\n"
            page_text += levels[level] * (len(text) + 5) + "\n\n"

        with open('{}/{}_{}.rst'.format(folder, i, page_ref), 'w+') as f:
            f.write(page_text)

pp = pprint.PrettyPrinter(indent=4)
pp.pprint(pages)
