from app.repositories.user_repository import UserRepository

class UserService:
    @staticmethod
    def get_user(user_id):
        return UserRepository.get_user_by_id(user_id)
    
    @staticmethod
    def get_all_users():
        return UserRepository.get_all_users()

    @staticmethod
    def create_user(username, password, rol_id):
        return UserRepository.create_user(username, password, rol_id)

    @staticmethod
    def update_user(user_id, data):
        return UserRepository.update_user(user_id, data)

    @staticmethod
    def delete_user(user_id):
        return UserRepository.delete_user(user_id)
