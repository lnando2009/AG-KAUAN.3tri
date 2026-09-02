import sqlite3
from database.db import get_db_connection

class UserModel:
    @staticmethod
    def find_by_username(username):
        conn = get_db_connection
        user = conn.execute('SELECT * FROM  user WHERE username = ?', (username)).fetchone()
        conn.close()
        return user
    
    @staticmethod
    def creat_user(username, password):
        conn = get_db_connection()
        try:
            conn.execute('INSERT INTO user (username, password) VALUES (?,?)', (username, password))
            conn.comit()
            return True
        except sqlite3.IntegrityError:
            return None
        finally:
            conn.close()

