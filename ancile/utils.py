"""
    utilities used by the parser
"""
from ancile.errors import ArgumentNumberMismatch

def fix_gap(function_tuple):
    """
    removes unnecessary whitespace gap if the function is nested

    :param function_string: String of function definition
    :return triuncated function
    """
    gap_size = len(function_tuple[0]) - len(function_tuple[0].lstrip())
    return ''.join(line[gap_size:] for line in function_tuple)

def regex_repl_function(true_args):
    """
    generates a replacement function for re.sub method

    :param true_args: Dictionary-like object of arg inputs.
    :return replacement function
    """

    def repl_function(match_object):
        before, arg, after = match_object.groups()
        real_arg = true_args[arg]
        if isinstance(real_arg, str) and arg[0] != "_":
            true_arg = "'" + real_arg + "'"
        else:
            true_arg = str(real_arg)
        return before + true_arg + after

    return repl_function

def build_programs(program, args=None, kwargs=None):
    """
        Build the same program for multiple users
        with different arguments

        Both args and kwargs must have the same length, or exactly one
        of them has to be null

        :param program: Ancile program function
        :param args: List or tuple containing lists or tuples of arguments
        :param kwargs: List or tuple containing dictionaries of arguments
        :return ancile program string
    """
    if not args and not kwargs:
        raise ArgumentNumberMismatch("No arguments provided")

    args = args or iter(list, None)
    kwargs = kwargs or iter(dict, None)

    return "\n".join(program(*arg, **kwarg) for arg, kwarg in zip(args, kwargs))
