import subprocess
import sys

from flake8_too_many.messages import TMN001


file = "tests/files/function_arguments.py"


def test() -> None:
    """Test default option `--max-function-arguments`."""
    process = subprocess.run(["flake8", file], stdout=subprocess.PIPE)
    e1, e2, e3, count = process.stdout.decode("utf-8").splitlines()
    assert e1.endswith(f"2:1: {TMN001.format(6, 5)}")
    if sys.version_info < (3, 7):
        assert e2.endswith(f"7:7: {TMN001.format(7, 5)}")
    else:
        assert e2.endswith(f"7:1: {TMN001.format(7, 5)}")
    assert e3.endswith(f"12:1: {TMN001.format(7, 5)}")
    assert int(count) == 3


def test_with_args() -> None:
    """Test customized option `--max-function-arguments`."""
    process = subprocess.run(
        ["flake8", "--max-function-arguments=6", file], stdout=subprocess.PIPE
    )
    e1, e2, count = process.stdout.decode("utf-8").splitlines()
    if sys.version_info < (3, 7):
        assert e1.endswith(f"7:7: {TMN001.format(7, 6)}")
    else:
        assert e1.endswith(f"7:1: {TMN001.format(7, 6)}")
    assert e2.endswith(f"12:1: {TMN001.format(7, 6)}")
    assert int(count) == 2
