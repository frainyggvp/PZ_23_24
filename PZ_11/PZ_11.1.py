"""Средствами языка Python сформировать текстовый файл (.txt), содержащий
последовательность из целых положительных и отрицательных чисел. Сформировать
новый текстовый файл (.txt) следующего вида, предварительно выполнив требуемую
обработку элементов:
Исходные данные:
Количество элементов:
Среднее арифметическое элементов:
Последовательность, в которой каждый последующий элемент равен квадрату суммы двух
соседних элементов:"""

integers = [2, 36, 4, 124, -8, 64, 0, 12]
average = sum(integers) / len(integers)

# последовательность
sequence = []
for i in range(len(integers) - 2):
    if integers[i] == (integers[i-1] + integers[i+1])**2:
        sequence.append(integers[i-1:i+2])


file = open("1.txt", "w", encoding="utf-8")
file.write(str(integers))
file.close()

file = open("2.txt", "w", encoding="utf-8")
file.write(f"Исходные данные: {integers}\nКоличество элементов: {len(integers)}\nСреднее арифметическое элементов: {average}\n")
file.write(f"Последовательность, в которой каждый последующий элемент равен квадрату суммы двух соседних элементов: {sequence}")
file.close()