# Необходимо разработать алгоритм, который принимает на вход список целых
# чисел и возвращает сумму всех четных чисел в этом списке. Если сумма
# отрицательная, вернуть 1.

# Выходные данные:
# Одно целое неотрицательное число, которое является суммой всех четных чисел в списке.
# Формат: одно число типа int.

# Входные данные:
# Список целых чисел, каждое число в диапазоне от -2 * 10**4 до 2 * 10**4.
# Формат: последовательность целых чисел типа list.

# def sum_even_numbers(arr: list[int]) -> int:
#
#     if not arr:
#         return 0
#
#     if not isinstance(arr, list): raise TypeError("Нужен массив целых чисел")
#
#     sum_even = 0
#     for i in arr:
#         if not isinstance(i, int): raise TypeError("Числа должны быть натуральными")
#
#         if i % 2 == 0:
#             sum_even += i
#
#     if sum_even < 0:
#         return 1
#
#     return sum_even


# Разработайте алгоритм, который определяет наиболее часто встречающийся
# элемент в предложенном списке чисел. Если таких элементов несколько, верните наименьший из них.

# Выходные данные: Одно целое число, представляющий наиболее часто встречающийся элемент в списке.
# Формат: число типа int.

# Входные данные:
# Список целых чисел, каждое число в диапазоне от 1 до 2*104.
# Формат: последовательность целых чисел типа list.

def repeating_number(arr: list[int]) -> int:

    if not arr:
        return 0

    if not isinstance(arr, list): raise TypeError("Нужен массив целых чисел")

    arr.sort()
    repeat_elem = arr[0]
    count = 1
    prim_count = 0

    for i in range(len(arr) - 1):
        if arr[i] == arr[i + 1]:
            count += 1

        else:
            if count > prim_count:
                prim_count = count
                repeat_elem = arr[i]
            count = 1

    if count > prim_count:
        repeat_elem = arr[-1]

    return repeat_elem


arr = [1, 5, 2, 2, 1, 5, 0, 3, 1, 4, 5, -7, 2, 5]
print(repeating_number(arr))
# sort = [-7, 0, 1, 1, 1, 2, 2, 2, 3, 4, 5, 5, 5, 5]
# count = 4
# prim_count = 3
# repeat_elem = 5
