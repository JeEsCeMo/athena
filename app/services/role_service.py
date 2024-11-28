from app.repositories.role_repository import RoleRepository

class RoleService:

    @staticmethod
    def get_role(rol_id):
        return RoleRepository.get_role_by_id(rol_id)

    @staticmethod
    def create_role(name, description):
        return RoleRepository.create_role(name, description)

    @staticmethod
    def update_role(rol_id, data):
        return RoleRepository.update_role(rol_id, data)

    @staticmethod
    def delete_role(rol_id):
        return RoleRepository.delete_role(rol_id)
    
    @staticmethod
    def get_all_roles():
        return RoleRepository.get_all_roles()
