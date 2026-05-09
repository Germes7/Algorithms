import pytest
from .HW_4 import reverse_string
from hypothesis import given, strategies as st

def test_reverse_string_incorrect_value():

    with pytest.raises(TypeError):
        reverse_string(7)

def test_reverse_string_empty_value():
    assert reverse_string("") == ""

@pytest.fixture
def array_1():
    return "1, 2, 3, 4, 5, 6, 7"

@pytest.fixture
def array_2():
    return 123

@pytest.fixture
def array_3():
    return None

@pytest.fixture
def array_4():
    return []

@pytest.fixture
def array_5():
    return "А роза упала на лапу Азора"

@pytest.fixture
def array_6():
    return "Превед Медвед"

@pytest.fixture
def array_7():
    return ";$123!@#*'"

@pytest.fixture
def array_8():
    return "Пиво!"

@pytest.fixture
def array_9():
    return "А"

@pytest.fixture
def array_10():
    return ("ааааааабббббббвввввввгггггггдддддддеееееееёёёёёёё")

@pytest.fixture
def array_11():
    return "ШалаШ"

# Позитивные тесты:
def test_reverse_string_pozitive_1(array_1):
    assert reverse_string(array_1) == "7 ,6 ,5 ,4 ,3 ,2 ,1"

def test_reverse_string_pozitive_2(array_5):
    assert reverse_string(array_5) == "арозА упал ан алапу азор А"

def test_reverse_string_pozitive_3(array_6):
    assert reverse_string(array_6) == "девдеМ деверП"

def test_reverse_string_pozitive_4(array_7):
    assert reverse_string(array_7) == "'*#@!321$;"

def test_reverse_string_pozitive_5(array_8):
    assert reverse_string(array_8) == "!овиП"

# Негативные тесты:
def test_reverse_string_negative_1(array_2):

    with pytest.raises(TypeError):
        reverse_string(array_2)

def test_reverse_string_negative_2(array_3):

    with pytest.raises(TypeError):
        reverse_string(array_3)

def test_reverse_string_negative_3(array_4):

    with pytest.raises(TypeError):
        reverse_string(array_4)

def test_reverse_string_negative_4():

    with pytest.raises(TypeError):
        reverse_string(bool)

# Пограничные тесты:
def test_reverse_string_border_1(array_9):
    assert reverse_string(array_9) == "А"

def test_reverse_string_border_2(array_10):
    assert reverse_string(array_10) == "ёёёёёёёееееееедддддддгггггггвввввввбббббббааааааа"

def test_reverse_string_border_3(array_11):
    assert reverse_string(array_11) == "ШалаШ"

@given(st.text(max_size=1000))
def test_reverse_string(random_text):

    result = reverse_string(random_text)
    assert result == random_text[::-1]