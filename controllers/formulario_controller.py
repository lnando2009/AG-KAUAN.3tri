from models.formulario_model import FormularioModel


class FormularioController:

    @staticmethod
    def create_formulario(user_id, data):
        nome = data.get('nome')
        email = data.get('email')
        data_nascimento = data.get('data_nascimento')
        cpf = data.get('cpf')
        genero = data.get('genero')

        if not nome or not email or not data_nascimento or not cpf or not genero:
            return {"error": "Todos os campos são obrigatórios"}, 400

        formulario = FormularioModel.create_formulario(
            user_id, nome, email, data_nascimento, cpf, genero
        )
        if formulario:
            return {"message": "Formulário criado com sucesso"}, 201
        return {"error": "Erro ao criar formulário"}, 500

    @staticmethod
    def get_formulario(formulario_id):
        formulario = FormularioModel.find_by_id(formulario_id)
        if not formulario:
            return {"error": "Formulário não encontrado"}, 404

        return formulario, 200

    @staticmethod
    def update_formulario(formulario_id, data):
        formulario = FormularioModel.find_by_id(formulario_id)
        if not formulario:
            return {"error": "Formulário não encontrado"}, 404

        if not data:
            return {"error": "Nenhum dado enviado"}, 400

        nome = data.get('nome')
        email = data.get('email')
        data_nascimento = data.get('data_nascimento')
        cpf = data.get('cpf')
        genero = data.get('genero')

        FormularioModel.update_formulario(formulario_id, nome, email, data_nascimento, cpf, genero)
        return {"message": "Formulário atualizado com sucesso"}, 200

    @staticmethod
    def delete_formulario(formulario_id):
        formulario = FormularioModel.find_by_id(formulario_id)
        if not formulario:
            return {"error": "Formulário não encontrado"}, 404

        FormularioModel.delete_formulario(formulario_id)
        return {"message": "Formulário excluído com sucesso"}, 200
