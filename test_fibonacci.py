import pytest
from fibonacci import Fibonacci

"""Tests for the non-integer values entered"""


def test_float():
    with pytest.raises(ValueError):
        list(Fibonacci(1.5))


"""Tests for the value zero entered"""


def test_input_zero():
    fib_list = [num for num in Fibonacci(0)]
    assert fib_list == [0]


"""Tests for the value one entered"""


def test_input_one():
    fib_list = [num for num in Fibonacci(1)]
    assert fib_list == [0, 1]

    """Tests for the value two entered"""


def test_input_two():
    fib_list = [num for num in Fibonacci(2)]
    assert fib_list == [0, 1, 1]
