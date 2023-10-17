# Вариант 18
# Даны три числа. Найти среднее из них (т.е. число, расположенное между наименьшим и наибольшим)

a = input("Введите число a: ")
b = input("Введите число b: ")
c = input("Введите число c: ")

if a.isdigit() and b.isdigit() and c.isdigit():
    if a > b > c:
        print(b)
    elif b > c > a:
        print(c)
    elif c > a > b:
        print(a)
else:
    print("Не все переменные являются числами!")