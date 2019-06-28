"""
    utilities used by the parser
"""

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
        true_arg = "'" + real_arg + "'" if isinstance(real_arg, str) else str(real_arg)
        return before + true_arg + after

    return repl_function
