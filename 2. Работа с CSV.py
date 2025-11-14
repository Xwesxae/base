import sqlite3
import csv

conn = sqlite3.connect('database.db')
cursor = conn.cursor()

# Создаем тестовый CSV файл
with open('data.csv', 'w', newline='') as file:
    writer = csv.writer(file)
    writer.writerow(['Anna', 'anna@mail.ru'])
    writer.writerow(['Sergey', 'sergey@mail.ru'])

# Импорт из CSV
with open('data.csv', 'r') as file:
    reader = csv.reader(file)
    for row in reader:
        cursor.execute("INSERT INTO users (name, email) VALUES (?, ?)", row)
conn.commit()

# Экспорт в CSV
cursor.execute("SELECT * FROM users")
with open('export.csv', 'w', newline='') as file:
    writer = csv.writer(file)
    writer.writerows(cursor.fetchall())

print("CSV операции завершены")
conn.close()
