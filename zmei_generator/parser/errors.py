
class ValidationError(Exception):

    def __init__(self, lineno, col, message) -> None:
        super().__init__()

        self.message = message

        self.lineno = lineno
        self.col = col

    def format_error(self):
        return f'[{self.lineno}:{self.col}] {self.message}'

    def __str__(self) -> str:
        return self.format_error()


class GlobalScopeValidationError(ValidationError):
    def __init__(self, message) -> None:
        super().__init__(0, 0, message)


class ValidationTokenError(ValidationError):

    def __init__(self, token, message, pos_diff=0) -> None:
        self.token = token

        super().__init__(self.token.line, self.token.column + pos_diff, message)


class PageParentValidationError(ValidationTokenError):

    def __init__(self, token, parent_page_name) -> None:
        self.parent_page_name = parent_page_name
        super().__init__(token, f"Parent page is not defined: \"{parent_page_name}\"")

class TabsSuitRequiredValidationError(ValidationTokenError):
    def __init__(self, token) -> None:
        super().__init__(token, f"@admin->tabs requires @suit feature enabled. Add \"@suit\""
                                f"to the beginning of the col file.")


class LangsRequiredValidationError(ValidationTokenError):
    def __init__(self, token) -> None:
        super().__init__(token, f"$ (localized fields) require @langs annotation with a list of languages added")