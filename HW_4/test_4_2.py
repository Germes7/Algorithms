import pytest

from .HW_4 import choice_sort
from hypothesis import given, strategies as st

def test_choice_sort_incorrect_list():

    with pytest.raises(TypeError):
        choice_sort("7")

def test_choice_sort_empty_list():

    with pytest.raises(ValueError):
        choice_sort([])

@pytest.fixture
def array_1():
    return [3, 8, 1, 5, -4, 0, 7]

@pytest.fixture
def array_2():
    return ["Призма", "Вол", "Лодка", "Пень"]

@pytest.fixture
def array_3():
    return [7, 7, 7, 7]

@pytest.fixture
def array_4():
    return [33, 18, 21, 15, 4, 18, 10, 27, 10]

@pytest.fixture
def array_5():
    return [33, "18", 21]

@pytest.fixture
def array_6():
    return [1, 2, 3, 4, 5]

@pytest.fixture
def array_7():
    return [211, 19, 18, 17, 16, 15, 14, 13, 12, 11, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1, 0]

# Позитивные тесты:
def test_choice_sort_pozitive_1(array_1):
    assert choice_sort(array_1) == ([-4, 0, 1, 3, 5, 7, 8], 21, 4)

def test_choice_sort_pozitive_2(array_1):
    assert choice_sort(array_1, key=lambda x: x, order_by=lambda x, y: x > y) == ([8, 7, 5, 3, 1, 0, -4], 21, 5)

def test_choice_sort_pozitive_3(array_2):
    assert choice_sort(array_2) == (['Вол', 'Лодка', 'Пень', 'Призма'], 6, 3)

def test_choice_sort_pozitive_4(array_2):
    assert choice_sort(array_2, key=len) == (['Вол', 'Пень', 'Лодка', 'Призма'], 6, 2)

def test_choice_sort_pozitive_5(array_3):
    assert choice_sort(array_3, order_by=lambda x, y: x < y) == ([7, 7, 7, 7], 6, 0)

def test_choice_sort_pozitive_6(array_4):
    assert choice_sort(array_4, order_by=lambda x, y: x <= y) == ([4, 10, 10, 15, 18, 18, 21, 27, 33], 36, 4)

# Негативные тесты:
def test_choice_sort_negative_1():

    with pytest.raises(TypeError):
        choice_sort(None)

def test_choice_sort_negative_2(array_5):

    with pytest.raises(TypeError):
        choice_sort(array_5)

def test_choice_sort_negative_3(array_1):

    with pytest.raises(TypeError):
        choice_sort(array_1, key=2)

def test_choice_sort_negative_4(array_1):

    with pytest.raises(TypeError):
        choice_sort(array_1, key=lambda x: x, order_by=lambda x: x)

# Пограничные тесты:
def test_choice_sort_border_1():
    assert choice_sort([7]) == ([7], 0, 0)

def test_choice_sort_border_2(array_6):
    assert choice_sort(array_6) == ([1, 2, 3, 4, 5], 10, 0)

def test_choice_sort_border_3(array_6):
    assert choice_sort(array_6, key=lambda x: x, order_by=lambda x, y: x <= y) == ([1, 2, 3, 4, 5], 10, 0)

def test_choice_sort_border_4(array_3):
    assert choice_sort(array_3, key=lambda x: x, order_by=lambda x, y: x <= y) == ([7, 7, 7, 7], 6, 3)

def test_choice_sort_border_5(array_7):
    assert choice_sort(array_7) == ([0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 211], 210, 10)

def test_choice_sort_border_6():
    assert choice_sort([1, 0]) == ([0, 1], 1, 1)

def test_choice_sort_border_7():
    assert choice_sort([7]) == ([7], 0, 0)

# Тесты через Hypothesis:
@given(st.lists(st.integers(), min_size=1, max_size=100))
def test_choice_sort(random_list):
    arr_to_sort = random_list.copy()

    result, comparisons, exchanges = choice_sort(arr_to_sort)
    assert result == sorted(random_list)