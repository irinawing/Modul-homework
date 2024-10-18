import sqlite3

connection = sqlite3.connect('not_telegram.db')
cursor = connection.cursor()

# Удаление id = 6
cursor.execute('DELETE FROM Users WHERE id = 6')

# Количество пользователей
cursor.execute('SELECT COUNT(*) FROM Users')
total_users = cursor.fetchone()[0]

# Сумма балансов и среднее значение
cursor.execute('SELECT SUM(balance) FROM Users')
all_balances = cursor.fetchone()[0]
print(all_balances / total_users)

# Иной вариант подсчета среднего значения

# cursor.execute('SELECT AVG(balance) FROM Users')
# avg_balance=cursor.fetchone()[0]
# print(avg_balance)

connection.commit()
connection.close()