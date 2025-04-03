import pytest
from fibonacci import Fibonacci

"""Tests for the non-integer values entered"""


def test_float():
    with pytest.raises(ValueError):
        list(Fibonacci(1.5))


def test_input_zero():
    fib_list = [num for num in Fibonacci(0)]
    assert fib_list == [0]
