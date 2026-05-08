import pytest
from .HW_4 import recursive_max
from hypothesis import given, strategies as st

def test_recursive_max_incorrect_list():

    with pytest.raises(TypeError):

        recursive_max("7")

def test_recursive_max_empty_list():
    assert recursive_max([]) == 0

@pytest.fixture
def array_1():
    return [3, 8, 1, 5, -4, 0, 7]

@pytest.fixture
def array_2():
    return [0, 0, 0, 0]

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
    return [1.2, 2.3, 3.4, 4.5, 5.5]

@pytest.fixture
def array_7():
    return [20, 19, 18, 17, 16, 15, 14, 13, 12, 11, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1, 0]

@pytest.fixture
def array_8():
    return [211, 19, 18, 17, 16, 15, 14, 13, 12, 11, 10, 9, 8, 7, 6, 5, 4, 3, 17, 27, 53,
            14, 56, 127, 253, 2, 1, 0, 13, 12, 11, 10, 9, 8, 7, 6, 5, 4, 3, 17, 27, 53,
            253, 2, 1, 0, 13, 12, 11, 10, 9, 16, 15, 14, 13, 12, 11, 10, 9, 8, 7, 6, 5, 4,
            3, 17, 27, 53, 12, 11, 10, 9, 16, 15, 14, 13, 12, 8, 7, 6, 5, 4, 3, 17, 27, 53]

@pytest.fixture
def array_9():
    return [-5, -1, 0.1, 0]

# Позитивные тесты:
def test_recursive_max_pozitive_1(array_1):
    assert recursive_max(array_1) == 8

def test_recursive_max_pozitive_2(array_4):
    assert recursive_max(array_4) == 33

def test_recursive_max_pozitive_3(array_7):
    assert recursive_max(array_7) == 20

def test_recursive_max_pozitive_4(array_6):
    assert recursive_max(array_6) == 5.5

# Негативные тесты:
def test_recursive_max_negative_1(array_5):

    with pytest.raises(TypeError):
        recursive_max(array_5)

def test_recursive_max_negative_2():

    with pytest.raises(TypeError):
        recursive_max([1, 5, None, 3, 7])

def test_recursive_max_negative_3():

    with pytest.raises(TypeError):
        recursive_max(None)

# Пограничные тесты:
def test_recursive_max_border_1(array_2):
    assert recursive_max(array_2) == 0

def test_recursive_max_border_2(array_3):
    assert recursive_max(array_3) == 7

def test_recursive_max_border_3(array_9):
    assert recursive_max(array_9) == 0.1

def test_recursive_max_border_4(array_8):
    assert recursive_max(array_8) == 253

def test_recursive_max_border_5():
    assert recursive_max([7]) == 7

def test_recursive_max_border_6():
    assert recursive_max([0]) == 0

@given(st.lists(st.integers(min_value=-1000000), min_size=0, max_size=1000))
def test_recursive_max_int(random_list):

    arr_to_sort = random_list.copy()
    result = recursive_max(arr_to_sort)
    if not random_list:
        assert result == 0
    else:
        assert result == max(random_list)

@given(st.lists(st.floats(min_value=-10000.9999999, allow_nan=False, allow_infinity=False), min_size=0, max_size=1000))
def test_recursive_max_float(random_list):

    arr_to_sort = random_list.copy()
    result = recursive_max(arr_to_sort)
    if not random_list:
        assert result == 0
    else:
        assert result == pytest.approx(max(random_list))