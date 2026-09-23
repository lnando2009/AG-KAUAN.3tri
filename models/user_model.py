import sqlite3
from database.db import get_db_connection

class UserModel:

    @staticmethod
    def find_by_username(username):
        conn = get_db_connection()
        user = conn.execute('SELECT * FROM users WHERE username = ?', (username,)).fetchone()
        conn.close()
        return user

    @staticmethod
    def create_user(username, password):
        conn = get_db_connection()
        try:
            conn.execute('INSERT INTO users (username, password) VALUES (?, ?)', (username, password))
            conn.commit()
            return True
        except sqlite3.IntegrityError:
            return None
        finally:
            conn.close()

    @staticmethod
    def find_by_id(user_id):
        conn = get_db_connection()
        user = conn.execute('SELECT * FROM users WHERE id = ?', (user_id,)).fetchone()
        conn.close()
        return user

    @staticmethod
    def update_user(user_id, username=None, password=None):
        conn = get_db_connection()
        try:
            if username is not None and password is not None:
                conn.execute('UPDATE users SET username = ?, password = ? WHERE id = ?',
                             (username, password, user_id))
            elif username is not None:
                conn.execute('UPDATE users SET username = ? WHERE id = ?', (username, user_id))
            elif password is not None:
                conn.execute('UPDATE users SET password = ? WHERE id = ?', (password, user_id))
            conn.commit()
            return True
        except sqlite3.IntegrityError:
            return None
        finally:
            conn.close()

    @staticmethod
    def delete_user(user_id):
        conn = get_db_connection()
        cursor = conn.execute('DELETE FROM users WHERE id = ?', (user_id,))
        conn.commit()
        deleted = cursor.rowcount > 0
        conn.close()
        return deleted
