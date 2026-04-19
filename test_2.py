from HW_1 import repeating_number
import pytest
import random

def test_not_arr():
    assert repeating_number([]) == 0

def test_incorrect_type_str():

    with pytest.raises(TypeError):
        repeating_number("2")

# Позитивные тесты:
def test_numbers_regular_1():
    assert repeating_number([1, 2, 2, 3, 2, 5, 6, 5, 8, 0, 5, 9, 5]) == 5

def test_numbers_regular_2():
    assert repeating_number([1, -2, -2, 3, -2, 5, 6, 5, -2, 8, 0, 5, 9, 5]) == -2

# Негативные тесты:
def test_repeating_number_incorrect_type_1():

    with pytest.raises(TypeError):
        repeating_number([2, 3, 2, "5"])

def test_repeating_number_incorrect_type_2():

    with pytest.raises(TypeError):
        repeating_number([1, 1, 2, None])

# Пограничные тесты:
def test_repeating_number_one_pozitive_elem():
    assert repeating_number([1]) == 1

def test_repeating_number_border_list():
    assert repeating_number([1, 5, 5, 10000, 6, 20000, 20000, 9000, 20000, 0]) == 20000

def test_repeating_number_on_list_once():
    assert repeating_number([2, 3, 5]) == 2
