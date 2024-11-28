from flask import Blueprint, request
from app.services.role_service import RoleService

role_bp = Blueprint('role_bp', __name__)
@role_bp.route('/roles', methods=['POST'])
def create_role():
    data = request.get_json()
    if not data or not data.get('name') or not data.get('description'):
        raise Exception('Faltan datos para crear el rol')

    role = RoleService.create_role(data['name'], data['description'])
    if role:
        return {'message': 'Rol creado exitosamente'}
    else:
        raise Exception('Error al crear el rol')
    

@role_bp.route('/roles/<int:rol_id>', methods=['PUT'])
def update_role(rol_id):
    data = request.get_json()
    rol = RoleService.update_role(rol_id, data)

    if isinstance(rol, tuple) and isinstance(rol[0], dict) and 'error' in rol[0]:
        raise Exception('Error al actualizar el rol')
    
    return {'message': 'Rol actualizado exitosamente'}

@role_bp.route('/roles', methods=['GET'])
def list_roles():
    roles = RoleService.get_all_roles()
    if not roles:
        return {'message': 'No hay roles disponibles'}, 404

    roles_list = [{'rol_id': role.rol_id, 'name': role.name, 'description': role.description} for role in roles]
    return roles_list


