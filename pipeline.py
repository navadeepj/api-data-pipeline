import requests
import sqlite3

def extract_data(url):
    try:
        response = requests.get(url)
        response.raise_for_status()
        print("Data fetched successfully")
        return response.json()
    except Exception as e:
        print("Error fetching data:", e)
        return []

def transform_data(data):
    cleaned = []
    for item in data:
        try:
            cleaned.append((
                item.get('id'),
                item.get('title', '').strip(),
                item.get('body', '').strip()
            ))
        except Exception as e:
            print("Error processing item:", e)
    print("Data transformed")
    return cleaned

def load_data(cleaned):
    conn = sqlite3.connect("data.db")
    cursor = conn.cursor()

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS posts (
        id INTEGER,
        title TEXT,
        body TEXT
    )
    """)

    cursor.executemany("INSERT INTO posts VALUES (?, ?, ?)", cleaned)

    conn.commit()
    conn.close()
    print("Data loaded into database")

def main():
    url = "https://jsonplaceholder.typicode.com/posts"
    data = extract_data(url)
    cleaned = transform_data(data)
    load_data(cleaned)

if __name__ == "__main__":
    main()
