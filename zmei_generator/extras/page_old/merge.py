from zmei_generator.config.domain.page_extra import PageExtra


class MergePageExtra(PageExtra):

    @classmethod
    def get_name(cls):
        return 'merge'

    def __init__(self, parsed_result, page):
        super().__init__(parsed_result, page)

        page.allow_merge = True


