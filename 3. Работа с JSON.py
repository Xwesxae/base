import sqlite3
import json

conn = sqlite3.connect('database.db')
cursor = conn.cursor()

# Создаем тестовый JSON файл
data = [
    {"name": "Dmitry", "email": "dmitry@mail.ru"},
    {"name": "Olga", "email": "olga@mail.ru"}
]
with open('data.json', 'w') as file:
    json.dump(data, file, indent=2)

# Импорт из JSON
with open('data.json', 'r') as file:
    data = json.load(file)
    for item in data:
        cursor.execute("INSERT INTO users (name, email) VALUES (?, ?)", 
                      (item['name'], item['email']))
conn.commit()

# Экспорт в JSON
cursor.execute("SELECT * FROM users")
columns = [desc[0] for desc in cursor.description]
result = [dict(zip(columns, row)) for row in cursor.fetchall()]

with open('export.json', 'w') as file:
    json.dump(result, file, indent=2)

print("JSON операции завершены")
conn.close()
