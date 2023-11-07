import pytest
from src import maths_operation

def test_sum_nums():
    result = maths_operation.sum_nums(1, 2)
    assert result == 3

def test_sum_nums_fail():
    result = maths_operation.sum_nums(1, 2)
    assert result == 2

def test_multiplication_nums():
    result = maths_operation.multiplication_nums(2, 3)
    assert result == 6

def test_sum_strings():
    result = maths_operation.sum_strings("Hello! ", "Devesh")
    assert result == "Hello! Devesh"