"""
    Utilities used internally by the parsers.
"""
from urllib.parse import urljoin


def fix_gap(function_tuple):
    """
    removes unnecessary whitespace gap if the function is nested

    :param function_string: String of function definition
    :returns: triuncated function
    """
    gap_size = len(function_tuple[0]) - len(function_tuple[0].lstrip())
    return "".join(line[gap_size:] for line in function_tuple)


def regex_repl_function(true_args):
    """
    generates a replacement function for re.sub method

    :param true_args: Dictionary-like object of arg inputs.
    :returns: replacement function
    """

    def repl_function(match_object):
        before, arg, after = match_object.groups()
        real_arg = true_args[arg]
        if isinstance(real_arg, str) and arg[0] != "_":
            true_arg = "'" + real_arg + "'"
        elif isinstance(real_arg, list) and arg[0] == "_":
            true_arg = "[" + ", ".join(map(str, real_arg)) + "]"
        elif isinstance(real_arg, tuple) and arg[0] == "_":
            true_arg = "(" + ", ".join(map(str, real_arg)) + ")"
        else:
            true_arg = str(real_arg)
        return before + true_arg + after

    return repl_function


def generate_url(ancile_url):
    """
        Generate an API endpoint url from URL base

        :param ancile_url: root URL of ancile instance
        :returns: API endpoint URL
    """
    return urljoin(ancile_url, "api/run")
