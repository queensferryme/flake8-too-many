# flake8-too-many

[![pre-commit.ci status](https://results.pre-commit.ci/badge/github/queensferryme/flake8-too-many/master.svg)](https://results.pre-commit.ci/latest/github/queensferryme/flake8-too-many/master)
[![github ci status](https://img.shields.io/github/workflow/status/queensferryme/flake8-too-many/Test?label=test&logo=github&message=passed)](https://github.com/RSSerpent/RSSerpent/actions/workflows/test.yaml)
[![codecov](https://codecov.io/gh/queensferryme/flake8-too-many/branch/master/graph/badge.svg?token=56VCCB1JUB)](https://codecov.io/gh/queensferryme/flake8-too-many)

A flake8 plugin that prevents you from writing "too many" bad codes.

## Installation

with `pip`

```shell
pip install flake8-too-many
```

with [`poetry`](https://python-poetry.org/)

```shell
poetry add -D flake8-too-many
```

with [`pre-commit`](https://pre-commit.com/) ([doc](https://flake8.pycqa.org/en/latest/user/using-hooks.html))

```yaml
repos:
  - repo: https://github.com/PyCQA/flake8
    rev: '' # pick a git hash/tag
    hooks:
      - id: flake8
        additional_dependencies:
          # ...
          - flake8-too-many
```

## Error Codes

| code   | description                       | example                                                      |
| ------ | --------------------------------- | ------------------------------------------------------------ |
| TMN001 | function has too many arguments.  | [link](https://github.com/queensferryme/flake8-too-many/blob/master/tests/files/function_arguments.py) |
| TMN002 | function returns too many values. | [link](https://github.com/queensferryme/flake8-too-many/blob/master/tests/files/function_return_values.py) |

## Options

These options could be either passed in as command line flags, or specified in a `.flake8` configuration file.

* `--max-function-arguments`, int, default to 5;
* `--max-function-return-values`, int, default to 3.

Run `flake8 -h` for detailed description of each option.
