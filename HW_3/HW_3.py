import time
import matplotlib.pyplot as plt
import random

# Задача №1
# Напишите функцию max_in_range(arr, start, end), которая принимает на вход список и два индекса start и end,
# и возвращает максимальный элемент и две координаты (относительную и абсолютную) между start и end включительно.
# Абсолютная координата - отсчитывается от начала всего массива.
# Относительная координата - отсчитывается от начала рассматриваемого диапазона.

def max_in_range(arr: list[int], start: int, end: int) ->tuple[int, int, int]:

    if not isinstance(arr, list): raise TypeError("Нужен массив")
    if not isinstance(start, int): raise TypeError("Нужно целочисленное значение")
    if start >= len(arr) or start < 0: raise ValueError("Индекс Start не может быть большим либо меньшим длины списка")
    if not isinstance(end, int): raise TypeError("Нужно целочисленное значение")
    if end >= len(arr) or end < start: raise ValueError("Индекс End не может быть большим либо меньшим длины списка\n"
                                                        "либо меньше Start")

    average = arr[start:end + 1]
    max = average[0]
    i_max = 0
    for i in range(1, len(average)):
        if average[i] > max:
            max = average[i]
            i_max = i

    coord = start + i_max

    return (max, i_max, coord)

#  O(n) = (1+1+1+1) + 1 + 1 + n(1+1+1+1+1+1+1+1) + 1 + 1 + 1 => O(n) + 2 + O(n) + 3 = O(2n) + 5 = O(n)

if __name__ == "__main__":

    n_values = [10, 100, 1000, 5000, 10000, 50000, 100000, 1000000]
    start = 3
    end = 8
    times = []

    for n in n_values:

        test_arr = [random.randint(0, 1000) for _ in range(n)]
        start_time = time.perf_counter()
        max_in_range(test_arr, 0, n - 1)
        end_time = time.perf_counter()

        times.append(end_time - start_time)

    plt.figure(figsize=(10, 6))
    plt.plot(n_values, times, marker='o', linestyle='-', color='b')

    plt.title('Зависимость времени поиска максимума от размера диапазона')
    plt.xlabel('Количество элементов (n)')
    plt.ylabel('Время выполнения (секунды)')
    plt.grid(True)
    plt.show()