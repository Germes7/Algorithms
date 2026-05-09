import pytest
from .HW_4 import is_palindrome
from hypothesis import given, strategies as st


def test_is_palindrome_incorrect_value():

    with pytest.raises(TypeError):
        is_palindrome(7)

def test_is_palindrome_return_value_1():
    assert is_palindrome("") == True

def test_is_palindrome_return_value_2():
    assert is_palindrome("2") == True

@pytest.fixture
def string_1():
    return "АрозаупаланалапуазорА"

@pytest.fixture
def string_2():
    return "ШалаШ"

@pytest.fixture
def string_3():
    return "**!**"

@pytest.fixture
def string_4():
    return 123

@pytest.fixture
def string_5():
    return None

@pytest.fixture
def string_6():
    return []

@pytest.fixture
def string_7():
    return "Шалаш"

@pytest.fixture
def string_8():
    return "А роза упала на лапу Азора"

@pytest.fixture
def string_9():
    return "АА"

@pytest.fixture
def string_10():
    return "АБ"

# Позитивные тесты:
def test_is_palindrome_pozitive_1(string_1):
    assert is_palindrome(string_1) == True

def test_is_palindrome_pozitive_2(string_2):
    assert is_palindrome(string_2) == True

def test_is_palindrome_pozitive_3(string_3):
    assert is_palindrome(string_3) == True

# Негативные тесты:
def test_is_palindrome_negative_1(string_4):

    with pytest.raises(TypeError):
        is_palindrome(string_4)

def test_is_palindrome_negative_2(string_5):

    with pytest.raises(TypeError):
        is_palindrome(string_5)

def test_is_palindrome_negative_3(string_6):

    with pytest.raises(TypeError):
        is_palindrome(string_6)

def test_is_palindrome_negative_4(string_7):
        assert is_palindrome(string_7) == False

def test_is_palindrome_negative_5(string_8):
        assert is_palindrome(string_8) == False

# Пограничные тесты:
def test_is_palindrome_border_1(string_9):
    assert is_palindrome(string_9) == True

def test_is_palindrome_border_2(string_10):
    assert is_palindrome(string_10) == False

def test_is_palindrome_border_3():
    assert is_palindrome("AoA") == True

@given(st.text(max_size=1000))
def test_reverse_string(random_text):

    result = is_palindrome(random_text)
    pre_result = (random_text == random_text[::-1])
    assert result == pre_result