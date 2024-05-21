# Дано трёхзначное число. Вывести число, полученное при перестановки второй и третьей цифры исходного числа.

import tkinter as tk


def swap_digits():
    try:
        num = entry.get()
        if not num.isdigit():
            raise ValueError
        elif len(str(num)) == 3:
            num = int(num)
            result.set(str(num // 100) + str(num % 10) + str(num // 10 % 10))
        else:
            result.set('Число должно быть трёхзначным')
    except ValueError:
        result.set('Введите число')


root = tk.Tk()
root.geometry('250x100')
root.title("Перестановка цифр")

# Создание поля ввода
entry = tk.Entry(root)
entry.grid(row=0, column=0)

# Создание кнопки
button = tk.Button(root, text="Свапнуть", command=swap_digits)
button.grid(row=1, column=0)

# Создание поля вывода
result = tk.StringVar()
result_label = tk.Label(root, textvariable=result)
result_label.grid(row=2, column=0)

root.mainloop()
