# Дано вещественное число X и целое число N (>0). Найти значение выражения 1 + X + X^2/2! + ... + X^N/N!
# (N! = 1 * 2 * ... * N). Полученное число является приближенным значением функции exp в точке X

import math

try:
    x = float(input("Введите x:"))
    n = int(input("Введите n:"))
    if not n > 0:
        print("N не больше нуля")
    else:
        result = 0
        fact = 1
        for i in range(0, n + 1):
            if not i == 0:
                fact *= i
            result += x ** i / fact

        print(f"Приближённое значение: {result}, точное значение: {math.exp(x)}")
except ValueError:
    print("Введены некоректные данные")
