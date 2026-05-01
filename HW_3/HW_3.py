import time
import sys
sys.set_int_max_str_digits(10000000)
import matplotlib.pyplot as plt
import random


# Задача №1
# Напишите функцию max_in_range(arr, start, end), которая принимает на вход список и два индекса start и end,
# и возвращает максимальный элемент и две координаты (относительную и абсолютную) между start и end включительно.
# Абсолютная координата - отсчитывается от начала всего массива.
# Относительная координата - отсчитывается от начала рассматриваемого диапазона.

def max_in_range(arr: list[int], start: int, end: int) -> tuple[int, int, int]:
    if not isinstance(arr, list): raise TypeError("Нужен массив")
    if not arr: raise ValueError("Массив не должен быть пустым")
    if type(start) is bool: raise TypeError("Требуется число а не булевое значение")
    if not isinstance(start, int): raise TypeError("Нужно целочисленное значение")
    if start >= len(arr) or start < 0: raise ValueError("Индекс Start не может быть большим либо меньшим длины списка")
    if type(end) is bool: raise TypeError("Требуется число а не булевое значение")
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


# Задача №2
# Напишите функцию rotate_and_reverse(arr, k), которая принимает на вход список и число k, и возвращает новый
# список, в котором сначала происходит циклический сдвиг вправо на k позиций, а затем инверсия всего списка.

def rotate_reverse(arr: list[int], k: int) -> list[int]:
    if not isinstance(arr, list): raise TypeError("Нужен массив")
    if not arr: raise ValueError("Массив не должен быть пустым")
    if not isinstance(k, int): raise TypeError("Нужно целочисленное значение")
    if k < 0: raise ValueError("Число должно быть большим либо равным нулю")

    arr_1 = arr.copy()
    k %= len(arr_1)
    lenht = (len(arr_1) - 1)

    for _ in range(k):
        buf = arr_1[lenht]

        for i in range(lenht, 0, -1):
            arr_1[i] = arr_1[i - 1]
        arr_1[0] = buf

    for i in range(len(arr_1) // 2):
        arr_1[i], arr_1[lenht - i] = arr_1[lenht - i], arr_1[i]

    return arr_1


# O(n) = 1 + 1 + 1 + 1 + 1 + 1 + (n*k) + 1 + 1 + 1 + 1 + 1 = 11 + (n*k) => O(n**2)

if __name__ == "__main__":

    n_values = [10, 100, 1000, 5000, 10000]
    start = 3
    end = 8
    times = []

    for n in n_values:
        test_arr = [random.randint(0, 1000) for _ in range(n)]
        start_time = time.perf_counter()
        rotate_reverse(test_arr, n // 10)
        end_time = time.perf_counter()

        times.append(end_time - start_time)

    plt.figure(figsize=(10, 6))
    plt.plot(n_values, times, marker='o', linestyle='-', color='b')

    plt.title('Сложность сдвига и реверса')
    plt.xlabel('Количество элементов (n)')
    plt.ylabel('Время выполнения (секунды)')
    plt.grid(True)
    plt.show()


# Задача №3
# Напишите функцию reverse_even_elements(arr), которая принимает на вход список и возвращает новый список,
# в котором только четные числа идут в обратном порядке, а нечетные остаются на своих местах.

def revers_even_elements(arr: list[int]) -> list[int]:
    if not isinstance(arr, list): raise TypeError("Нужен массив")
    if not arr: raise ValueError("Массив не должен быть пустым")

    arr_1 = arr.copy()
    lenght_arr_1 = len(arr_1)
    arr_even = []

    for i in range(lenght_arr_1):
        if arr_1[i] % 2 == 0:
            arr_even.append(arr_1[i])

    lenht_arr_even = len(arr_even) - 1
    for i in range(len(arr_even) // 2):
        arr_even[i], arr_even[lenht_arr_even - i] = arr_even[lenht_arr_even - i], arr_even[i]

    i_count = 0
    for i in range(lenght_arr_1):

        if arr_1[i] % 2 == 0:
            arr_1[i] = arr_even[i_count]
            i_count += 1

    return arr_1


#  O(n) = 1 + 1 + 1 + 1 + 1 + (2n) + 1 + 1 + (2n / 2) + 1 +1 + 1 + 1 + 1 + (2n) = 2n + n + 2n => O(n)

# if __name__ == "__main__":

    n_values = [10, 100, 1000, 5000, 10000, 100000, 500000, 1000000, 10000000]
    times = []

    for n in n_values:
        test_arr = [random.randint(0, 1000) for _ in range(n)]
        start_time = time.perf_counter()
        revers_even_elements(test_arr)
        end_time = time.perf_counter()

        times.append(end_time - start_time)

    plt.figure(figsize=(10, 6))
    plt.plot(n_values, times, marker='o', linestyle='-', color='b')

    plt.title('Сложность реверса от четных чисел')
    plt.xlabel('Количество элементов (n)')
    plt.ylabel('Время выполнения (секунды)')
    plt.grid(True)
    plt.show()

# Задача №4
# Вам дано большое целое число, представленное в виде целочисленного массива digits, где каждая цифра
# digits[i] — это i-я цифра этого числа. Цифры упорядочены слева направо от старшей значимости к младшей.
# Большое целое число не содержит старших нулей.
# Увеличьте большое целое число на единицу и верните результирующий массив digits.
# Пример:
# Input: array = [1, 2, 3, 6]
# Output: [1, 2, 3, 7]

def plus_one(arr: list[int]) -> list[int]:
    if not isinstance(arr, list): raise TypeError("Нужен массив")
    if not arr: raise ValueError("Массив не должен быть пустым")

    str_arr = ""
    for i in range(len(arr)):
        str_arr += str(arr[i])

    int_arr = int(str_arr) + 1

    arr_result = []
    while int_arr > 0:

        i = int_arr % 10
        arr_result.append(i)
        int_arr //= 10

    arr_result.reverse()  # Не стал расписывать через цикл реверс
    return arr_result


# O(n) = 1 + 1 + (2n) + 1 + 1 + 1 + (2n +1 + 1 + 1) + 2n = 5 + 2n + 5n + 2n => O(n)

if __name__ == "__main__":

    n_values = [10, 100, 1000, 5000, 10000, 100000]
    times = []

    for n in n_values:
        test_arr = [random.randint(0, 9) for _ in range(n)]
        test_arr[0] = random.randint(1, 9)
        start_time = time.perf_counter()
        plus_one(test_arr)
        end_time = time.perf_counter()
        times.append(end_time - start_time)

    plt.figure(figsize=(10, 6))
    plt.plot(n_values, times, marker='o', linestyle='-', color='b')

    plt.title('Зависимость времени выполнения функции от количества цифр')
    plt.xlabel('Количество элементов (n)')
    plt.ylabel('Время выполнения (секунды)')
    plt.grid(True)
    plt.show()