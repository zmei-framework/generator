from zmei_generator.generator.utils import handle_parse_exception
from zmei_generator.parser.errors import ValidationError
from zmei_generator.parser.parser import parse_string
from zmei_generator.parser.populate import populate_collection_set


class ParseError(Exception):
    pass


class Parser(object):

    def parse_file(self, filename, app_name):

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

        except ValidationError as e:
            handle_parse_exception(e, config, 'Error parsing {}'.format(filename))

