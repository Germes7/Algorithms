from HW_1 import output_iter
import pytest

def test_not_arr():
    assert output_iter([], 5) == 0

def test_incorrect_target():

    with pytest.raises(TypeError):
        output_iter([1, 2], 12.5)

def test_incorrect_arr_and_target():

    with pytest.raises(TypeError):
        output_iter("", 1.5)

def test_incorrect_elem_in_arr():

    with pytest.raises(TypeError):
        output_iter([1, 3, "5", 4], 8)

# Позитивные тесты:
def test_output_iter_pozitive_1():
    assert output_iter([1, 5, 3, 0, 7], 6) == [0, 1]

def test_output_iter_pozitive_2():
    assert output_iter([-1, -5, -7, -3], -8) == [0, 2]

# Негативные тесты:
def test_output_iter_no_true_target():
    assert output_iter([1, 2, 3, 5], 9) == []

def test_output_iter_one_elem_in_arr_equal_target():
    assert output_iter([3], 3) == []

# Пограничные тесты:
def test_output_iter_numbers_border_list_1():
    assert output_iter([-109, 2, 5, 100, 35, 4, 0, 15, 109], 6) ==[1, 5]

def test_output_iter_numbers_border_list_2():
    assert output_iter([3, 3], 6) == [0, 1]

def test_output_iter_numbers_border_list_3():
    assert output_iter([-6, 10, 12, 100, 13, 0, 9, 17], 109) == [3, 6]

def test_output_iter__zero_target():
    assert output_iter([0, 1, 2, 0], 0) == [0, 3]