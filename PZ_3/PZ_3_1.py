# Вариант 18
# Дано целое положительное число. Проверить истинность высказывания: "Данное число является нечетным трёхзначным"

integer = input("Введите целое положительное число: ")

if not integer.isdigit():
    print("Не число или число не положительное! False")
elif len(integer) != 3:
    print("Не трёхзначное число! False")
elif int(integer) % 2 == 0:
    print("Число чётное! False")
else:
    print("True")