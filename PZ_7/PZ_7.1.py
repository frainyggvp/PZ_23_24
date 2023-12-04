"""Дана строка. Преобразовать в ней все строчные буквы (как латинские, так и русские)
в прописные, а прописные — в строчные."""

string = "ABC abc Python 61"
new_string = ""

for i in string:
    if i.islower():
        new_string += i.upper()
    elif i.isupper():
        new_string += i.lower()
    else:
        new_string += i

print("Строка без изменений:", string)
print("Строка изменённая:", new_string)
