# Задача №1
# Необходимо разработать алгоритм, который принимает на вход список целых
# чисел и возвращает сумму всех четных чисел в этом списке. Если сумма
# отрицательная, вернуть 1.


# Выходные данные:
# Одно целое неотрицательное число, которое является суммой всех четных чисел в списке.
# Формат: одно число типа int.

# Входные данные:
# Список целых чисел, каждое число в диапазоне от -2 * 10**4 до 2 * 10**4.
# Формат: последовательность целых чисел типа list.

def sum_even_numbers(arr: list[int]) -> int:

    if not isinstance(arr, list): raise TypeError("Нужен массив целых чисел")

    if not arr:
        return 0

    sum_even = 0
    for i in arr:
        if not isinstance(i, int): raise TypeError("Числа должны быть натуральными")

        if i % 2 == 0:
            sum_even += i

    if sum_even < 0:
        return 1

    return sum_even


# Задача №2
# Разработайте алгоритм, который определяет наиболее часто встречающийся
# элемент в предложенном списке чисел. Если таких элементов несколько, верните наименьший из них.

# Выходные данные: Одно целое число, представляющий наиболее часто встречающийся элемент в списке.
# Формат: число типа int.

# Входные данные:
# Список целых чисел, каждое число в диапазоне от 1 до 2*10**4.
# Формат: последовательность целых чисел типа list.

def repeating_number(arr: list[int]) -> int:

    if not isinstance(arr, list): raise TypeError("Нужен массив целых чисел")

    if not arr:
        return 0

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


# Задача №3
# Дан массив целых чисел nums и целое число target.
# Верните индексы этих двух чисел так, чтобы их сумма равнялась target.
# Предположим, что для каждого входного значения существует ровно одно решение, и нельзя использовать
# один и тот же элемент дважды. Ответ можно возвращать в любом порядке.

# Пример №1
# Входные данные: nums = [2,7,11,15], target = 9
# Выходные данные: [0, 1]
# Пояснение: Поскольку nums[0] + nums[1] == 9, мы возвращаем [0, 1]

# Пример №2
# Входные данные: nums = [3, 2, 4], target = 6
# Выходные данные: [1, 2]

def output_iter(sequence: list[int], target: int)-> list[int]:

    if not isinstance(sequence, list): raise TypeError("Нужен массив целых чисел")

    if not isinstance(target, int): raise TypeError("Нужно целое число")

    if not sequence:
        return 0

    lengts = len(sequence)

    for i in range(lengts):
        for j in range(i + 1, lengts):
            if sequence[i] + sequence[j] == target:
                return [i, j]

    return []
