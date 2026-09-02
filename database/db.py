import sqlite3
from config import DATABASE

def get_db_connection():
    conn = sqlite3.connect(DATABASE)
    conn.row_factory= sqlite3.Row
    return conn

def init_db():
    conn = get_db_connection()

    conn.execute('''CREATE TABLE IF NOT EXISTS user(
        id IMTEGER PRIMARY KEY AUTOINCREMENT,
        username TEXT UNIQUE NOT NULL,
        password TEXT NOT NULL
    )''')

    conn.execute('''CREATE TABLE IF NOT EXISTS formularios(
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        user_id INTERGER NOT NULL,
        nome TEXT NOT NULL,
        email TEXT NOT NULL,
        data_nascimento TEXT NOT NULL,
        genero TEXT NOT NULL,
        FOREING KEY (user_id) REFERENCE user(id)
    )''')
    
    conn.commit()
    conn.close()