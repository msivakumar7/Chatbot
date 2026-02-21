import sqlite3

conn = sqlite3.connect("chat.db")
cur = conn.cursor()

cur.execute("""
CREATE TABLE IF NOT EXISTS knowledge (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    question TEXT,
    answer TEXT
)
""")

data = [
    ("hello", "Hello! 👋 How can I help you today?"),
    ("hi", "Hi there! 😊"),
    ("your name", "I am an AI chatbot created using Flask."),
    ("python", "Python is a powerful programming language used for web, AI, and automation."),
    ("ai", "Artificial Intelligence means machines that simulate human intelligence."),
    ("database", "A database stores and organizes data efficiently."),
    ("bye", "Goodbye! Have a great day! 👋")
]

cur.executemany("INSERT INTO knowledge (question, answer) VALUES (?,?)", data)

conn.commit()
conn.close()

print("Database updated successfully!")
