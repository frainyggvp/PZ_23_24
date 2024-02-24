# В матрице найти среднее арифметическое элементов последних двух столбцов.
import random
from functools import reduce

rows, cols = 3, 3
matrix = [[random.randint(-5, 5) for i in range(rows)] for i in range(cols)]
print(f"Матрица: {matrix}")


def average(m, r, c):
    for j in range(r):
        for k in range(c-2, c):
            yield m[j][k]


average_list = list(average(matrix, rows, cols))
print("Значения последних двух столбцов:", average_list)
print("Среднее арифметическое:", reduce(lambda x, y: x + y, average_list) / len(average_list))



