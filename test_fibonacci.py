import pytest
from fibonacci import Fibonacci


"""Tests for the non-integer values entered"""


def test_float():
    with pytest.raises(ValueError):
        list(Fibonacci(1.5))

