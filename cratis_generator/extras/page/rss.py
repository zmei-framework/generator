from cratis_generator.config.domain.page_extra import PageExtra
from cratis_generator.config.domain.exceptions import ValidationException

from cPyparsing import *

from cratis_generator.config.grammar import identifier
from cratis_generator.generator.utils import handle_parse_exception

class RssPageExtra(PageExtra):

    @classmethod
    def get_name(cls):
        return 'rss'

    def __init__(self, parsed_result, page):
        super().__init__(parsed_result, page)

        fields = Each([
            Suppress(field) + Suppress(':') + Group(
                identifier.setResultsName('field') + Suppress('->') + restOfLine.setResultsName('expression')
            ).setResultsName(field) for field in ['date', 'title', 'description', 'url']
        ])

        try:
            if page.parent:
                raise ValidationException('Rss page {} should not have parent'.format(page))

            fields = ['items', 'title', 'description']

            for field in fields:
                if field not in page.page_items:
                    raise ValidationException('Rss page {} must have field "{}"'.format(page, field))

            rss_data = fields.parseString(parsed_result.extra_body)

            page.rss = {
                field: rss_data[field] for field in fields
            }

        except ParseException as e:
            handle_parse_exception(e, parsed_result.extra_body, '@rss extra for page: {}'.format(page))



