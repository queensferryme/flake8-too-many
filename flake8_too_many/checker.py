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
    version = "0.1.5"

    options: Options

    def __init__(self, tree: ast.Module) -> None:
        self.tree = tree

    @classmethod
    def add_options(cls, parser: OptionManager) -> None:
        """Define configurable options of the `flake8-too-many` plugin."""
        parser.add_option(
            "--ignore-defaulted-arguments",
            default=False,
            parse_from_config=True,
            type=bool,
            help="Whether to ignore defaulted arguments for option \
                 `--max-function-arguments`",
        )
        parser.add_option(
            "--max-function-arguments",
            default=6,
            parse_from_config=True,
            type=int,
            help="Maximum number of function arguments allowed",
        )
        parser.add_option(
            "--max-function-return-stmts",
            default=3,
            parse_from_config=True,
            type=int,
            help="Maximum number of return statements in a function allowed",
        )
        parser.add_option(
            "--max-function-return-values",
            default=3,
            parse_from_config=True,
            type=int,
            help="Maximum number of function return values allowed",
        )
        parser.add_option(
            "--max-unpacking-targets",
            default=3,
            parse_from_config=True,
            type=int,
            help="Maximum number of unpacking targets allowed",
        )

    @classmethod
    def parse_options(cls, options: Namespace) -> None:
        """Store parsed options in `cls.options`."""
        cls.options = Options(
            **{
                "ignore_defaulted_arguments": options.ignore_defaulted_arguments,
                "max_function_arguments": options.max_function_arguments,
                "max_function_return_stmts": options.max_function_return_stmts,
                "max_function_return_values": options.max_function_return_values,
                "max_unpacking_targets": options.max_unpacking_targets,
            }
        )

    def run(self) -> Iterable[Tuple[int, int, str, Type["Checker"]]]:
        """Run the `flake8-too-many` plugin over one python module."""
        visitor = Visitor(self.options)
        visitor.visit(self.tree)
        for error in visitor.errors:
            yield (*error, Checker)
