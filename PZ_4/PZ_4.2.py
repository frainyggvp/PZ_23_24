# Даны целые положительные числа A и B (A<B). Вывести все целые числа от А до В включительно;
# при этом каждое число должно выводиться столько раз, каково его значение (например 3 выводится 3 раза)

a = input("A:")
b = input("B:")

try:
    a, b = int(a), int(b)
    if not a<b:
        print("A должно быть меньше B")
    else:
        for i in range(a, b+1):
            for j in range(i, i*2):
                print(i)

except ValueError:
    print("Вы ввели не числа")
