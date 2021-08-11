import ast
from typing import Iterable, Tuple, Type

from .visitor import Visitor


class Checker:
    """A check plugin for flake8.

    This class is registered via `setuptools` entry points, by adding these two lines \
    below to `pyproject.toml`.
    ```toml
    [tool.poetry.plugins."flake8.extension"]
    TMN = "flake8_too_many:Checker"
    ```
    Plugins need to be registered so that flake8 could discover & load them.
    """

    name = "flake8-too-many"
    version = "0.1.0"

    def __init__(self, tree: ast.Module) -> None:
        self.tree = tree

    def run(self) -> Iterable[Tuple[int, int, str, Type["Checker"]]]:
        """Run the `flake8-too-many` plugin over one python module."""
        visitor = Visitor()
        visitor.visit(self.tree)
        for error in visitor.errors:
            yield (*error, Checker)
