import ast
from .visitor import Visitor


class Checker:
    name = "flake8-too-many"
    version = "0.1.0"

    def __init__(self, tree: ast.Module) -> None:
        self.tree = tree

    def run(self):
        visitor = Visitor()
        visitor.visit(self.tree)
        for error in visitor.errors:
            yield (*error, Checker)
