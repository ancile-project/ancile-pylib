from inspect import getsource
import re
from ancile.errors import ArgumentNumberMismatch

'''
    Generates ancile program

    :param func: Function to be ancile-fied

    e.g.:
    
    >> @ancile_function
    .. def test_function():
           print("Test")
    
    >> test_function()
    "print(\"Test\")\n"
'''
def ancile_function(func):
    code = getsource(func)
    code = code.replace("\n    ", "\n")
    parsed_args = [arg.strip() for arg in code[code.index("(") + 1:code.index(")")].split(",")]

    for _ in range(2):
        code = code[code.index("\n") + 1:]

    in_args, in_kwargs, in_kwargs_index = [], {}, {}
    if any(parsed_args):
        for index, parsed_arg in enumerate(parsed_args):
            if not parsed_arg.startswith("*"):
                if "=" in parsed_arg:
                    key, value = parsed_arg.split("=")
                    value = value.strip('\"\'')
                    in_kwargs[key] = value
                    in_kwargs_index[index] = key
                else:
                    in_args.append(parsed_arg)

        if len(parsed_args) > 0:
            mul_kwargs = parsed_args[-1].startswith("**")
            mul_kwargs_kw = parsed_args[-1] if mul_kwargs else None
            mul_args = (parsed_args[-1].startswith("*") ^ mul_kwargs) or (len(parsed_args) > 1 and parsed_args[-2].startswith("*"))
            mul_kwargs_kw = parsed_args[:-(1+mul_kwargs)] if mul_args else None
        else:
            mul_kwargs = mul_args = False

    def final_function(*args, **kwargs):
        if not in_args and not in_kwargs:
            return code

        if len(args) + len(kwargs) < len(in_args):
            raise ArgumentNumberMismatch(
                "Expected minimum of {} arguments, received {}.".format(
                    len(in_args), len(args)+len(kwargs)
                )
            )

        true_args = {}

        if len(args) < len(in_args):
            stop_point = 0
            for arg, supposed_arg in zip(args, in_args):
                true_args[supposed_arg] = arg
            
            for arg in in_args[len(args):]:
                if arg not in kwargs:
                    raise ArgumentNumberMismatch(
                        "Mandatory parameter {} does not have an argument.".format(
                            arg
                        )
                    )
                else:
                    true_args[arg] = kwargs.pop(arg)

        elif len(args) == len(in_args):
            true_args = {
                arg_name: arg for arg_name, arg in zip(in_args, args)
            }

        else:
            true_args = {
                arg_name: arg for arg_name, arg in zip(in_args, args)
            }

            for index in range(len(true_args), len(args)):
                if index not in in_kwargs_index:
                    raise ArgumentNumberMismatch(
                        "Expected maximum of {} arguments, received {}.".format(
                            len(in_args) + len(in_kwargs), len(args) + len(kwargs)
                        )
                    )
                else:
                    true_args[in_kwargs_index[index]] = args[index]

        for keyword_arg in in_kwargs:
            if keyword_arg not in true_args:
                if keyword_arg not in kwargs:
                    true_args[keyword_arg] = in_kwargs[keyword_arg]
                else:
                    true_args[keyword_arg] = kwargs.pop(keyword_arg)

        ## use string substitution to generate an ancile program
        ## using the function parameters

        var_regex = r"([^\w])(" + "|".join(true_args) + r")([^\w])"
        repl_function = regex_repl_function(true_args)

        final_code = re.sub(var_regex, repl_function, code)
        return final_code
    return final_function

def regex_repl_function(true_args):
    
    def repl_function(match_object):
        before, arg, after = match_object.groups()
        real_arg = true_args[arg]
        if isinstance(real_arg, str):
            true_arg = "\'" + real_arg + "\'"
        else:
            true_arg = str(real_arg)

        return before + true_arg + after

    return repl_function
