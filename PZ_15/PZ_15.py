import sqlite3

data = [(1, '2023-12-10', 50000, 'car', 3, 'Rostov'),
        (2, '2023-12-11', 11889, 'life', 5, 'Moskow'),
        (3, '2023-12-11', 100, 'house', 8, 'St.Petersburg'),
        (4, '2024-02-26', 85000, 'house', 8, 'Krasnodar'),
        (5, '2024-03-08', 110, 'car', 3, 'Rostov'),
        (6, '2024-03-15', 50, 'car', 3, 'Moskow'),
        (7, '2024-03-27', 14000, 'life', 5, 'Moskow'),
        (8, '2024-04-02', 56500, 'house', 8, 'Luhansk'),
        (9, '2024-04-03', 27290, 'house', 8, 'Krasnodar'),
        (9, '2024-04-03', 27290, 'house', 8, 'Krasnodar'),
        (10, '2024-04-07', 10, 'car', 3, 'Los-Angeles')]

with sqlite3.connect('company.db') as con:
    cur = con.cursor()
    cur.execute("""CREATE TABLE IF NOT EXISTS contract (
                    contract_id INTEGER PRIMARY KEY AUTOINCREMENT,
                    contract_date TEXT,
                    sum INTEGER,
                    type TEXT,
                    rate INTEGER,
                    branch TEXT )""")

with sqlite3.connect('company.db') as con:
    cur = con.cursor()
    cur.executemany("""INSERT OR REPLACE INTO contract values(?, ?, ?, ?, ?, ?)""", data)

# with sqlite3.connect('company.db') as con:
#     cur = con.cursor()
#     cur.execute("""SELECT * FROM contract""")
#     print(cur.fetchall())
# with sqlite3.connect('company.db') as con:
#     cur = con.cursor()
#     cur.execute("""SELECT * FROM contract WHERE type=='car'""")
#     print(cur.fetchall())
# with sqlite3.connect('company.db') as con:
#     cur = con.cursor()
#     cur.execute("""SELECT * FROM contract WHERE rate>4""")
#     # print(cur.fetchall())


# with sqlite3.connect('company.db') as con:
#     cur = con.cursor()
#     cur.execute("""DELETE FROM contract WHERE sum < 5000""")
#     cur.execute("""SELECT * FROM contract""")
#     print(cur.fetchall())
# with sqlite3.connect('company.db') as con:
#     cur = con.cursor()
#     cur.execute("""DELETE FROM contract WHERE branch LIKE 'K%'""")
#     cur.execute("""SELECT * FROM contract""")
#     print(cur.fetchall())
# with sqlite3.connect('company.db') as con:
#     cur = con.cursor()
#     cur.execute("""DELETE FROM contract WHERE type=='life'""")
#     cur.execute("""SELECT * FROM contract""")
#     print(cur.fetchall())


with sqlite3.connect('company.db') as con:
    cur = con.cursor()
    cur.execute("""UPDATE contract SET sum=911 WHERE type=='car'""")
    cur.execute("""SELECT * FROM contract""")
    print(cur.fetchall())
with sqlite3.connect('company.db') as con:
    cur = con.cursor()
    cur.execute("""UPDATE contract SET contract_date='2024-04-24' WHERE rate > 5""")
    cur.execute("""SELECT * FROM contract""")
    print(cur.fetchall())
with sqlite3.connect('company.db') as con:
    cur = con.cursor()
    cur.execute("""UPDATE contract SET branch='Derbent' WHERE type=='life'""")
    cur.execute("""SELECT * FROM contract""")
    print(cur.fetchall())