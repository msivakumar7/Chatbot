
import os
from flask import Flask, request, jsonify, render_template
import sqlite3

app = Flask(__name__)

def init_db():
    conn = sqlite3.connect("chat.db")
    cur = conn.cursor()

    cur.execute("""
    CREATE TABLE IF NOT EXISTS knowledge (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        question TEXT UNIQUE,
        answer TEXT
    )
    """)

    data = [
        ("hello", "Hello! 👋 How can I help you today?"),
        ("hi", "Hi there! 😊"),
        ("your name", "I am an AI chatbot built using Flask."),
        ("python", "Python is a powerful programming language."),
        ("ai", "Artificial Intelligence simulates human intelligence."),
        ("database", "A database stores and organizes data efficiently."),
        ("bye", "Goodbye! Have a great day! 👋")
    ]

    for q, a in data:
        cur.execute("INSERT OR IGNORE INTO knowledge (question, answer) VALUES (?, ?)", (q, a))

    conn.commit()
    conn.close()

init_db()

def get_answer(user_msg):
    conn = sqlite3.connect("chat.db")
    cur = conn.cursor()

    cur.execute("SELECT answer FROM knowledge WHERE question LIKE ?", 
                ('%' + user_msg.lower() + '%',))
    result = cur.fetchone()

    conn.close()

    if result:
        return result[0]
    else:
        return "Sorry, I don't understand that yet."

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/chat", methods=["POST"])
def chat():
    user_msg = request.json["message"]
    reply = get_answer(user_msg)
    return jsonify({"reply": reply})

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 10000))
    app.run(host="0.0.0.0", port=port)
