from .HW_3 import revers_even_elements
import pytest

@pytest.fixture
def check_array():
    return [1, 2, 4, 7, 3]

@pytest.fixture
def check_array_not_even():
    return [1, 3, 5, 7, 9] # все не четные

@pytest.fixture
def check_array_even():
    return [2, 4, 6, 8] # все четные

@pytest.fixture
def check_array_with_zero():
    return [0, 2, 3, 6, 8]

@pytest.fixture
def check_array_1():
    return [1, 2, 3, 7, 11]

@pytest.fixture
def check_array_2():
    return [2, 6]

@pytest.fixture
def check_array_3():
    return [2, 3, 7, 8]

@pytest.fixture
def check_array_4():
    return [1, 2, 4, 7]

@pytest.fixture
def check_array_5():
    return [-1, -2, -7, -4, -17]

def test_revers_even_elements_incorrect_list():

    with pytest.raises(TypeError):
        revers_even_elements("5")

def test_revers_even_elements_not_arr():

    with pytest.raises(ValueError):
        revers_even_elements([])

# Позитивные тесты:
def test_revers_even_elements_pozitive_1(check_array):
    assert revers_even_elements(check_array) == [1, 4, 2, 7, 3]

def test_revers_even_elements_pozitive_even(check_array_even):
    assert revers_even_elements(check_array_even) == [8, 6, 4, 2]

def test_revers_even_elements_pozitive_not_even(check_array_not_even):
    assert revers_even_elements(check_array_not_even) == [1, 3, 5, 7, 9]

def test_revers_even_elements_pozitive_with_zero(check_array_with_zero):
    assert revers_even_elements(check_array_with_zero) == [8, 6, 3, 2, 0]

# Пограничные тесты:
def test_revers_even_elements_border_1(check_array_1):
    assert revers_even_elements(check_array_1) == [1, 2, 3, 7, 11]

def test_revers_even_elements_border_2(check_array_2):
    assert revers_even_elements(check_array_2) == [6, 2]

def test_revers_even_elements_border_3(check_array_3):
    assert revers_even_elements(check_array_3) == [8, 3, 7, 2]

def test_revers_even_elements_border_4(check_array_4):
    assert revers_even_elements(check_array_4) == [1, 4, 2, 7]

def test_revers_even_elements_border_5(check_array_5):
    assert revers_even_elements(check_array_5) == [-1, -4, -7, -2, -17]