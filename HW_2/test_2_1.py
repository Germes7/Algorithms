from .HW_2 import factorial
import pytest

def test_factorial_incorrect_type_str():

    with pytest.raises(TypeError):
        factorial("5")

def test_factorial_negative_value():

    with pytest.raises(ValueError):
        factorial(-2)

def test_factorial_value_zero():
    assert factorial(0) == 1

# Позитивные тесты:
def test_factorial_1():
    assert factorial(5) == 120

def test_factorial_2():
    assert factorial(1) == 1

# Негативные тесты:
def test_factorial_incorrect_type_float():
    with pytest.raises(TypeError):
        factorial(1.5)

# Пограничные тесты:
def test_iinput_border_value1():
    assert factorial(2) == 2

def test_iinput_border_value2():
    assert factorial(20) == 2432902008176640000