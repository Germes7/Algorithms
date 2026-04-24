from .HW_2 import count_ones
import pytest

def test_count_ones_incorrect_type_empty_str():

    with pytest.raises(ValueError):
        count_ones("")

def test_count_ones_incorrect_type_sub_zero():

    with pytest.raises(ValueError):
        count_ones(-5)

# Позитивные тесты:
def test_count_ones_pozitive1():
    assert count_ones(6) == 2

def test_count_ones_pozitive2():
    assert count_ones(0) == 0

# Негативные тесты:
def test_count_ones_incorrect_type_str():

    with pytest.raises(TypeError):
        count_ones("5")

def test_count_ones_incorrect_type_float():

    with pytest.raises(TypeError):
        count_ones(1.5)

# Пограничные тесты:
def test_count_ones_input_border_value1():
    assert count_ones(1) == 1

def test_count_ones_input_border_value2():
    assert count_ones(1000000000) == 13