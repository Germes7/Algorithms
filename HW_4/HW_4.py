import time
import sys
sys.set_int_max_str_digits(10000000)
import matplotlib.pyplot as plt
import random
from typing import Any
sys.setrecursionlimit(10000)

# Задача №1. Сортировка “Пузырька”
# Напишите функцию, которая принимает на вход массив элементов, анонимную функцию key (задает ключ сортировки)
# и анонимную функцию order_by (задает признак сортировки). Результатом функции должен быть отсортированный
# массив элементов по методу сортировки “Пузырька”. Если переданный на вход массив пустой, выдать []

def bubble_sort(arr: list[Any], key=lambda x: x, order_by=lambda x, y: x > y) -> list[Any]:
    if not isinstance(arr, list): raise TypeError("Нужен массив")
    if not arr: return []

    lenth = len(arr)
    for i in range(lenth):

        for j in range(0, lenth - i - 1):
            if order_by(key(arr[j]), key(arr[j +1])):
                arr[j], arr[j + 1] = arr[j + 1], arr[j]

    return arr


# O(n) = 1 + 1 + 2 + 1 + (2n**2) => O(n2)

if __name__ == "__main__":

    n_values = [10, 100, 1000, 2000, 2500, 5000]
    times = []

    for n in n_values:
        test_arr = [random.randint(0, 1000) for _ in range(n)]
        start_time = time.perf_counter()
        bubble_sort(test_arr)
        end_time = time.perf_counter()

        times.append(end_time - start_time)

    plt.figure(figsize=(10, 6))
    plt.plot(n_values, times, marker='o', linestyle='-', color='b')

    plt.title('Тест сортировки методом "Пузырька')
    plt.xlabel('Количество элементов (n)')
    plt.ylabel('Время выполнения (секунды)')
    plt.grid(True)
    plt.show()


# Задача №2. Сортировка выбором + подсчет операций.
# Напишите функцию, реализующую сортировку методом “Выбора” (простых перестановок), но модифицируйте её так,
# чтобы подсчитывать количество операций сравнения и обмена элементов, и возвращать эти значения вместе
# с отсортированным массивом.

def choice_sort(arr: list[int], key=lambda x: x, order_by=lambda x, y: x < y) -> tuple[list[int], int, int]:
    if not isinstance(arr, list): raise TypeError("Нужен массив")
    if not arr: raise ValueError("Массив не должен быть пустым")

    lenth = len(arr)
    count_comparison = 0
    count_exchange = 0
    for i in range(lenth - 1):
        i_min = i

        for j in range(i + 1, lenth):
            count_comparison += 1

            if order_by(key(arr[j]), key(arr[i_min])):
                i_min = j

        if i_min != i:
            arr[i], arr[i_min] = arr[i_min], arr[i]
        count_exchange += 1

    return (arr, count_comparison, count_exchange)


# O(n) = 1 + 1 + 1 + 1 + 1 + 1 + 1 + (n2 - 1) + 1 + (n2 + 1) + 1 + 1 + 1 + 1 + 1 => O(n2)

if __name__ == "__main__":

    n_values = [10, 100, 1000, 2000, 2500, 5000]
    times = []

    for n in n_values:
        test_arr = [random.randint(0, 1000) for _ in range(n)]
        start_time = time.perf_counter()
        choice_sort(test_arr)
        end_time = time.perf_counter()

        times.append(end_time - start_time)

    plt.figure(figsize=(10, 6))
    plt.plot(n_values, times, marker='o', linestyle='-', color='b')

    plt.title('Тест сортировки методом "Выбора"')
    plt.xlabel('Количество элементов (n)')
    plt.ylabel('Время выполнения (секунды)')
    plt.grid(True)
    plt.show()


# Задача №3.
# Напишите функцию recursive_sum, которая принимает на вход массив элементов и возвращает сумму
# всех элементов массива. Если переданный на вход массив пустой, функции должны возвращать 0.
# Используйте рекурсивный подход.

def recursive_sum(arr: list[int | float]) -> int | float:
    if not isinstance(arr, list): raise TypeError("Нужен список")
    if not arr: return 0

    sum = arr[0]
    del arr[0]
    return sum + recursive_sum(arr)


# O(n) = 1 + 1 + 1 + (n2) => O(n2)

if __name__ == "__main__":

    n_values = [10, 50, 100, 200, 400, 500, 1000, 2000, 4000, 7000, 9000]
    times = []

    for n in n_values:
        test_arr = [random.randint(0, 1000) for _ in range(n)]
        start_time = time.perf_counter()
        recursive_sum(test_arr)
        end_time = time.perf_counter()

        times.append(end_time - start_time)

    plt.figure(figsize=(10, 6))
    plt.plot(n_values, times, marker='o', linestyle='-', color='b')

    plt.title('Тест функции sum с рекурсией')
    plt.xlabel('Количество элементов (n)')
    plt.ylabel('Время выполнения (секунды)')
    plt.grid(True)
    plt.show()