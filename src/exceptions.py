class Error(Exception):
    """Base class for other exceptions"""
    pass

class InvalidInputCharacterError(Error):
    """Raised when an input character of a string is invalid"""
    pass


class InputValueNegativeError(Error):
    """Raised when the input value is negative when not allowed"""
    pass

class InputValueNotStringError(Error):
    """Raised when the input value is negative when not allowed"""
    pass