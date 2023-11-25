# Вариант 18
# Даны три числа. Найти среднее из них (т.е. число, расположенное между наименьшим и наибольшим)

a = input("Введите число a: ")
b = input("Введите число b: ")
c = input("Введите число c: ")
d = input("Введите число d: ")

try:
    a, b, c, d = int(a), int(b), int(c), int(d)
    arr = [a, b, c, d]
    arr.sort()
    print(arr[-2])
except ValueError:
    print("Некорректный ввод")