import sys
from io import StringIO

import pytest

from src.main import main


def run_cli(args):
    stdout = StringIO()
    stderr = StringIO()
    old_out, old_err = sys.stdout, sys.stderr
    try:
        sys.stdout, sys.stderr = stdout, stderr
        code = main(args)
    finally:
        sys.stdout, sys.stderr = old_out, old_err
    return code, stdout.getvalue().strip(), stderr.getvalue().strip()


@pytest.mark.parametrize(
    "args,expected",
    [
        (["add", "2", "3"], "5.0"),
        (["subtract", "5", "3"], "2.0"),
        (["multiply", "2", "3"], "6.0"),
        (["divide", "6", "3"], "2.0"),
    ],
)
def test_cli_happy_paths(args, expected):
    code, out, err = run_cli(args)
    assert code == 0
    assert out == expected
    assert err == ""


def test_cli_divide_by_zero_error():
    code, out, err = run_cli(["divide", "1", "0"])
    assert code == 2
    assert out == ""
    assert "Error: Cannot divide by zero." in err
