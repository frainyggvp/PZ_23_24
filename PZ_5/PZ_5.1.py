# Составить программу, в которой функция генерирует четырехзначное число и определяет, есть ли в числе одинаковые цифры

import random

def random_four():
    random_digit = str(random.randint(1000, 10000))
    journal = []
    print(random_digit)

    for digit in random_digit:
        counter = 0
        for i in random_digit:
            if digit == i:
                counter += 1
        if counter > 1 and digit not in journal:
            journal.append(digit)
            print(digit)

random_four()
