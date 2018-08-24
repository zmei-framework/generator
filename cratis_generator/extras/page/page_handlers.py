from cratis_generator.config.domain.page_extra import PageExtra
from cratis_generator.config.domain.exceptions import ValidationException


class HandleErrorExtra(PageExtra):
    @classmethod
    def get_name(cls):
        return 'error'

    def __init__(self, parsed_result, page):
        super().__init__(parsed_result, page)

        try:
            code = int(parsed_result.extra_body.strip())
        except ValueError:
            raise ValidationException('Extra "error" for page {} accpets only numeric error codes'.format(page))

        page.handlers.append(code)
