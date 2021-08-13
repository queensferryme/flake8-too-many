import ast
from ast import AsyncFunctionDef, FunctionDef
from typing import Optional, Tuple, Union

from flake8_too_many.messages import TMN003


AnyFunctionDef = Union[AsyncFunctionDef, FunctionDef]


def get_number_of_return_stmts(fn: AnyFunctionDef) -> int:
    """Get the number of return statements in a function."""
    number = 0
    for node in ast.walk(fn):
        if isinstance(node, ast.Return):
            number += 1
    return number


def validate_function_return_stmts(
    fn: AnyFunctionDef, max_function_return_stmts: int
) -> Optional[Tuple[int, int, str]]:
    """Validate if there are too many return statements in a function."""
    n = get_number_of_return_stmts(fn)
    if n > max_function_return_stmts:
        return (fn.lineno, fn.col_offset, TMN003.format(n, max_function_return_stmts))
    return None
