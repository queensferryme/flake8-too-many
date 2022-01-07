import subprocess
import sys

from flake8_too_many.messages import TMN001


file = "tests/files/function_arguments.py"


def test() -> None:
    """Test default option `--max-function-arguments`."""
    process = subprocess.run(["flake8", file], stdout=subprocess.PIPE)
    error1, error2, count = process.stdout.decode("utf-8").splitlines()
    if sys.version_info < (3, 7):
        assert error1.endswith(f"7:7: {TMN001.format(7, 6)}")
    else:
        assert error1.endswith(f"7:1: {TMN001.format(7, 6)}")
    assert error2.endswith(f"12:1: {TMN001.format(7, 6)}")
    assert int(count) == 2


def test_with_max_function_arguments() -> None:
    """Test customized option `--max-function-arguments`."""
    process = subprocess.run(
        ["flake8", "--max-function-arguments=5", file], stdout=subprocess.PIPE
    )
    *errors, count = process.stdout.decode("utf-8").splitlines()
    assert errors[0].endswith(f"2:1: {TMN001.format(6, 5)}")
    if sys.version_info < (3, 7):
        assert errors[1].endswith(f"7:7: {TMN001.format(7, 5)}")
    else:
        assert errors[1].endswith(f"7:1: {TMN001.format(7, 5)}")
    assert errors[2].endswith(f"12:1: {TMN001.format(7, 5)}")
    assert int(count) == 3


def test_with_ignore_defaulted_arguments() -> None:
    """Test customized option `--ignore-defaulted-arguments`."""
    process = subprocess.run(
        ["flake8", "--ignore-defaulted-arguments=true", file], stdout=subprocess.PIPE
    )
    error, count = process.stdout.decode("utf-8").splitlines()
    assert error.endswith(f"12:1: {TMN001.format(7, 6)}")
    assert int(count) == 1
