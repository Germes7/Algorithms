from .HW_3 import max_in_range
import pytest

def test_max_in_range_incorrect_list():

    with pytest.raises(TypeError):
        max_in_range("5")

def test_max_in_range_not_arr():

    with pytest.raises(ValueError):
        max_in_range([], 1, 9)

@pytest.fixture
def check_array_1():
    return [1, -5, 7, 10, 12, 27, 5]

@pytest.fixture
def check_array_2():
    return [1, 3, 5, 8, 0, 7, 12, 3, -1, 6, 11]

@pytest.fixture
def check_array_3():
    return [11, 5, 0, 7, 4]

@pytest.fixture
def check_array_4():
    return [1, 5, 0, 7, 4, 9]

@pytest.fixture
def check_array_5():
    return [2, 2, 2, 2, 2]

@pytest.fixture
def check_array_6():
    return [-11, -15, -20, -17, -24, -9]

def test_max_in_range_start_float(check_array_1):

    with pytest.raises(TypeError):
        max_in_range(check_array_1, 1.5, 2)

def test_max_in_range_start_exceeds_length_arr(check_array_1):

    with pytest.raises(ValueError):
        max_in_range(check_array_1, 8, 12)

def test_max_in_range_start_sub_zero(check_array_1):

    with pytest.raises(ValueError):
        max_in_range(check_array_1, -7, 3)

def test_max_in_range_end_float(check_array_1):

    with pytest.raises(TypeError):
        max_in_range(check_array_1, 1, 2.5)

def test_max_in_range_end_exceeds_length_arr(check_array_1):

    with pytest.raises(ValueError):
        max_in_range(check_array_1, 2, 8)

def test_max_in_range_end_less_start(check_array_1):

    with pytest.raises(ValueError):
        max_in_range(check_array_1, 5, 3)

# Позитивные тесты:
def test_max_in_range_pozitive_1(check_array_2):
    assert max_in_range(check_array_2, 2, 7) == (12, 4, 6)

def test_max_in_range_pozitive_2(check_array_2):
    assert max_in_range(check_array_2, 0, 2) == (5, 2, 2)

def test_max_in_range_pozitive_3(check_array_2):
    assert max_in_range(check_array_2, 7, 10) == (11, 3, 10)

# Негативные тесты:
def test_max_in_range_negative_1(check_array_1):

    with pytest.raises(TypeError):
        max_in_range(check_array_1, None, 5)

def test_max_in_range_negative_2(check_array_1):

    with pytest.raises(TypeError):
        max_in_range(check_array_1, 3, True)

def test_max_in_range_negative_start_bool(check_array_1):

    with pytest.raises(TypeError):
        max_in_range(check_array_1, True, 3)

def test_max_in_range_negative_end_bool(check_array_1):

    with pytest.raises(TypeError):
        max_in_range(check_array_1, 2, False)

# Пограничные тесты:
def test_max_in_range_border_1(check_array_1):
    assert max_in_range(check_array_1, 1, 1) == (-5, 0, 1)

def test_max_in_range_border_2(check_array_1):
    assert max_in_range(check_array_1, 0, 6) == (27, 5, 5)

def test_max_in_range_border_3(check_array_3):
    assert max_in_range(check_array_3, 0, 4) == (11, 0, 0)

def test_max_in_range_border_4(check_array_4):
    assert max_in_range(check_array_4, 0, 5) == (9, 5, 5)

def test_max_in_range_border_5(check_array_5):
    assert max_in_range(check_array_5, 1, 3) == (2, 0, 1)

def test_max_in_range_border_6(check_array_6):
    assert  max_in_range(check_array_6, 1, 3) == (-15, 0, 1)