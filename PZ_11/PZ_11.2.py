"""Из предложенного текстового файла (text18-18.txt) вывести на экран его содержимое,
количество знаков пунктуации в первых четырёх строках. Сформировать новый файл, в
который поместить текст в стихотворной форме выведя строки в обратном порядке."""

with open("text18-18.txt", "r", encoding="utf-16") as file:
    content = file.read()
with open("text18-18.txt", "r", encoding="utf-16") as file:
    lines = file.readlines()
signs = 0
for i in range(4):
    for k in lines[i]:
        if k == "." or k == "," or k == "…":
            signs += 1
print(content, "\nКол-во знаков пунктуации в первых 4 строках:", signs)
with open("3.txt", "w", encoding="utf-8") as file:
    for l in reversed(lines):
        file.write(l)
