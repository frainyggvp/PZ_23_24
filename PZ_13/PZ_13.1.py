# В матрице элементы кратные 3 увеличить в 3 раза
import random

rows, cols = 3, 3
matrix = [[random.randint(-9, 9) for i in range(rows)] for i in range(cols)]
print(f"Матрица: {matrix}")


def third(m):
    for r in range(rows):
        for c in range(cols):
            if m[r][c] % 3 == 0:
                yield [r, c]


third_ids = (list(third(matrix)))
for id in third_ids:
    matrix[id[0]][id[1]] *= 3

print("Изменённая матрица:", matrix)