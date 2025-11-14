import sqlite3

conn = sqlite3.connect('database.db')
cursor = conn.cursor()

# Создание таблицы
cursor.execute('''
CREATE TABLE IF NOT EXISTS users (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL,
    email TEXT UNIQUE
)
''')
conn.commit()

# CREATE
cursor.execute("INSERT INTO users (name, email) VALUES (?, ?)", ("Ivan", "ivan@mail.ru"))
cursor.execute("INSERT INTO users (name, email) VALUES (?, ?)", ("Maria", "maria@mail.ru"))
conn.commit()

# READ
cursor.execute("SELECT * FROM users")
print("Все пользователи:", cursor.fetchall())

# UPDATE
cursor.execute("UPDATE users SET email = ? WHERE name = ?", ("new@mail.ru", "Ivan"))
conn.commit()

# DELETE
cursor.execute("DELETE FROM users WHERE name = ?", ("Maria",))
conn.commit()

cursor.execute("SELECT * FROM users")
print("После удаления:", cursor.fetchall())

conn.close()
