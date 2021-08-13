import subprocess


file = "tests/files/function_return_values.py"


def test() -> None:
    """Test default option `--max-function-return-values`."""
    process = subprocess.run(["flake8", file], stdout=subprocess.PIPE)
    e1, e2, e3, count = process.stdout.decode("utf-8").splitlines()
    assert e1.endswith("7:5: TMN002 function returns too many values (5 > 3).")
    assert e2.endswith("12:5: TMN002 function returns too many values (5 > 3).")
    assert e3.endswith("17:5: TMN002 function returns too many values (6 > 3).")
    assert int(count) == 3


def test_with_args() -> None:
    """Test customized option `--max-function-return-values`."""
    process = subprocess.run(
        ["flake8", "--max-function-return-values=5", file], stdout=subprocess.PIPE
    )
    e1, count = process.stdout.decode("utf-8").splitlines()
    assert e1.endswith("17:5: TMN002 function returns too many values (6 > 5).")
    assert int(count) == 1
