from .HW_2 import palindrome_num
import pytest

def test_palindrome_num_incorrect_type_empty_str():

    with pytest.raises(TypeError):
        palindrome_num("")

def test_incorrect_type_empty_float():

    with pytest.raises(TypeError):
        palindrome_num(1.7)

# Позитивные тесты:
def test_input_value_zero():
    assert palindrome_num(0) == True

def test_input_value_pozitive1():
    assert palindrome_num(12121) == True

def test_input_value_pozitive2():
    assert palindrome_num(12122) == False

# Негативные тесты:
def test_input_value_sub_zero1():
    assert palindrome_num(-2) == False

def test_input_value_sub_zero2():
    assert palindrome_num(-202) == False

# Пограничные тесты:
def test_palindrome_input_border_value1():
    assert palindrome_num(11) == True

def test_palindrome_input_border_value2():
    assert palindrome_num(10101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101) == True