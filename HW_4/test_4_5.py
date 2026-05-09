import pytest
from .HW_4 import recursive_sum_even
from hypothesis import given, strategies as st

def test_recursive_sum_even_incorrect_list():

    with pytest.raises(TypeError):
        recursive_sum_even("7")

def test_recursive_sum_even_empty_list():
    assert recursive_sum_even([]) == 0

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
    return [8, 8, 8, 8]

@pytest.fixture
def array_5():
    return [33, "18", 21]

@pytest.fixture
def array_6():
    return [-1.0, -2.0, -4.0, -5.0, -6.0]

@pytest.fixture
def array_7():
    return [1.0, 2.0, 4.0, 5.0, 6.0]

@pytest.fixture
def array_8():
    return [1.1, 2.1, 4.1, 5.1, 6.1]

@pytest.fixture
def array_9():
    return [20, 19, 18, 17, 16, 15, 14, 13, 12, 11, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1, 0]

@pytest.fixture
def array_10():
    return [211, 19, 18, 17, 16, 15, 14, 13, 12, 11, 10, 9, 8, 7, 6, 5, 4, 3, 17, 27, 53,
            14, 56, 127, 253, 2, 1, 0, 13, 12, 11, 10, 9, 8, 7, 6, 5, 4, 3, 17, 27, 53,
            253, 2, 1, 0, 13, 12, 11, 10, 9, 16, 15, 14, 13, 12, 11, 10, 9, 8, 7, 6, 5, 4,
            3, 17, 27, 53, 12, 11, 10, 9, 16, 15, 14, 13, 12, 8, 7, 6, 5, 4, 3, 17, 27, 53]

@pytest.fixture
def array_11():
    return [-500, 1, 2, 500]

@pytest.fixture
def array_12():
    return [1]

# Позитивные тесты:
def test_recursive_sum_even_pozitive_1(array_1):
    assert recursive_sum_even(array_1) == 4

def test_recursive_sum_even_pozitive_2(array_6):
    assert recursive_sum_even(array_6) == -12.0

def test_recursive_sum_even_pozitive_3(array_7):
    assert recursive_sum_even(array_7) == 12.0

def test_recursive_sum_even_pozitive_4(array_9):
    assert recursive_sum_even(array_9) == 110

def test_recursive_sum_even_pozitive_5():
    assert recursive_sum_even([14]) == 14

# Негативные тесты:
def test_recursive_sum_even_negative_1(array_5):

    with pytest.raises(TypeError):
        recursive_sum_even(array_5)

def test_recursive_sum_even_negative_2():

    with pytest.raises(TypeError):
        recursive_sum_even([1, 5, None, 3, 7])

def test_recursive_sum_even_negative_3():

    with pytest.raises(TypeError):
        recursive_sum_even(None)

def test_recursive_sum_even_negative_4(array_8):
    assert recursive_sum_even(array_8) == 0.0

def test_recursive_sum_even_negative_5(array_12):
    assert recursive_sum_even(array_12) == 0

def test_recursive_sum_even_negative_6():
    assert recursive_sum_even([1.1, 2, 4.3, -5.5, 6, -8.0]) == 0.0

# Пограничные тесты:
def test_recursive_sum_even_border_1(array_2):
    assert recursive_sum_even(array_2) == 0

def test_recursive_sum_even_border_2(array_3):
    assert recursive_sum_even(array_3) == 0

def test_recursive_sum_even_border_3(array_4):
    assert recursive_sum_even(array_4) == 32

def test_recursive_sum_even_border_4(array_10):
    assert recursive_sum_even(array_10) == 376

def test_recursive_sum_even_border_5(array_11):
    assert recursive_sum_even(array_11) == 2

@given(st.lists(st.integers(min_value=-1000000), min_size=0, max_size=1000))
def test_sum_even_int(random_list):

    arr_to_test = random_list.copy()
    result = recursive_sum_even(arr_to_test)
    expected_sum = sum(x for x in random_list if x % 2 == 0)

    assert result == expected_sum

@given(st.lists(st.floats(min_value=-1000, allow_nan=False, allow_infinity=False), min_size=0, max_size=1000))
def test_sum_even_float(random_list):

    arr_to_test = random_list.copy()
    result = recursive_sum_even(arr_to_test)
    expected_sum = sum(x for x in random_list if x % 2 == 0)

    if not random_list:
        assert result == 0
    else:
        assert result == pytest.approx(expected_sum)