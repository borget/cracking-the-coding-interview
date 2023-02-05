class BooleanError(Exception):
    """
    Raised when boolean columns have incorrect values. [1, 0] are only allowed.
    """
    pass


class IntegerError(Exception):
    """
    Raised when integer value is incorrect.
    """

    pass


class WidthError(Exception):
    """
    Raised if width value is less or equals to Zero.
    """
    pass


class InvalidColumnName(Exception):
    """
    Raised when column name is not valid.
    """
    pass
