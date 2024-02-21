# Составить генератор (yield), который преобразует все буквенные символы в строчные.
def gen(ar):
    n = [el.lower() for el in ar]
    yield n


array = ["А", "Б", "В"]
new_array = gen(array)

for i in new_array:
    print(i)
