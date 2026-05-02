
import sqlite3

def connect():
    return sqlite3.connect("library.db")

def create_tables():
    conn = connect()
    cursor = conn.cursor()

    cursor.execute('''
    CREATE TABLE IF NOT EXISTS books (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        title TEXT,
        author TEXT,
        available INTEGER DEFAULT 1
    )
    ''')

    conn.commit()
    conn.close()
