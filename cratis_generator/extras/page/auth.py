from cratis_generator.config.domain import PageExtra

from pyparsing import *

from cratis_generator.config.grammar import class_name, identifier

class AuthExtra(PageExtra):

    @classmethod
    def get_name(cls):
        return 'auth'

    def __init__(self, parsed_result, page):
        super().__init__(parsed_result, page)

        page.auth = True




