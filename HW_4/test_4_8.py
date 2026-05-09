import pytest
from .HW_4 import fibonacci
from hypothesis import given, strategies as st

def test_fibonacci_incorrect_value():

    with pytest.raises(TypeError):
        fibonacci(1.5)

def test_fibonacci_sub_zero_value():

    with pytest.raises(ValueError):
        fibonacci(-5)

# Позитивные тесты:
def test_fibonacci_pozitive_1():
    assert fibonacci(2) == 1

def test_fibonacci_pozitive_2():
    assert fibonacci(3) == 2

def test_fibonacci_pozitive_3():
    assert fibonacci(4) == 3

def test_fibonacci_pozitive_4():
    assert fibonacci(10) == 55

def test_fibonacci_pozitive_5():
    assert fibonacci(20) == 6765

# Негативные тесты:
def test_fibonacci_negative_1():

    with pytest.raises(TypeError):
        fibonacci([])

def test_fibonacci_negative_2():

    with pytest.raises(TypeError):
        fibonacci(None)

# Пограничные тесты:
def test_fibonacci_border_1():
    assert fibonacci(0) == 0

def test_fibonacci_border_2():
    assert fibonacci(1) == 1

def test_fibonacci_border_3():
    assert fibonacci(35) == 9227465

@given(st.integers(min_value=0, max_value=23))
def test_fibonacci(n):

    result = fibonacci(n)
    fib_1 = [0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55]

    if n < len(fib_1):
        assert result == fib_1[n]
    if n > 1:
        assert result >= fibonacci(n - 1)