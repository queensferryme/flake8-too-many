from dataclasses import dataclass


@dataclass
class Options:
    """List of configurable options of the `flake8-too-many` plugin."""

    ignore_defaulted_arguments: bool
    max_function_arguments: int
    max_function_return_stmts: int
    max_function_return_values: int
    max_unpacking_targets: int
