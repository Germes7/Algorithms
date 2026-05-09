import pytest
from .HW_4 import sum_of_digits
from hypothesis import given, strategies as st

def test_sum_of_digits_incorrect_value():

    with pytest.raises(TypeError):
        sum_of_digits(1.7)

# Позитивные тесты:
def test_sum_of_digits_pozitive_1():
    assert sum_of_digits(2) == 2

def test_sum_of_digits_pozitive_2():
    assert sum_of_digits(237) == 12
def test_sum_of_digits_pozitive_3():
    assert sum_of_digits(1002) == 3
def test_sum_of_digits_pozitive_4():
    assert sum_of_digits(-221) == 5
def test_sum_of_digits_pozitive_5():
    assert sum_of_digits(22222222222) == 22

# Негативные тесты:
def test_sum_of_digits_negative_1():

    with pytest.raises(TypeError):
        sum_of_digits("123")

def test_sum_of_digits_negative_2():

    with pytest.raises(TypeError):
        sum_of_digits([1, 2, 3])

def test_sum_of_digits_negative_3():

    with pytest.raises(TypeError):
        sum_of_digits(None)

# Пограничные тесты:
def test_sum_of_digits_border_1():
    assert sum_of_digits(0) == 0

def test_sum_of_digits_border_2():
    assert sum_of_digits(91011) == 12

def test_sum_of_digits_border_3():
    assert sum_of_digits(1000) == 1

def test_sum_of_digits_border_4():
    assert sum_of_digits(111111111112222222222233333333333333344444444455555555555566666666666777777777777) == 324

@given(st.integers())
def test_sum_of_digits(n):

    result = sum_of_digits(n)
    assert result >= 0

    if -10 < n < 10:
        assert result == abs(n)

@given(st.integers(min_value=10 ** 100, max_value=10 ** 200))
def test_sum_of_digits_large_numbers(n):

    result = sum_of_digits(n)
    assert result > 0