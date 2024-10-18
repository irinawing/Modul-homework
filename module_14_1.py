import sqlite3

connection = sqlite3.connect('not_telegram.db')

cursor = connection.cursor()
cursor.execute('''
CREATE TABLE IF NOT EXISTS Users (
    id INTEGER PRIMARY KEY,
    username TEXT NOT NULL,
    email TEXT NOT NULL,
    age INTEGER,
    balance INTEGER NOT NULL
)
''')
# Заполнение с 1 до 10
users_data = []
for i in range(1, 11):
    users_data.append((i, f'User{i}', f'example{i}@gmail.com', i * 10, 1000))

cursor.executemany('INSERT INTO Users '
                   '(id, username, email, age, balance) VALUES (?, ?, ?, ?, ?)', users_data)
connection.commit()

# Обновление - 2 этап
cursor.execute('''
UPDATE Users
SET balance = balance - 500
WHERE id % 2 = 1
''')
connection.commit()

# Удаление каждой 3-ей записи, начиная с 1-ой
cursor.execute('''
DELETE FROM Users
WHERE id % 3 = 1
''')
connection.commit()

# выборка всех записей при помощи fetchall(), где возраст не равен 60

cursor.execute('''
SELECT username, email, age, balance
FROM Users
WHERE age != 60
''')

# вывод в указанном формате
rows = cursor.fetchall()
for row in rows:
    print(f'Имя: {row[0]} | Почта: {row[1]} | Возраст: {row[2]} | Баланс: {row[3]}')
connection.close()