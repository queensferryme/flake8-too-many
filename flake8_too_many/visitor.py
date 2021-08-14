import ast
from typing import Any, List, Optional, Tuple

from flake8_too_many.utils.function_return_stmts import validate_function_return_stmts

from .options import Options
from .utils import validate_function_arguments, validate_function_return_values


class Visitor(ast.NodeVisitor):
    """Visit each node of an Abstract Syntax Tree (AST)."""

    def __init__(self, options: Options) -> None:
        super().__init__()
        self.errors: List[Tuple[int, int, str]] = []
        self.options = options

    def add_error(self, error: Optional[Tuple[int, int, str]]) -> None:
        """Add error to the `self.errors` list if it exists."""
        if error is None:
            return
        self.errors.append(error)

    def visit_AsyncFunctionDef(  # noqa: D102, N802
        self, fn: ast.AsyncFunctionDef
    ) -> Any:
        # TMN001
        error = validate_function_arguments(fn, self.options.max_function_arguments)
        self.add_error(error)
        # TMN003
        error = validate_function_return_stmts(
            fn, self.options.max_function_return_stmts
        )
        self.add_error(error)
        return self.generic_visit(fn)

    def visit_FunctionDef(self, fn: ast.FunctionDef) -> Any:  # noqa: D102, N802
        # TMN001
        error = validate_function_arguments(fn, self.options.max_function_arguments)
        self.add_error(error)
        # TMN003
        error = validate_function_return_stmts(
            fn, self.options.max_function_return_stmts
        )
        self.add_error(error)
        return self.generic_visit(fn)

    def visit_Lambda(self, fn: ast.Lambda) -> Any:  # noqa: D102, N802
        # TMN001
        error = validate_function_arguments(fn, self.options.max_function_arguments)
        self.add_error(error)
        return self.generic_visit(fn)

    def visit_Return(self, rt: ast.Return) -> Any:  # noqa: D102, N802
        # TMN002
        error = validate_function_return_values(
            rt, self.options.max_function_return_values
        )
        self.add_error(error)
        return self.generic_visit(rt)
