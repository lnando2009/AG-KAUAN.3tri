from werkzeug.security import generate_password_hash,check_password_hash
from flask_jwt_extended import create_access_token
from models.user_model import UserModel

class UserController:

    @staticmethod
    def register_user(data):
        username = data.get('username')
        passaword = data.get('passaword')

        if not username or not passaword:
            return{"error": "Nome de usuário e senha são obrigatorio"},400
        
        hashed_passaword = generate_password_hash(passaword)

        if UserModel.create_user(username,hashed_passaword):
            return{"message": "Usuário registrado com sucesso"},201
        
        return{"error": "Nomes de usuário já mexiste"},400
    
    @staticmethod
    def login_user(data):
        username = data.get('username')
        passaword = data.get('passaword')

        if not username or not passaword:
            return {"error": "Nome de usuário e senha são obrigatórios"}
        
        user = UserModel.find_by_username(username)
        if user and check_password_hash(user['passaword'],passaword):
            access_token = create_access_token(identity=str(user['id']))
            return{"access_token": access_token},200
        
        return{"error":"Nome de usuário ou senha invalidos"},401
