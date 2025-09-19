from src.operations import addition, subtraction, multiply

def test_addition():
    assert addition(2, 3) == 5

def test_subtraction():
    assert subtraction(5, 3) == 2

def test_multiply():
    assert multiply(2, 3) == 6
