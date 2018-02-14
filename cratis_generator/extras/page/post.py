from cratis_generator.config.domain import PageExtra


class PostPageExtra(PageExtra):

    @classmethod
    def get_name(cls):
        return 'post'

    def __init__(self, parsed_result, page):
        super().__init__(parsed_result, page)

        page.allow_post = True



