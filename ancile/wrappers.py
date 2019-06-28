"""
    Wrappers used for ancile functions
"""

from inspect import getsourcelines
import re
from ancile.errors import ArgumentNumberMismatch
from ancile.utils import fix_gap, regex_repl_function

def ancile_program(func):
    """
    Generates ancile program

    :param func: Function to be ancile-fied

    e.g.:

    >> @ancile_program
    .. def test_function():
           print("Test")

    >> test_function()
    "print(\"Test\")\n"
    """

    code_list = getsourcelines(func)[0]
    args_line = code_list[1]
    code = fix_gap(code_list[2:])

    first_paren = args_line.index("(") + 1
    second_paren = args_line.index(")")
    split_args = args_line[first_paren:second_paren].split(",")

    exp_args, exp_kwargs, exp_kwargs_index = [], {}, {}

    for index, arg in enumerate(split_args):
        arg = arg.strip()
        if not arg.startswith("*"):
            if "=" in arg:
                key, value = arg.split("=")
                exp_kwargs[key] = value.strip("'\"")
                exp_kwargs_index[index] = key
            elif arg:
                exp_args.append(arg)

    # potentially add support for *args and **kwargs

    # if len(parsed_args) > 0:
    #     mul_kwargs = parsed_args[-1].startswith("**")
    #     mul_kwargs_kw = parsed_args[-1] if mul_kwargs else None
    #     mul_args = (parsed_args[-1].startswith("*") ^ mul_kwargs) or (len(parsed_args) > 1 \
    #         and parsed_args[-2].startswith("*"))
    #     mul_args_kw = parsed_args[:-(1+mul_kwargs)] if mul_args else None
    # else:
    #     mul_kwargs = mul_args = False

    if not exp_args and not exp_kwargs:
        return lambda: code

    def final_function(*args, **kwargs):

        if len(args) + len(kwargs) < len(exp_args):
            raise ArgumentNumberMismatch(
                "{1} arguments, expecting {0} or more.".format(
                    len(exp_args),
                    len(args)+len(kwargs)))

        true_args = {arg_name: arg for arg_name, arg in zip(exp_args, args)}

        if len(args) < len(exp_args):

            for arg in exp_args[len(args):]:
                if arg not in kwargs:
                    raise ArgumentNumberMismatch(
                        "Mandatory parameter {} does not have an argument.".format(arg))

                true_args[arg] = kwargs.pop(arg)

        elif len(args) > len(exp_args):

            for index in range(len(true_args), len(args)):
                if index not in exp_kwargs_index:
                    raise ArgumentNumberMismatch(
                        "Expected maximum of {} arguments, received {}.".format(
                            len(exp_args) + len(exp_kwargs), len(args) + len(kwargs)))

                true_args[exp_kwargs_index[index]] = args[index]

        for keyword_arg in exp_kwargs:
            if keyword_arg not in true_args:
                if keyword_arg not in kwargs:
                    true_args[keyword_arg] = exp_kwargs[keyword_arg]
                else:
                    true_args[keyword_arg] = kwargs.pop(keyword_arg)

        ## use string substitution to generate an ancile program
        ## using the function parameters

        var_regex = r"([^\w]|^)(" + "|".join(true_args) + r")([^\w])"
        repl_function = regex_repl_function(true_args)

        final_code = re.sub(var_regex, repl_function, code)
        return final_code

    return final_function
