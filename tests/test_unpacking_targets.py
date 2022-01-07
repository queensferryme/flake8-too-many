import subprocess


file = "tests/files/unpacking_targets.py"


def test() -> None:
    """Test default option `--max-unpacking-targets`."""
    process = subprocess.run(["flake8", file], stdout=subprocess.PIPE)
    error1, error2, count = process.stdout.decode("utf-8").splitlines()
    assert error1.endswith("2:1: TMN004 unpacking has too many targets (7 > 3).")
    assert error2.endswith("9:1: TMN004 unpacking has too many targets (6 > 3).")
    assert int(count) == 2


def test_with_args() -> None:
    """Test customized option `--max-unpacking-targets`."""
    process = subprocess.run(
        ["flake8", "--max-unpacking-targets=6", file], stdout=subprocess.PIPE
    )
    error, count = process.stdout.decode("utf-8").splitlines()
    assert error.endswith("2:1: TMN004 unpacking has too many targets (7 > 6).")
    assert int(count) == 1
