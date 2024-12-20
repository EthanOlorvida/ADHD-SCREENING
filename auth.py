import sqlite3

def connect_db():
    return sqlite3.connect('users.db')

def login(username, password):
    conn = connect_db()
    cursor = conn.cursor()
    cursor.execute("SELECT password FROM users WHERE username = ?", (username,))
    result = cursor.fetchone()
    conn.close()
    if result and result[0] == password:
        return True
    return False

def sign_up(username, password, firstname, lastname, age):
    conn = connect_db()
    cursor = conn.cursor()  
    
    cursor.execute("SELECT 1 FROM users WHERE username = ?", (username,))
    if cursor.fetchone():
        conn.close()
        return False
    
    cursor.execute("INSERT INTO users (username, password, firstname, lastname, age) VALUES (?, ?, ?, ?, ?)", (username, password, firstname, lastname, age))
    conn.commit()
    conn.close()
    return True

def save_quiz(username, responses):
    conn = connect_db()
    cursor = conn.cursor()
    cursor.execute("UPDATE users SET quiz_responses = ? WHERE username = ?", (responses, username))
    conn.commit()
    conn.close()

def create_table():
    conn = connect_db()
    cursor = conn.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS users (
            username TEXT PRIMARY KEY,
            password TEXT,
            firstname TEXT,
            lastname TEXT,
            age INTEGER,
            quiz_responses TEXT
        )
    ''')
    conn.commit()
    conn.close()
