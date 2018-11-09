import ast
import re
from abc import abstractmethod

import os
from bs4 import BeautifulSoup, NavigableString
from pyparsing import *
from jinja2 import Environment, FileSystemLoader, TemplateNotFound
from termcolor import colored


class Value(object):
    def __init__(self, val):
        self.val = val

    def parsed(self):
        return self.expr

    @abstractmethod
    def expr(self):
        pass

    @abstractmethod
    def __str__(self):
        pass


class ExpressionValue(Value):
    def parsed(self):
        return ast.literal_eval(self.val)

    def expr(self):
        return self.val

    def __str__(self) -> str:
        return '{{ ' + self.expr() + ' }}'


class StringValue(Value):
    def expr(self):
        return '"{}"'.format(self.val.replace('"', "'"))

    def __str__(self) -> str:
        return self.val


class TranslatableStringValue(StringValue):
    def expr(self):
        return super().expr() + '|_'

    def __str__(self) -> str:
        return '{{ ' + self.expr() + ' }}'


loaded_themes = {}


def render_template(theme_folder, template_name, context):
    context = context or {}

    if theme_folder not in loaded_themes:
        loader = FileSystemLoader(theme_folder)

        env = Environment(loader=loader,
                          variable_start_string='<{',
                          variable_end_string='}>',
                          block_start_string='<%',
                          block_end_string='%>'
                          )

        def expr(val):
            return val.expr()

        env.filters['expr'] = expr

        loaded_themes[theme_folder] = env
    else:
        env = loaded_themes[theme_folder]

    template = env.get_template(template_name)

    return template.render(**context)


def render_tag(el, theme_name='default', replace=True):
    self_content = ""
    for child in el.children:
        if isinstance(child, NavigableString):
            self_content += "\n" + str(child)  # str(parse_val(str(child).strip()))
        else:
            print(type(child), child)
            self_content += "\n" + render_tag(child, replace=False)

    context = {'_': self_content}
    for key, val in el.attrs.items():
        context[key] = parse_val(val)

    m = re.match('^block:([a-z0-9_]+)$', el.name)
    if m:
        tag_template = '{{% block {} %}}{}{{% endblock %}}'.format(m.group(1), self_content)
    else:
        theme_folder = 'col/themes/{}'.format(theme_name)
        template_name = '{}.html'.format(el.name.replace('.', '/'))
        try:
            tag_template = render_template(theme_folder, template_name, context=context)
        except TemplateNotFound:
            print(colored(
                'Warning!', on_color='on_red'),
                'Can not load template: ',
                colored(template_name, on_color='on_blue'),
                'Theme folder:', theme_folder
            )
            tag_template = self_content

        if replace:
            el.replaceWith(tag_template)

    return tag_template


def parse_val(val):
    if len(val) and val[0] == '!':
        new_val = ast.literal_eval(val[1:])
    elif len(val) and val[0] == '$':
        new_val = TranslatableStringValue(val[1:])
    elif len(val) and val[0] == '@':
        new_val = ExpressionValue(val[1:])
    else:
        new_val = StringValue(val)
    return new_val


def unescape_html(html):
    html = html.replace('&lt;', '<')
    html = html.replace('&gt;', '>')
    html = html.replace('&amp;', '&')
    return html


def render_blocks(file_source):
    parts = file_source.split('<genius:blocks')
    if len(parts) > 0:
        content = []
        for idx, part in enumerate(parts):
            if idx == 0:
                content.append(part)
            else:
                sub = part.split('</genius:blocks>')
                if len(sub) != 2:
                    print('WARN: Error parsing template file: not closed <genius:blocks> tag?')
                    continue

                block_html = '<genius:blocks' + sub[0] + '</genius:blocks>'
                block = BeautifulSoup(block_html, "html.parser")
                theme = block.attrs.get('theme', 'default')

                for block_tag in block.children:
                    for subtag in block_tag.children:
                        if isinstance(subtag, str):
                            continue
                        render_tag(subtag, theme_name=theme)

                first_block = list(block.children)[0]
                first_block.unwrap()

                source = unescape_html(str(block))

                content.append(source)
                content.append(sub[1])

        file_source = ''.join(content)

    return file_source
