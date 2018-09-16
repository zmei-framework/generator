import re

from cPyparsing import *

identifier = Word(alphas + '_', alphanums + '_')

uri_segment = OneOrMore(Word(alphanums + '-._') | (Literal('<') + SkipTo(Literal('>')) + Literal('>')))
uri_expr = Combine(Optional('$') + Literal('/') + Optional(delimitedList(uri_segment, delim='/', combine=True)) + Optional('/'))
file_name = Word(alphanums + '-/_.')


# extras

extra = (LineStart() +
         Combine(Suppress('@') + Word(alphanums + '_')).setResultsName("extra_name") +
         Optional(
             Suppress('.') + Word(alphanums + '_').setResultsName("descriptor")
         ) +
         Optional(
             QuotedString('<@', endQuoteChar='@>', multiline=True) |
             QuotedString('<<', endQuoteChar='>>', multiline=True) |
             QuotedString('{{', endQuoteChar='}}', multiline=True) |
             QuotedString('{', endQuoteChar='}', multiline=True) |
             QuotedString('(', endQuoteChar=')', multiline=True)
         ).setResultsName('extra_body'))

extras = ZeroOrMore(Group(extra)).setResultsName('extras')


# Collection header

field_name_spec = Literal('*') | Literal('.*') | (Combine(Optional('^') + Optional('.') + Optional('*') + identifier + Optional('*')))

def modifier(symbol, name):
    return Optional(Literal(symbol)).setParseAction(lambda tokens: len(tokens) > 0).setResultsName(name)


choice = Group((Word(alphanums + '_')|QuotedString('"')).setResultsName('value') + Optional(Suppress('/') + (
    QuotedString('"')|Regex(r"\w[\w _\.\-]+\w", re.UNICODE)).setResultsName('label')))

glob_expr = Literal('<glob:') + QuotedString('"').setResultsName('glob_expr') + Literal('>')

choices = Group(delimitedList(choice)).setResultsName('choices')

choices_or_glob = glob_expr | choices


collection_name = Regex(r"\w[\w _\.\-]+\w", re.UNICODE) \
    .setParseAction(lambda tokens: " ".join(tokens)) \
    .setResultsName("name")

collection_name_plural = Suppress('/') + Regex(r"\w[\w _\.\-]+\w", re.UNICODE) \
    .setResultsName("name_plural")

ref = Combine(Suppress('#') + Optional(Word(alphanums + '_').setResultsName("parent") + (Literal('->') | Literal('~>')).setResultsName('parent_separator')) + Word(alphanums + '_').setResultsName("ref"))
class_name = Word(alphanums + '_.').setResultsName('class_name')

ref_or_class_name = ref | class_name


collection_header = (
    LineStart() + Optional(White()) + ref + Optional(Suppress(':')) + Optional(collection_name) + Optional(collection_name_plural) +
    LineStart() + Optional(White()) + Suppress(Word('-'))
).setResultsName('header')

field_verbose_name = Suppress('/') + Regex(r"[^\?\r\n]+", re.UNICODE) \
    .setParseAction(lambda tokens: " ".join(tokens).strip()) \
    .setResultsName("verbose_name")

type_declaration = identifier.setResultsName('type_name') + Optional(
    QuotedString('(', endQuoteChar=')')).setResultsName('type_opts')

calculated_expression = QuotedString('<<', endQuoteChar=';').setResultsName('calculated_expression')
calculated_static_expression = QuotedString('<@', endQuoteChar=';').setResultsName('calculated_static_expression')

field_declaration = Suppress(':') + (calculated_expression | calculated_static_expression | type_declaration)

field_help = Suppress('?') + Regex(r"[^\r\n]+", re.UNICODE).setParseAction(lambda tokens: " ".join(tokens).strip()).setResultsName('field_help')

collection_field = Group(
    LineStart() +
    # Each -> in any order
    Each([
        modifier('$', 'translatable'),
        modifier('=', 'display_field'),
        modifier('&', 'unique'),
        modifier('!', 'index'),
        modifier('*', 'required'),
        modifier('~', 'not_null'),
    ]) +
    identifier.setResultsName('name') +
    Optional(field_declaration) +
    Optional(field_verbose_name) +
    Optional(field_help)
)


to_string_declaration = Suppress('=') + QuotedString('"').setResultsName('to_string')

options = Optional(to_string_declaration)

fields = ZeroOrMore(collection_field).setResultsName('fields')

collection = LineStart() + Group(collection_header + options + fields + extras)

page_imports = SkipTo(Literal('%%')).setResultsName('page_imports') + Literal('%%')
collection_imports = Literal('%%') + SkipTo(Literal('%%')).setResultsName('collection_imports') + Literal('%%')


collections = OneOrMore(collection).setResultsName('collections')




# Page header
file_name_expr = Literal('expr') + (QuotedString("(", endQuoteChar=")") | QuotedString("<", endQuoteChar=">")).setResultsName('template_expr')
file_name_or_expr = file_name_expr | file_name.setResultsName('template_name')

page_header = Suppress('[') + Optional(identifier.setResultsName('parent_name') + Suppress('->')) + \
              identifier.setResultsName('page_name') + \
              Optional(Suppress('as') + identifier.setResultsName('url_alias')) + \
              Optional(Suppress(':') + uri_expr.setResultsName('uri') +
                                                                Optional(Suppress(':') + file_name_or_expr)) + Suppress(']')
page_item = Group(identifier.setResultsName('key') + Suppress(':') + restOfLine.setResultsName('expression'))

page_code = Optional(QuotedString('{', endQuoteChar='}', multiline=True).setResultsName('page_code'))

function = Group(identifier.setResultsName('name') + Suppress('(') +
                 Optional(delimitedList(identifier)).setResultsName('args') + Suppress(')') + \
    QuotedString('{', endQuoteChar='}', multiline=True).setResultsName('body'))

functions = ZeroOrMore(function).setResultsName('functions')


html = Optional(LineStart() + Literal('<') + Group(Optional(identifier + Literal(':')) + identifier) + SkipTo(page_header | collection_header | Literal('%%') | stringEnd)).setResultsName('html')

page = Group(page_header + Each([ZeroOrMore(page_item).setResultsName('page_items'), extras]) + functions + page_code + html)

collection_set_extras = ZeroOrMore(Group(extra)).setResultsName('col_extras')

pages = OneOrMore(page).setResultsName('pages')

col_import = Group(LineStart() + Literal('%include') + QuotedString('"').setResultsName('path'))
imports = OneOrMore(col_import).setResultsName('col_imports')

collection_set = (Optional(imports) + Optional(page_imports) + Optional(collection_set_extras) + Optional(pages) + Optional(collection_imports) + Optional(collections) + stringEnd).ignore(cStyleComment)

