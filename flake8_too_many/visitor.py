import ast
from typing import Any

from .utils import validate_function_argument


class Visitor(ast.NodeVisitor):
    def __init__(self) -> None:
        super().__init__()
        self.errors = []

    def visit_AsyncFunctionDef(self, fn: ast.AsyncFunctionDef) -> Any:
        error = validate_function_argument(fn)
        if error is not None:
            self.errors.append(error)
        return self.generic_visit(fn)

    def visit_FunctionDef(self, fn: ast.FunctionDef) -> Any:
        error = validate_function_argument(fn)
        if error is not None:
            self.errors.append(error)
        return self.generic_visit(fn)

    def visit_Lambda(self, fn: ast.Lambda) -> Any:
        error = validate_function_argument(fn)
        if error is not None:
            self.errors.append(error)
        return self.generic_visit(fn)
