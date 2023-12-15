"""Дана строка, состоящая из русских слов, разделенных пробелами (одним или
несколькими). Вывести строку, содержащую эти же слова, разделенные одним
пробелом и расположенные в обратном порядке."""

string = "Выйду я в  поле с  конём"
strings = string.split(' ')

for i in strings:
    if i == '':
        strings.remove(i)

strings = strings[::-1]
string_join = ''.join(strings)
result = ""
for i in strings:
    result += i + ' '

print(f"Обычная строка: {string}\nИзменённая строка: {result}")
