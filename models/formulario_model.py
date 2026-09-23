import sqlite3
from database.db import get_db_connection

class FormularioModel:

    @staticmethod
    def create_formulario(user_id, nome, email, data_nascimento, cpf, genero):
        conn = get_db_connection()
        try:
            conn.execute('''INSERT INTO formularios (user_id, nome, email, data_nascimento, cpf, genero)
                            VALUES (?, ?, ?, ?, ?, ?)''',
                        (user_id, nome, email, data_nascimento, cpf, genero))
            conn.commit()
            return True
        except sqlite3.IntegrityError:
            return None
        finally:
            conn.close()

    @staticmethod
    def find_by_id(formulario_id):
        conn = get_db_connection()
        formulario = conn.execute('SELECT * FROM formularios WHERE id = ?', (formulario_id,)).fetchone()
        conn.close()
        return dict(formulario) if formulario else None

    @staticmethod
    def update_formulario(formulario_id, nome=None, email=None, data_nascimento=None, cpf=None, genero=None):
        conn = get_db_connection()
        try:
            campos = []
            valores = []

            if nome is not None:
                campos.append('nome = ?')
                valores.append(nome)
            if email is not None:
                campos.append('email = ?')
                valores.append(email)
            if data_nascimento is not None:
                campos.append('data_nascimento = ?')
                valores.append(data_nascimento)
            if cpf is not None:
                campos.append('cpf = ?')
                valores.append(cpf)
            if genero is not None:
                campos.append('genero = ?')
                valores.append(genero)

            if not campos:
                return False

            valores.append(formulario_id)
            conn.execute(f'UPDATE formularios SET {", ".join(campos)} WHERE id = ?', valores)
            conn.commit()
            return True
        finally:
            conn.close()

    @staticmethod
    def delete_formulario(formulario_id):
        conn = get_db_connection()
        cursor = conn.execute('DELETE FROM formularios WHERE id = ?', (formulario_id,))
        conn.commit()
        deleted = cursor.rowcount > 0
        conn.close()
        return deleted
