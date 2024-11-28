from app.models.user import User
from app import db
from sqlalchemy.exc import SQLAlchemyError

class UserRepository:
    @staticmethod
    def get_user_by_id(user_id):
        return User.query.get(user_id)

    @staticmethod
    def get_all_users():
        return User.query.all()

    @staticmethod
    def create_user(username, password, rol_id):
        user = User(username=username, rol_id=rol_id)
        user.set_password(password)
        db.session.add(user)
        db.session.commit()
        return user

    @staticmethod
    def update_user(user_id, data):
        try:
            updated_rows = User.query.filter_by(user_id=user_id).update(data)
            if updated_rows == 0:
                return {"error": "Usuario no encontrado"}, 404
            
            db.session.commit()
            return User.query.get(user_id)  
        except SQLAlchemyError as e:
            db.session.rollback()
            return {"error": str(e)}, 400


    @staticmethod
    def delete_user(user_id):
        user = User.query.get(user_id)
        if user:
            db.session.delete(user)
            db.session.commit()

    @staticmethod
    def get_user_by_username(username):
        return User.query.filter_by(username=username).first()
