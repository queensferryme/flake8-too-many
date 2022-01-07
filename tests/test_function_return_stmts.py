import subprocess


file = "tests/files/function_return_stmts.py"


def test() -> None:
    """Test default option `--max-function-return-stmts`."""
    process = subprocess.run(["flake8", file], stdout=subprocess.PIPE)
    error, count = process.stdout.decode("utf-8").splitlines()
    assert error.endswith(
        "2:1: TMN003 function has too many return statements (6 > 3)."
    )
    assert int(count) == 1


def test_with_args() -> None:
    """Test customized option `--max-function-return-stmts`."""
    process = subprocess.run(
        ["flake8", "--max-function-return-stmts=6", file], stdout=subprocess.PIPE
    )
    count, *_ = process.stdout.decode("utf-8").splitlines()
    assert int(count) == 0
