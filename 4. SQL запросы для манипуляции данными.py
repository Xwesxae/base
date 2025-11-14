import sqlite3

conn = sqlite3.connect('database.db')
cursor = conn.cursor()

# Создаем вторую таблицу для сложных запросов
cursor.execute('''
CREATE TABLE IF NOT EXISTS posts (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    title TEXT NOT NULL,
    user_id INTEGER,
    FOREIGN KEY (user_id) REFERENCES users (id)
)
''')

# Добавляем тестовые данные
cursor.execute("INSERT INTO posts (title, user_id) VALUES (?, ?)", ("First post", 1))
cursor.execute("INSERT INTO posts (title, user_id) VALUES (?, ?)", ("Second post", 1))
cursor.execute("INSERT INTO posts (title, user_id) VALUES (?, ?)", ("Third post", 3))
conn.commit()

# Сложные запросы
print("=== ПОЛЬЗОВАТЕЛИ И ИХ ПОСТЫ ===")
cursor.execute('''
    SELECT u.name, COUNT(p.id) as post_count 
    FROM users u 
    LEFT JOIN posts p ON u.id = p.user_id 
    GROUP BY u.id
''')
print("Количество постов по пользователям:", cursor.fetchall())

print("=== ПОИСК ПО ИМЕНИ ===")
cursor.execute("SELECT * FROM users WHERE name LIKE ?", ('%Iv%',))
print("Найдены:", cursor.fetchall())

print("=== СОРТИРОВКА И ЛИМИТ ===")
cursor.execute("SELECT * FROM users ORDER BY id DESC LIMIT 3")
print("Последние 3 пользователя:", cursor.fetchall())

conn.close()
