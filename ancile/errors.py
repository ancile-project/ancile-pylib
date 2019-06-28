"""
    Exceptions to make catching ancile
    server-side errors easier.
"""

class PolicyException(Exception):
    """
        When the program does not match the
        user's policy.
    """

class AncileException(Exception):
    """
        Non-policy related server-side ancile exception.
    """

class ArgumentNumberMismatch(Exception):
    """
        If the arguments given do not match the number
        of arguments specified for an ancile function.
    """
