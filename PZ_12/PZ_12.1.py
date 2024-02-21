# В последовательности на n целых элементов найти произведение элементов средней трети.
from functools import reduce
elements = [3, 12, 43, 11, 2, 4, 12, 0, 3]

print("Исходный массив:", elements, "\nПроизведение средней трети:", reduce(lambda x, y: x*y, elements[3:6]))
