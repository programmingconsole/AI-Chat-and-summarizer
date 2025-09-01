import sqlite3
from datetime import datetime

DB_NAME = "student_progress.db"

def init_db():
    """Initialize SQLite DB"""
    conn = sqlite3.connect(DB_NAME)
    cur = conn.cursor()
    cur.execute("""
        CREATE TABLE IF NOT EXISTS progress (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            topic TEXT,
            summary TEXT,
            questions TEXT,
            timestamp TEXT
        )
    """)
    conn.commit()
    conn.close()

def save_progress(topic, summary, questions):
    """Save session into DB"""
    conn = sqlite3.connect(DB_NAME)
    cur = conn.cursor()
    cur.execute(
        "INSERT INTO progress (topic, summary, questions, timestamp) VALUES (?, ?, ?, ?)",
        (topic, summary, "|".join(questions), datetime.now().strftime("%Y-%m-%d %H:%M:%S"))
    )
    conn.commit()
    conn.close()

def fetch_history():
    """Fetch all previous records"""
    conn = sqlite3.connect(DB_NAME)
    cur = conn.cursor()
    cur.execute("SELECT topic, summary, questions, timestamp FROM progress")
    rows = cur.fetchall()
    conn.close()
    return rows
