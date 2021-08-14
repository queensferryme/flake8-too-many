import ast
from typing import Optional, Tuple, Union

from ..messages import TMN002


AnyReturn = Union[ast.Return, ast.Yield]


def get_number_of_return_values(rt: AnyReturn) -> int:
    """Get the number of function return values."""
    value = rt.value
    if value is None:
        return 0
    elif not isinstance(value, (ast.List, ast.Tuple)):
        return 1
    return len(value.elts)


def validate_function_return_values(
    rt: AnyReturn, max_function_return_values: int
) -> Optional[Tuple[int, int, str]]:
    """Validate if there are too many function return values."""
    n = get_number_of_return_values(rt)
    if n > max_function_return_values:
        return (rt.lineno, rt.col_offset, TMN002.format(n, max_function_return_values))
    return None
