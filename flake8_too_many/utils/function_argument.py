from ast import AsyncFunctionDef, FunctionDef, Lambda
from typing import Optional, Tuple, Union

from ..message import TMN001


AnyFunctionDef = Union[AsyncFunctionDef, FunctionDef, Lambda]


def get_number_of_arguments(fn: AnyFunctionDef) -> int:
    """Get the number of function arguments."""
    arguments = fn.args
    number = 0
    # position-only arguments are only available in py3.8+
    number += len(getattr(arguments, "posonlyargs", ""))
    number += len(arguments.args)
    number += 1 if arguments.vararg else 0
    number += len(arguments.kwonlyargs)
    number += 1 if arguments.kwarg else 0
    return number


def validate_function_argument(fn: AnyFunctionDef) -> Optional[Tuple[int, int, str]]:
    """Validate if there are too many function arguments."""
    n = get_number_of_arguments(fn)
    if n > 5:
        return (
            fn.lineno,
            fn.col_offset,
            # `ast.Lambda` nodes don't have the `name` attribute
            TMN001.format(getattr(fn, "name", "lambda"), n, 5),
        )
