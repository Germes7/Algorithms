from .HW_3 import rotate_reverse
import pytest

@pytest.fixture
def check_array_1():
    return [1, 2, 3, 4, 5]

@pytest.fixture
def check_array_2():
    return [3, 3, 3, 3, 3]

@pytest.fixture
def check_array_3():
    return [1, 2, 3]

def test_rotate_reverse_incorrect_list():

    with pytest.raises(TypeError):
        rotate_reverse("7", 3)

def test_rotate_reverse_not_arr():

    with pytest.raises(ValueError):
        rotate_reverse([], 2)

def test_rotate_reverse_k_is_bool(check_array_1):

    with pytest.raises(TypeError):
        rotate_reverse(check_array_1, True)

def test_rotate_reverse_incorrect_k(check_array_1):

    with pytest.raises(TypeError):
        rotate_reverse(check_array_1, 1.5)

def test_rotate_reverse_k_sub_zero(check_array_1):

    with pytest.raises(ValueError):
        rotate_reverse(check_array_1, -2)

# Позитивные тесты:
def test_rotate_reverse_pozitive_1(check_array_3):
    assert rotate_reverse(check_array_3, 2) == [1, 3, 2]

def test_rotate_reverse_pozitive_2(check_array_1):
    assert rotate_reverse(check_array_1, 3) == [2, 1, 5, 4, 3]

# Негативные тесты:
def test_rotate_reverse_is_new_object(check_array_1): # честно, скоммуниздил у ИИ
    original = check_array_1.copy()
    result = rotate_reverse(check_array_1, 2)
    assert check_array_1 == original
    assert result is not check_array_1

# Пограничные тесты:
def test_rotate_reverse_border_1(check_array_1):
    assert rotate_reverse(check_array_1, 1) == [4, 3, 2, 1, 5]

def test_rotate_reverse_border_2(check_array_2):
    assert rotate_reverse(check_array_2, 3) == [3, 3, 3, 3, 3]

def test_rotate_reverse_border_3(check_array_1):
    assert rotate_reverse(check_array_1, 5) == [5, 4, 3, 2, 1]

def test_rotate_reverse_border_4(check_array_1):
    assert rotate_reverse(check_array_1, 0) == [5, 4, 3, 2, 1]