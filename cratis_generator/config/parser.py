import re
from glob import glob

import os

from cratis_generator.config.domain import ValidationException
from cratis_generator.config.grammar import collection_set
from cratis_generator.extras.dates import DateTreeExtra
from cratis_generator.extras.document import DocumentExtra
from cratis_generator.extras.page.page_handlers import HandleErrorExtra
from cratis_generator.extras.page.post import PostPageExtra
from cratis_generator.extras.page.rss import RssPageExtra
from cratis_generator.extras.sortable import SortableExtra, OrderExtra
from cratis_generator.extras.tree import TreeExtra
from cratis_generator.extras.mixin import MixinExtra
from cratis_generator.generator.utils import handle_parse_exception
from pyparsing import ParseException

from cratis_generator.extras.admin import AdminExtra
from cratis_generator.extras.rest import RestExtra


class ParseError(Exception):
    pass

class Parser(object):

    def get_field_class(self, type_name):
        from cratis_generator.config.fields import field_type_map

        if type_name == '':
            type_name = 'text'

        try:
            return field_type_map[type_name]
        except KeyError:
            raise NotImplementedError('Unknown field type: ' + type_name)

    def parse_file(self, filename, app_name):
        from cratis_generator.config.domain import CollectionSetDef

        parse_result = self.parse_collection_set(filename)
        parse_result['page_imports'] = '\n'.join(parse_result['page_imports'])
        parse_result['collection_imports'] = '\n'.join(parse_result['collection_imports'])

        return CollectionSetDef(
            type('parse_result', (object,), parse_result), self, app_name=app_name
        )

    def parse_collection_set(self, filename, result=None):
        with open(filename, 'r', encoding='utf8') as f:
            config = f.read()
        relative_path = os.path.dirname(filename)

        try:
            parse_result = collection_set.parseString(config)

            all_attrs = ['page_imports', 'collection_imports', 'collections', 'pages']
            parse_result_dict = {}
            for attr in all_attrs:
                val = getattr(parse_result, attr)
                if not val:
                    val = []
                else:
                    if isinstance(val, str):
                        val = [val]
                    else:
                        val = list(val)

                parse_result_dict[attr] = val

            if not result:
                result = parse_result_dict
            else:
                for attr in all_attrs:
                    result[attr] += parse_result_dict[attr]

            if parse_result.col_imports:
                for import_expr in parse_result.col_imports:
                    glob_path = os.path.join(relative_path, import_expr.path)

                    count = 0
                    for file_path in glob(glob_path):
                        count += 1
                        self.parse_collection_set(file_path, result)

                    if not count:
                        raise ValidationException('Error parsing {}: Expression "{}" did not returned any files '
                                                  '(relatively to path: {}/)'.format(
                            filename, import_expr.path, relative_path
                        ))

            return result

        except ParseException as e:
            handle_parse_exception(e, config, 'Error parsing {}'.format(filename))

    def get_extras_available(self):
        return {x.get_name(): x for x in (
            AdminExtra,
            RestExtra,
            TreeExtra,
            SortableExtra,
            OrderExtra,
            DocumentExtra,
            DateTreeExtra,
            MixinExtra,
        )}

    def get_page_extras_available(self):
        return {x.get_name(): x for x in (
            PostPageExtra,
            RssPageExtra,
            HandleErrorExtra
        )}

