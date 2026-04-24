import time
import matplotlib.pyplot as plt

# Задача №1
# Напишите функцию factorial(n), которая принимает одно целое число n и возвращает факториал этого числа.
# Функция должна обрабатывать все допустимые значения n (неотрицательные целые числа).
# Входные данные: Целое число n 0 ≤ n ≤ 20
# Выходные данные: Целое число, равное n!
# Ограничение на время: 5 сек.
#  Оцените временную сложность алгоритма в лучшем, среднем и худшем случаях.
#  Напишите модульные тесты для проверки корректности функции в стратегиях: позитивные тесты, негативные и граничные.

def factorial(n: int) -> int:

    if not isinstance(n, int): raise TypeError("Требуется целое число")
    if n < 0: raise ValueError("Число должно быть большим либо равным нулю")

    if n == 0:
        return 1

    mult = 1
    for i in range(1, n + 1):
        mult *= i

    return mult

if __name__ == "__main__":

    n_values = [1, 5, 10, 20, 50, 100, 150, 200, 300, 500]
    times = []

    for n in n_values:
        start_time = time.perf_counter()
        factorial(n)
        end_time = time.perf_counter()

        times.append(end_time - start_time)

    plt.figure(figsize=(10, 6))
    plt.plot(n_values, times, marker='o', linestyle='-', color='b')

    plt.title('Зависимость времени выполнения от n (Факториал числа)')
    plt.xlabel('Значение n')
    plt.ylabel('Время выполнения (секунды)')
    plt.grid(True)
    plt.show()

# Задача №2
# Напишите функцию fibonacci(n), которая принимает одно целое число n и возвращает список чисел Фибоначчи
# от 0 до n-го числа (включительно).
# Функция должна обрабатывать все допустимые значения n (n ≥ 0).
# Вход: Целое число n (n ≥ 0)
# Выход: Список чисел Фибоначчи от 0 до n-го числа (включительно)
# Оцените временную сложность алгоритма в лучшем, среднем и худшем случаях.
# Напишите модульные тесты для проверки корректности функции в стратегиях: позитивные тесты, негативные и граничные.

def fibonacci(n: int) -> list[int]:

    if not isinstance(n, int): raise TypeError("Число должно быть целым")
    if n < 0: raise ValueError("Число должно быть больше -1")

    if n == 0: return [0]
    if n == 1: return [0, 1]

    fib_arr = [0, 1]
    for i in range(2, n + 1):
        fib = (fib_arr[i - 1]) + (fib_arr[i - 2])
        fib_arr.append(fib)

    return fib_arr

if __name__ == "__main__":

    n_values = [1, 10, 100, 500, 1000, 2000, 5000, 10000, 100000]
    times = []

    for n in n_values:
        start_time = time.perf_counter()
        fibonacci(n)
        end_time = time.perf_counter()

        times.append(end_time - start_time)

    plt.figure(figsize=(10, 6))
    plt.plot(n_values, times, marker='o', linestyle='-', color='b')

    plt.title('Зависимость времени выполнения от n (Фибоначчи)')
    plt.xlabel('Значение n')
    plt.ylabel('Время выполнения (секунды)')
    plt.grid(True)
    plt.show()


# Задача №3
# Напишите функцию count_ones(n), которая принимает одно целое число n в десятичном представлении и возвращает
# количество единиц в его двоичном представлении. Функция должна обрабатывать все допустимые значения n (n ≥ 0).
# Вход: Целое число n (n ≥ 0)
# Выход: Целое число, равное количеству единиц в двоичном представлении n
# 1. Оцените временную сложность алгоритма в лучшем, среднем и худшем случаях.
# 2. Напишите модульные тесты для проверки корректности функции в стратегиях: позитивные тесты, негативные и граничные.

def count_ones(n: int) -> int:

    if n == '': raise ValueError("Требуется число")
    if not isinstance(n, int): raise TypeError("Требуется целое число")
    if n < 0: raise ValueError("Число должно быть >= 0")

    bit_numbers = format(n, "b")

    count = 0
    for iter in bit_numbers:
        if iter == "1":
            count += 1

    return count

if __name__ == "__main__":

    n_values = [10, 1000, 10000, 100000, 1000000, 100000000, 100000000]
    times = []

    for n in n_values:
        start_time = time.perf_counter()
        count_ones(n)
        end_time = time.perf_counter()

        times.append(end_time - start_time)

    plt.figure(figsize=(10, 6))
    plt.plot(n_values, times, marker='o', linestyle='-', color='b')

    plt.title('Зависимость времени выполнения от n (Двоичное представление числа)')
    plt.xlabel('Значение n')
    plt.ylabel('Время выполнения (секунды)')
    plt.grid(True)
    plt.show()


# Задача №4
# Дано целое число x. Верните true, если x является палиндромом, и false в противном случае.
# Пример 1:
# Input: x = 121
# Output: true
# Пример 2:
# Input: x = -121
# Output: false
# Пример 3
# Input: x = 10
# Output: false
# Пояснение: Читается как 01 справа налево. Следовательно, это не палиндром.
# Constraints:
# -2^31 <= x <= 2^31 - 1

def palindrome_num(num: int) -> bool:

    if not isinstance(num, int): raise TypeError("Требуется нат. число")
    if num == "": raise TypeError("Требуется число")

    if num < 0:
        return False

    num_str = str(num)
    lengt = len(num_str)

    for i in range(len(num_str) // 2):
        if num_str[i] != num_str[lengt- 1 - i]:
            return False

    return True

if __name__ == "__main__":

    n_values = [101, 1010101, 10101010101, 10101010101010101010101, 10101010101010101010101010101010101010101010101,
                10101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101]
    times = []

    for num in n_values:
        start_time = time.perf_counter()
        palindrome_num(num)
        end_time = time.perf_counter()

        times.append(end_time - start_time)

    plt.figure(figsize=(10, 6))
    plt.plot(n_values, times, marker='o', linestyle='-', color='b')

    plt.title('Зависимость времени выполнения от n (Палиндром числа)')
    plt.xlabel('Значение n')
    plt.ylabel('Время выполнения (секунды)')
    plt.grid(True)
    plt.show()