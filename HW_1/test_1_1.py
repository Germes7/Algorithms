from HW_1 import sum_even_numbers
import pytest

def test_not_arr():
    assert sum_even_numbers([]) == 0

def test_sum_even_numbers_incorrect_type_str():

    with pytest.raises(TypeError):
        sum_even_numbers("1")

def test_sum_even_numbers_incorrect_type_list_natural_number():
    with pytest.raises(TypeError):
        sum_even_numbers([1.5])

# Позитивные тесты:
def test_sum_even_numbers_regular_list():
    assert sum_even_numbers([1, 2, 4, 7, 0, 6, 3]) == 12

def test_sum_even_numbers_all_even_numbers_of_list():
    assert sum_even_numbers([2, 4, 8, 6, 12]) == 32

def test_sum_even_numbers_negative_numbers_of_list():
    assert sum_even_numbers([2, 4, -8, 6, -12]) == 1

# Негативные тесты:
def test_sum_even_numbers_incorrect_type_1():

    with pytest.raises(TypeError):
        sum_even_numbers([2, 4, 1.5])

def test_sum_even_numbers_incorrect_type_2():

    with pytest.raises(TypeError):
        sum_even_numbers([1, 2, None])

# Пограничные тесты:
def test_sum_even_numbers_one_pozitive_elem():
    assert sum_even_numbers([4]) == 4

def test_sum_even_numbers_one_negative_elem():
    assert sum_even_numbers([-2]) == 1

def test_sum_even_numbers_border_list_1():
    assert sum_even_numbers([-20000, 1, 20000]) == 0

def test_sum_even_numbers_border_list_2():
    assert sum_even_numbers([20000, 2, 20000]) == 40002

def test_sum_even_numbers_border_list_3():
    assert sum_even_numbers([-20000, 3, -20000]) == 1

def test_sum_even_numbers_border_list_4():
    assert sum_even_numbers([1, 3, 5]) == 0