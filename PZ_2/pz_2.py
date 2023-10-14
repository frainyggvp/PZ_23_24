def take_number():
  inp = input("Введите трёхзначное число: ")
  if inp.isdigit() and len(str(inp)) == 3 and int(inp) > 99:
    inp = int(inp)
    print(str(inp//100) + str(inp%10) + str(inp//10%10))
  else:
    print("Некорректные вводные данные")
    take_number()

if __name__ == "__main__":
  take_number()
