"""Имеется список студентов группы, в котором все имена различны. Определить, есть ли в
группе студент, который побывал в гостях у всех студентов. (Для каждого студента
составить список из множества побывавших у него в гостях друзей, причем хозяина в этот
список не включать)."""

students_friends = {
    'Alice': {'Bob', 'Charlie'},
    'Bob': {'Alice', 'David'},
    'Charlie': {'Alice', 'Eve', 'Bob'},
    'David': {'Bob', 'Eve'},
    'Eve': {'Charlie', 'David', 'Bob'}
}

for student in students_friends:
    guests_set = set()
    for friend_list in students_friends.values():
        if student in friend_list:
            guests_set.update(friend_list.difference({student}))
    if guests_set == set(students_friends.keys()).difference({student}):
        print(f"Студент {student} побывал в гостях у всех остальных студентов.")

