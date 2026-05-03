import time
import sys
sys.set_int_max_str_digits(10000000)
import matplotlib.pyplot as plt
import random
from typing import Any

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