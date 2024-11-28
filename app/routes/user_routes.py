from flask import Blueprint, request
from app.services.user_service import UserService

user_bp = Blueprint('user_bp', __name__)

@user_bp.route('/users', methods=['POST'])
def create_user():
    data = request.get_json()
    user = UserService.create_user(data['username'], data['password'], data['rol_id'])
    if user:
        return {'message': 'Usuario creado exitosamente'}
    else:
        raise Exception('Error al crear el usuario')

# @user_bp.route('/users/<int:user_id>', methods=['PUT'])
# def update_user(user_id):
#     data = request.get_json()
#     user = UserService.update_user(user_id, data)
#     if user:
#         return {'message': 'Usuario actualizado exitosamente'}
#     else:
#         raise Exception('Error al actualizar el usuario')
    
@user_bp.route('/users/<int:user_id>', methods=['PUT'])
def update_user(user_id):
    data = request.get_json()
    rol = UserService.update_user(user_id, data)

    if isinstance(rol, tuple) and isinstance(rol[0], dict) and 'error' in rol[0]:
        raise Exception('Error al actualizar el usuario')
    
    return {'message': 'Usuario actualizado exitosamente'}

@user_bp.route('/users', methods=['GET'])
def list_users():
    users = UserService.get_all_users()
    if not users:
        return {'message': 'No hay usuarios disponibles'}, 404

    users_list = [{ 'nombre': user.name, 'usuario': user.username, 'estado': user.is_active} for user in users]
    return users_list

