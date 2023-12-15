"""Дан список размера N, все элементы которого, кроме первого, упорядочены по
возрастанию. Сделать список упорядоченным, переместив первый элемент на новую
позицию."""

A = [11, 4, 14, 23, 45, 56, 101, 200]
print(A)
A.sort()
print(A)

maximum = A[0]
minimum = A[0]

for i in range(len(A)):
    if A[i] > maximum:
        maximum = A[i]

for i in range(len(A)):
    if A[i] < minimum:
        minimum = A[i]

print(f"Min: {minimum}, Max: {maximum}")