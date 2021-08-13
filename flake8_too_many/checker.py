import ast
from argparse import Namespace
from typing import Iterable, Tuple, Type

from flake8.options.manager import OptionManager  # type: ignore[import]

from .options import Options
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
    version = "0.1.0-alpha.0"

    options: Options

    def __init__(self, tree: ast.Module) -> None:
        self.tree = tree

    @classmethod
    def add_options(  # type: ignore[no-any-unimported]
        cls, parser: OptionManager
    ) -> None:
        """Define configurable options of the `flake8-too-many` plugin."""
        parser.add_option(
            "--max-function-arguments",
            default=5,
            parse_from_config=True,
            type=int,
            help="Maximum number of function arguments allowed",
        )
        parser.add_option(
            "--max-function-return-values",
            default=3,
            parse_from_config=True,
            type=int,
            help="Maximum number of function return values allowed",
        )

    @classmethod
    def parse_options(cls, options: Namespace) -> None:
        """Store parsed options in `cls.options`."""
        cls.options = Options(
            **{
                "max_function_arguments": options.max_function_arguments,
                "max_function_return_values": options.max_function_return_values,
            }
        )

    def run(self) -> Iterable[Tuple[int, int, str, Type["Checker"]]]:
        """Run the `flake8-too-many` plugin over one python module."""
        visitor = Visitor(self.options)
        visitor.visit(self.tree)
        for error in visitor.errors:
            yield (*error, Checker)
