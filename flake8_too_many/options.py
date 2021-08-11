from dataclasses import dataclass


@dataclass
class Options:
    """List of configurable options of the `flake8-too-many` plugin."""

    max_function_arguments: int
