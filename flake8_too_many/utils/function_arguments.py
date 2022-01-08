from ast import AsyncFunctionDef, FunctionDef, Lambda, arg
from typing import List, Optional, Tuple, Union

from ..messages import TMN001
from ..options import Options


AnyFunctionDef = Union[AsyncFunctionDef, FunctionDef, Lambda]


def get_number_of_arguments(
    fn: AnyFunctionDef, ignore_defaulted_arguments: bool
) -> int:
    """Get the number of function arguments."""
    arguments: List[arg] = []
    # posonlyargs, args, vararg, kwonlyargs, kwarg
    # position-only arguments are only available in py3.8+
    arguments.extend(getattr(fn.args, "posonlyargs", []))
    arguments.extend(fn.args.args)
    if fn.args.vararg:
        arguments.append(fn.args.vararg)
    arguments.extend(fn.args.kwonlyargs)
    if fn.args.kwarg:
        arguments.append(fn.args.kwarg)
    # NOTE: do not count arguments named `_`
    number = len(list(filter(lambda x: x.arg != "_", arguments)))
    if ignore_defaulted_arguments:
        number -= len(fn.args.defaults)
        number -= len(fn.args.kw_defaults)
    return number


def validate_function_arguments(
    fn: AnyFunctionDef, options: Options
) -> Optional[Tuple[int, int, str]]:
    """Validate if there are too many function arguments."""
    n = get_number_of_arguments(fn, options.ignore_defaulted_arguments)
    if n > options.max_function_arguments:
        return (
            fn.lineno,
            fn.col_offset,
            TMN001.format(n, options.max_function_arguments),
        )
    return None
