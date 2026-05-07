import pytest
from .HW_4 import recursive_sum
from hypothesis import given, strategies as st

def test_recursive_sum_incorrect_list():

    with pytest.raises(TypeError):
        recursive_sum("7")

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
    return [1, 2, [3, 4], 5, 6, 7]

@pytest.fixture
def array_7():
    return [211, 19, 18, 17, 16, 15, 14, 13, 12, 11, 10, 9, 8, 7, 6, 5, 4, 3, 17, 27, 53,
            14, 56, 127, 253, 2, 1, 0, 13, 12, 11, 10, 9, 8, 7, 6, 5, 4, 3, 17, 27, 53,
            253, 2, 1, 0, 13, 12, 11, 10, 9, 16, 15, 14, 13, 12, 11, 10, 9, 8, 7, 6, 5, 4,
            3, 17, 27, 53, 12, 11, 10, 9, 16, 15, 14, 13, 12, 8, 7, 6, 5, 4, 3, 17, 27, 53]

# Позитивные тесты:
def test_recursive_sum_pozitive_1(array_1):
    assert recursive_sum(array_1) == 20

def test_recursive_sum_pozitive_2(array_4):
    assert recursive_sum(array_4) == 156

def test_recursive_sum_pozitive_3(array_7):
    assert recursive_sum(array_7) == 1916

def test_recursive_sum_pozitive_4():
    assert recursive_sum([]) == 0

# Негативные тесты:
def test_recursive_sum_negative_1(array_5):

    with pytest.raises(TypeError):
        recursive_sum(array_5)

def test_recursive_sum_negative_2(array_6):

    with pytest.raises(TypeError):
        recursive_sum(array_6)

def test_recursive_sum_negative_3():

    with pytest.raises(TypeError):
        recursive_sum([1, None, 3])

def test_recursive_sum_negative_4():

    with pytest.raises(TypeError):
        recursive_sum(None)

# Пограничные тесты:
def test_recursive_sum_border_1(array_2):
    assert recursive_sum(array_2) == 0

def test_recursive_sum_border_2(array_3):
    assert recursive_sum(array_3) == 28

def test_recursive_sum_border_3():
    assert recursive_sum([1]) == 1

@given(st.lists(st.integers(), min_size=0, max_size=1000))
def test_recursive_sum_int(random_list):
    arr_to_sort = random_list.copy()

    result = recursive_sum(arr_to_sort)
    assert result == sum(random_list)

@given(st.lists(st.floats(allow_nan=False, allow_infinity=False), min_size=0, max_size=550))
def test_recursive_sum_float(random_list):
    arr_to_sort = random_list.copy()

    result = recursive_sum(arr_to_sort)
    assert result == pytest.approx(sum(random_list)) # данная строка, с ИИ. На больших числах тип float
                                        # выдает погрешности. При точном сравнении, они влияют на тест.