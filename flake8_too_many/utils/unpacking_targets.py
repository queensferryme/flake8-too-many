import ast
from typing import Optional, Tuple, Union

from flake8_too_many.messages import TMN004


def get_number_of_unpacking_targets_in_assignments(node: ast.Assign) -> int:
    """Get the number of unpacking targets in an `assignment` expression."""
    if len(node.targets) > 1:
        return 1
    target = node.targets[0]
    if not isinstance(target, (ast.List, ast.Tuple)):
        return 1
    return len(target.elts)


def get_number_of_unpacking_targets_in_for_loops(node: ast.For) -> int:
    """Get the number of unpacking targets in a `for` loop."""
    target = node.target
    if not isinstance(target, (ast.List, ast.Tuple)):
        return 1
    return len(target.elts)


def validate_unpacking_targets(
    node: Union[ast.Assign, ast.For], max_unpacking_targets: int
) -> Optional[Tuple[int, int, str]]:
    """Validate if there are too many unpacking targets."""
    n = 0
    if isinstance(node, ast.Assign):
        n = get_number_of_unpacking_targets_in_assignments(node)
    else:
        n = get_number_of_unpacking_targets_in_for_loops(node)
    if n > max_unpacking_targets:
        return (node.lineno, node.col_offset, TMN004.format(n, max_unpacking_targets))
    return None
