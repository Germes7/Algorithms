from .HW_2 import fibonacci
import pytest

def test_fibonacci_incorrect_type_str():

    with pytest.raises(TypeError):
        fibonacci("5")

def test_fibonacci_negative_value():

    with pytest.raises(ValueError):
        fibonacci(-2)

# Позитивные тесты:
def test_fibonacci1():
    assert fibonacci(0) == [0]

def test_fibonacci2():
    assert fibonacci(1) == [0, 1]

def test_fibonacci3():
    assert fibonacci(7) == [0, 1, 1, 2, 3, 5, 8, 13]

# Негативные тесты:
def test_fibonacci_incorrect_type_float():

    with pytest.raises(TypeError):
        fibonacci(2.5)

def test_fibonacci_value_none():
    with pytest.raises(TypeError):
        fibonacci(None)

# Пограничные тесты:
def test_fibonacci_input_border_value1():
    assert fibonacci(2) == [0, 1, 1]

def test_fibonacci_input_border_value2():
    assert fibonacci(20) == [0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144, 233, 377, 610, 987, 1597, 2584, 4181, 6765]