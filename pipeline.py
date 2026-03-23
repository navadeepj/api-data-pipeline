import requests
import sqlite3

# EXTRACT

url = "https://jsonplaceholder.typicode.com/posts"
response = requests.get(url)
data = response.json()

print("Data fetched successfully")

# TRANSFORM

cleaned_data = []

for item in data:
    cleaned_data.append((
        item['id'],
        item['title'].strip(),
        item['body'].strip()
    ))

print("Data cleaned")

# LOAD

conn = sqlite3.connect("data.db")
cursor = conn.cursor()

cursor.execute("""
CREATE TABLE IF NOT EXISTS posts (
    id INTEGER,
    title TEXT,
    body TEXT
)
""")

cursor.executemany("INSERT INTO posts VALUES (?, ?, ?)", cleaned_data)

conn.commit()
conn.close()

print("Data stored in database")
