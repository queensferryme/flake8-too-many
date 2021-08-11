import ast
from typing import Any, List, Tuple

from .options import Options
from .utils import validate_function_arguments


class Visitor(ast.NodeVisitor):
    """Visit each node of an Abstract Syntax Tree (AST)."""

    def __init__(self, options: Options) -> None:
        super().__init__()
        self.errors: List[Tuple[int, int, str]] = []
        self.options = options

    def visit_AsyncFunctionDef(self, fn: ast.AsyncFunctionDef) -> Any:  # noqa: N802
        """Visit `ast.AsyncFunctionDef` nodes."""
        error = validate_function_arguments(fn, self.options.max_function_arguments)
        if error is not None:
            self.errors.append(error)
        return self.generic_visit(fn)

    def visit_FunctionDef(self, fn: ast.FunctionDef) -> Any:  # noqa: N802
        """Visit `ast.FunctionDef` nodes."""
        error = validate_function_arguments(fn, self.options.max_function_arguments)
        if error is not None:
            self.errors.append(error)
        return self.generic_visit(fn)

    def visit_Lambda(self, fn: ast.Lambda) -> Any:  # noqa: N802
        """Visit `ast.Lambda` nodes."""
        error = validate_function_arguments(fn, self.options.max_function_arguments)
        if error is not None:
            self.errors.append(error)
        return self.generic_visit(fn)
