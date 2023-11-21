import math

def custom_exm(x, n):
    result = 0
    fact = 1
    for i in range(0, n + 1):
        if not i == 0:
            fact *= i
        result += x**i / fact
    return result

try:
    x = int(input("Введите x:"))
    n = int(input("Введите n:"))
    print(f"Приближённое значение: {custom_exm(x, n)}, точное значение: {math.exp(x)}")
except ValueError:
    print("Введены некоректные данные")