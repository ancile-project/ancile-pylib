"""
    utilities used by the parser
"""
import re

SPACE_REGEX = r"(\n *)def "


def fix_gap(function_string):
    """
    removes unnecessary whitespace gap if the function is nested

    :param function_string: String of function definition
    :return triuncated function
    """
    matches = re.findall(SPACE_REGEX, function_string)
    fixed_gap = function_string.replace(matches[0], '\n') if matches else function_string
    return fixed_gap.strip()


def regex_repl_function(true_args):
    """
    generates a replacement function for re.sub method

    :param true_args: Dictionary-like object of arg inputs.
    :return replacement function
    """
    
    def repl_function(match_object):
        before, arg, after = match_object.groups()
        real_arg = true_args[arg]
        true_arg = "'" + real_arg + "'" if isinstance(real_arg, str) else str(real_arg)
        return before + true_arg + after

    return repl_function
