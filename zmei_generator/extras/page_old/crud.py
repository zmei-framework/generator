

field_filter = Optional(QuotedString('<', endQuoteChar='>')).setResultsName('filter_expr')
field = Group(field_name_spec.setResultsName('spec') + field_filter)

ref_parser = Combine(Literal('#') + Word(alphanums + '_')).setResultsName('model') + \
             Optional(QuotedString('<', endQuoteChar='>').setResultsName('query')) + \
             Optional(Suppress('fields:') + Group(delimitedList(field)).setResultsName('fields'))

class_parser = Word(alphanums + '_.').setResultsName('model') + \
               Optional(QuotedString('<', endQuoteChar='>').setResultsName('query'))

parser = ((ref_parser | class_parser) +
          Each([
              Optional(Suppress('fields:') + Group(delimitedList(
                  field_name_spec.setResultsName('spec') + field_filter)).setResultsName('fields')),
              Optional(Suppress('list_fields:') + Group(delimitedList(
                  field_name_spec.setResultsName('spec') + field_filter)).setResultsName('list_fields')),
              Optional(Suppress('skip:') + Group(delimitedList(
                  Literal('create') | Literal('edit') | Literal('delete') | Literal('detail') | Literal('list')
              )).setResultsName('skip')),
              Optional(Suppress('block:') + identifier.setResultsName('block_name')),
              Optional(Suppress('theme:') + identifier.setResultsName('theme')),
              Optional(Suppress('url_prefix:') + Word(alphanums + '-/').setResultsName('url_prefix')),
              Optional(Suppress('pk_param:') + Word(alphanums + '_').setResultsName('pk_param')),
              Optional(Suppress('object_expr:') + restOfLine.setResultsName('object_expr')),
              Optional(Suppress('edit_auth:') + restOfLine.setResultsName('edit_auth')),
              Optional(Suppress('item_name:') + Word(alphanums + '_').setResultsName('item_name')),
              Optional(Suppress('link_extra:') + QuotedString('"').setResultsName('link_extra')),
              Optional(Suppress('link_suffix:') + QuotedString('"').setResultsName('link_suffix'))
          ]) +
          Optional(Suppress('=>') + restOfLine.setResultsName('next_page'))
          ).ignore(cStyleComment)




