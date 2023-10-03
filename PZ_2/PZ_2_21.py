def take_number():
  inp = input("Введите трёхзначное число: ")
  if inp.isdigit() and len(str(inp)) == 2:
    print(str(inp[0] + inp[2] + inp[1]))
  else:
    print("Некорректные вводные данные")
    take_number()

if __name__ == "__main__":
  take_number()

