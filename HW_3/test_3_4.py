from .HW_3 import plus_one
import pytest

@pytest.fixture
def check_array_1():
    return [1, 2, 4]

@pytest.fixture
def check_array_2():
    return [1, 2, 4, 0]

@pytest.fixture
def check_array_3():
    return [1, 2, 4, 9]

@pytest.fixture
def check_array_4():
    return [1, 0, 0]

@pytest.fixture
def check_array_5():
    return [9, 9, 9, 9]

@pytest.fixture
def check_array_6():
    return [6]

@pytest.fixture
def check_array_7():
    return [1, 2, 9, 9]

@pytest.fixture
def check_array_8():
    return [9]

@pytest.fixture
def check_array_9():
    return [9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9,
            9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9]

@pytest.fixture
def check_array_negative_prima_zero():
    return [0, 2, 4]

@pytest.fixture
def check_array_negative_more_than_nine():
    return [2, 12, 14]

@pytest.fixture
def check_array_negative_element_sub_zero():
    return [-2, 12, 14]

def test_plus_one_incorrect_list():

    with pytest.raises(TypeError):
        plus_one("7")

def test_plus_one_not_arr():

    with pytest.raises(ValueError):
        plus_one([])

# Позитивные тесты:
def test_plus_one_pozitive_1(check_array_1):
    assert plus_one(check_array_1) == [1, 2, 5]

def test_plus_one_pozitive_2(check_array_2):
    assert plus_one(check_array_2) == [1, 2, 4, 1]

def test_plus_one_pozitive_3(check_array_3):
    assert plus_one(check_array_3) == [1, 2, 5, 0]

def test_plus_one_pozitive_4(check_array_4):
    assert plus_one(check_array_4) == [1, 0, 1]

def test_plus_one_pozitive_5(check_array_5):
    assert plus_one(check_array_5) == [1, 0, 0, 0, 0]

def test_plus_one_pozitive_6(check_array_6):
    assert plus_one(check_array_6) == [7]

def test_plus_one_pozitive_7(check_array_7):
    assert plus_one(check_array_7) == [1, 3, 0, 0]

# Негативные тесты:
def test_plus_one_negative_prima_zero(check_array_negative_prima_zero):

    with pytest.raises(ValueError):
        plus_one(check_array_negative_prima_zero)

def test_plus_one_negative_more_than_nine(check_array_negative_more_than_nine):

    with pytest.raises(ValueError):
        plus_one(check_array_negative_more_than_nine)

def test_plus_one_negative_sub_zero(check_array_negative_element_sub_zero):

    with pytest.raises(ValueError):
        plus_one(check_array_negative_element_sub_zero)

def test_plus_one_negative_element_bool():

    with pytest.raises(TypeError):
        plus_one([1, 2, 3, True, 5])

def test_plus_one_negative_element_float():

    with pytest.raises(TypeError):
        plus_one([1, 2, 1.5, 7])

# Пограничные тесты:
def test_plus_one_border_1(check_array_8):
    assert plus_one(check_array_8) == [1, 0]

def test_plus_one_border_2(check_array_9):
    assert plus_one(check_array_9) == [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
                                       0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]