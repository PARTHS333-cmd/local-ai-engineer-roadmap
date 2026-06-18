import sqlite3

DB_NAME = "assistant.db"

def initialize_database():

    conn = sqlite3.connect(DB_NAME)

    cursor = conn.cursor()

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS messages (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        role TEXT,
        content TEXT
    )
    """)

    conn.commit()
    conn.close()

def add_message(role, content):

    conn = sqlite3.connect(DB_NAME)

    cursor = conn.cursor()

    cursor.execute(
        "INSERT INTO messages(role, content) VALUES (?, ?)",
        (role, content)
    )

    conn.commit()
    conn.close()

def get_history():

    conn = sqlite3.connect(DB_NAME)

    cursor = conn.cursor()

    cursor.execute(
        "SELECT role, content FROM messages"
    )

    rows = cursor.fetchall()

    conn.close()

    return [
        {
            "role": row[0],
            "content": row[1]
        }
        for row in rows
    ]

# Run only when this file is executed directly
if __name__ == "__main__":

    initialize_database()

    print("Database created successfully.")