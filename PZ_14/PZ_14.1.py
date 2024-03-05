# Из исходного текстового файла (expansion.txt) выбрать имена файлов, соответствующие типам:
# .xls, .xml, .html, .css, .py . Посчитать количество полученных элементов
import re

pattern = r'([^\s]+\.(xls|xml|html|css|py))'
with open("expansion.txt", "r", encoding="utf-8") as file:
    matches = re.findall(pattern, file.read())

for match in matches:
    print(match[0])

# Подсчет количества найденных элементов
print("Общее количество файлов: ", len(matches))
