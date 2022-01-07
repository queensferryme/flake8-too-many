import subprocess


file = "tests/files/function_return_values.py"


def test() -> None:
    """Test default option `--max-function-return-values`."""
    process = subprocess.run(["flake8", file], stdout=subprocess.PIPE)
    *errors, count = process.stdout.decode("utf-8").splitlines()
    assert errors[0].endswith("7:5: TMN002 function returns too many values (5 > 3).")
    assert errors[1].endswith("12:5: TMN002 function returns too many values (5 > 3).")
    assert errors[2].endswith("17:5: TMN002 function returns too many values (6 > 3).")
    assert int(count) == 3


def test_with_args() -> None:
    """Test customized option `--max-function-return-values`."""
    process = subprocess.run(
        ["flake8", "--max-function-return-values=5", file], stdout=subprocess.PIPE
    )
    error, count = process.stdout.decode("utf-8").splitlines()
    assert error.endswith("17:5: TMN002 function returns too many values (6 > 5).")
    assert int(count) == 1
