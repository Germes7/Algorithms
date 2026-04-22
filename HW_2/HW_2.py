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


# Задача № 2
# Напишите функцию fibonacci(n), которая принимает одно целое число n и возвращает список чисел Фибоначчи
# от 0 до n-го числа (включительно).
# Функция должна обрабатывать все допустимые значения n (n ≥ 0).
# Вход: Целое число n (n ≥ 0)
# Выход: Список чисел Фибоначчи от 0 до n-го числа (включительно)
# Оцените временную сложность алгоритма в лучшем, среднем и худшем случаях.
# Напишите модульные тесты для проверки корректности функции в стратегиях: позитивные тесты, негативные и граничные.
import time
import matplotlib.pyplot as plt

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