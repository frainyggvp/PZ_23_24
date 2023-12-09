"""Дана строка. Преобразовать в ней все строчные буквы (как латинские, так и русские)
в прописные, а прописные — в строчные."""

string = "ABC abc Python 61"
new_string = ""

for i in string:
    new_string += i.swapcase()

print("Строка без изменений:", string)
print("Строка изменённая:", new_string)
