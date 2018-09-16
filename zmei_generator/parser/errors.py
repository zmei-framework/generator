

class ValidationError(object):

    def __init__(self, token, message) -> None:
        super().__init__()

        self.token = token
        self.message = message

    def format_error(self):
        return f'[{self.token.line}:{self.token.column}] {self.message}'


class PageParentValidationError(ValidationError):

    def __init__(self, token, parent_page_name) -> None:
        self.parent_page_name = parent_page_name
        super().__init__(token, f"Parent page is not defined: \"{parent_page_name}\"")

