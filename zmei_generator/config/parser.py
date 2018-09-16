import os
from cPyparsing import ParseException
from glob import glob

from zmei_generator.config.domain.exceptions import ValidationException
from zmei_generator.config.grammar import collection_set
from zmei_generator.extras.admin import AdminExtra
from zmei_generator.extras.api import ApiExtra
from zmei_generator.extras.clean import CleanExtra
from zmei_generator.extras.collection_set.react import ReactCollectionSetExtra
from zmei_generator.extras.dates import DateTreeExtra
from zmei_generator.extras.db_signals import PreSaveExtra, PostSaveExtra, PreDeleteExtra, \
    PostDeleteExtra, M2mChangedExtra
from zmei_generator.extras.mixin import MixinExtra
from zmei_generator.extras.page.auth import AuthExtra
from zmei_generator.extras.page.block import BlocksPageExtra
from zmei_generator.extras.page.crud import CrudPageExtra, CrudCreatePageExtra, CrudUpdatePageExtra, \
    CrudDeletePageExtra, CrudDetailPageExtra
from zmei_generator.extras.page.form import FormExtra
from zmei_generator.extras.page.menu import MenuPageExtra
from zmei_generator.extras.page.merge import MergePageExtra
from zmei_generator.extras.page.page_handlers import HandleErrorExtra
from zmei_generator.extras.page.post import PostPageExtra
from zmei_generator.extras.page.rss import RssPageExtra
from zmei_generator.extras.rest import RestExtra
from zmei_generator.extras.sortable import SortableExtra, OrderExtra
from zmei_generator.extras.tree import TreeExtra
from zmei_generator.generator.utils import handle_parse_exception
from zmei_generator.parser.parser import parse_string
from zmei_generator.parser.populate import populate_collection_set


class ParseError(Exception):
    pass

class Parser(object):

    def get_field_class(self, type_name):
        from zmei_generator.config.fields import field_type_map

        if type_name == '':
            type_name = 'text'

        try:
            return field_type_map[type_name]
        except KeyError:
            raise NotImplementedError('Unknown field type: ' + type_name)

    def parse_file(self, filename, app_name):
        from zmei_generator.config.domain.collection_set_def import CollectionSetDef

        return self.parse_collection_set(filename, app_name)
        # TODO: imports.
        # parse_result['page_imports'] = '\n'.join(parse_result['page_imports'])
        # parse_result['collection_imports'] = '\n'.join(parse_result['collection_imports'])

        # return CollectionSetDef(
        #     type('parse_result', (object,), parse_result), self, app_name=app_name
        # )

    def parse_collection_set(self, filename, app_name):
        with open(filename, 'r', encoding='utf8') as f:
            config = f.read()

        config = config.replace(chr(8232), '')  # some wired windows-only utf new line?

        # relative_path = os.path.dirname(filename)

        try:
            tree = parse_string(config)

            return populate_collection_set(tree, app_name)

            # parse_result = collection_set.parseString(config)

            # all_attrs = ['page_imports', 'collection_imports', 'col_extras', 'col_imports', 'collections', 'pages']
            # parse_result_dict = {}
            # for attr in all_attrs:
            #     val = getattr(parse_result, attr)
            #     if not val:
            #         val = []
            #     else:
            #         if isinstance(val, str):
            #             val = [val]
            #         else:
            #             val = list(val)
            #
            #     parse_result_dict[attr] = val
            #
            # if not result:
            #     result = parse_result_dict
            # else:
            #     for attr in all_attrs:
            #         result[attr] += parse_result_dict[attr]
            #
            # if parse_result.col_imports:
            #     for import_expr in parse_result.col_imports:
            #         glob_path = os.path.join(relative_path, import_expr.path)
            #
            #         count = 0
            #         for file_path in sorted(glob(glob_path)):
            #             count += 1
            #             self.parse_collection_set(file_path, result)
            #
            #         if not count:
            #             raise ValidationException('Error parsing {}: Expression "{}" did not returned any files '
            #                                       '(relatively to path: {}/)'.format(
            #                 filename, import_expr.path, relative_path
            #             ))

            return result

        except ParseException as e:
            handle_parse_exception(e, config, 'Error parsing {}'.format(filename))

    def get_extras_available(self):
        return {x.get_name(): x for x in (
            AdminExtra,
            RestExtra,
            ApiExtra,
            TreeExtra,
            SortableExtra,
            OrderExtra,
            DateTreeExtra,
            MixinExtra,
            CleanExtra,

            PreSaveExtra,
            PostSaveExtra,
            PreDeleteExtra,
            PostDeleteExtra,
            M2mChangedExtra,
        )}

    def get_page_extras_available(self):
        return {x.get_name(): x for x in (
            FormExtra,
            AuthExtra,
            CrudPageExtra,
            CrudCreatePageExtra,
            CrudUpdatePageExtra,
            CrudDeletePageExtra,
            CrudDetailPageExtra,
            BlocksPageExtra,
            MenuPageExtra,
            PostPageExtra,
            MergePageExtra,
            RssPageExtra,
            HandleErrorExtra,
        )}

    def get_collection_extras_available(self):
        return {x.get_name(): x for x in (
            ReactCollectionSetExtra,
        )}

