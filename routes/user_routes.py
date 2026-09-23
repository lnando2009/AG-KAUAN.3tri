from flask import Blueprint, request, jsonify
from flask_jwt_extended import jwt_required
from controllers.user_controller import UserController

user_bp = Blueprint('users', __name__)


@user_bp.route('/register', methods=['POST'])
def register():
    data, status = UserController.register_user(request.get_json(silent=True) or {})
    return jsonify(data), status


@user_bp.route('/login', methods=['POST'])
def login():
    data, status = UserController.login_user(request.get_json(silent=True) or {})
    return jsonify(data), status


@user_bp.route('/<int:user_id>', methods=['GET'])
@jwt_required()
def get_user(user_id):
    data, status = UserController.get_user(user_id)
    return jsonify(data), status


@user_bp.route('/<int:user_id>', methods=['PUT'])
@jwt_required()
def update_user(user_id):
    data, status = UserController.update_user(user_id, request.get_json(silent=True) or {})
    return jsonify(data), status


@user_bp.route('/<int:user_id>', methods=['DELETE'])
@jwt_required()
def delete_user(user_id):
    data, status = UserController.delete_user(user_id)
    return jsonify(data), status
