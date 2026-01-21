from flask import Blueprint, jsonify, request
from app.service.user_service import UserService

user_controller = Blueprint('user_controller', __name__, url_prefix='/api')

@user_controller.route('/users', methods=['POST'])
def create_user():
    user = UserService.create_user(request.get_json(force=True))
    return jsonify({'message': 'Usuario creado correctamente', 'user': user.to_dict()}), 201

@user_controller.route('/users/<int:user_id>', methods=['GET'])
def get_user(user_id):
    user = UserService.get_user_by_id(user_id)
    return jsonify({'message': 'Usuario obtenido correctamente', 'user': user.to_dict()}), 200

@user_controller.route('/users', methods=['GET'])
def get_all_users():
    users = UserService.get_all_users()
    return jsonify({'message': 'Usuarios obtenidos correctamente', 'users': [user.to_dict() for user in users]}), 200

@user_controller.route('/users/<int:user_id>', methods=['PUT'])
def update_user(user_id):
    user = UserService.update_user(user_id, request.get_json(force=True))
    return jsonify({'message': 'Usuario actualizado correctamente', 'user': user.to_dict()}), 200

@user_controller.route('/users/<int:user_id>', methods=['DELETE'])
def delete_user(user_id):
    UserService.delete_user(user_id)
    return jsonify({'message': 'Usuario eliminado correctamente'}), 200