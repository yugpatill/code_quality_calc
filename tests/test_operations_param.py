import math

import pytest

from src.operations import add, divide, multiply, subtract


@pytest.mark.parametrize(
    "a,b,expected",
    [
        (0, 0, 0),
        (2, 3, 5),
        (-2, 3, 1),
        (2.5, 0.5, 3.0),
    ],
)
def test_add_param(a, b, expected):
    assert add(a, b) == expected


@pytest.mark.parametrize(
    "a,b,expected",
    [
        (0, 0, 0),
        (5, 3, 2),
        (-2, -3, 1),
        (2.5, 0.5, 2.0),
    ],
)
def test_subtract_param(a, b, expected):
    assert subtract(a, b) == expected


@pytest.mark.parametrize(
    "a,b,expected",
    [
        (0, 0, 0),
        (2, 3, 6),
        (-2, 3, -6),
        (2.5, 2, 5.0),
    ],
)
def test_multiply_param(a, b, expected):
    assert multiply(a, b) == expected


@pytest.mark.parametrize(
    "a,b,expected",
    [
        (6, 3, 2.0),
        (2.5, 0.5, 5.0),
        (-6, 3, -2.0),
    ],
)
def test_divide_param(a, b, expected):
    assert math.isclose(divide(a, b), expected)


def test_divide_by_zero_param():
    with pytest.raises(ValueError):
        divide(1, 0)
