"""Имеется список студентов группы, в котором все имена различны. Определить, есть ли в
группе студент, который побывал в гостях у всех студентов. (Для каждого студента
составить список из множества побывавших у него в гостях друзей, причем хозяина в этот
список не включать)."""

students_friends = {
    'Алиса': {'Саша', 'Данил'},
    'Саша': {'Алиса', 'Аня'},
    'Данил': {'Алиса', 'Саша'},
    'Давид': {'Саша', 'Аня'},
    'Аня': {'Данил', 'Саша'}
}

guests = {student: set() for student in students_friends}

for student, friends in students_friends.items():
    for friend in friends:
        guests[friend].add(student)

for student, friends in guests.items():
    if friends == set(students_friends.keys()) - {student}:
        print(f"Студент {student} побывал в гостях у всех остальных студентов.")