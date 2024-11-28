from app.models.role import Role
from app import db
from sqlalchemy.exc import SQLAlchemyError

class RoleRepository:
    @staticmethod
    def get_role_by_id(rol_id):
        return Role.query.get(rol_id)

    @staticmethod
    def get_all_roles():
        return Role.query.all()

    @staticmethod
    def create_role(name, description):
        role = Role(name=name, description=description)
        db.session.add(role)
        db.session.commit()
        return role

    @staticmethod
    def update_role(rol_id, data):
        try:
            updated_rows = Role.query.filter_by(rol_id=rol_id).update(data)
            if updated_rows == 0:
                return {"error": "Rol no encontrado"}, 404
            
            db.session.commit()
            return Role.query.get(rol_id)  
        except SQLAlchemyError as e:
            db.session.rollback()
            return {"error": str(e)}, 400

    @staticmethod
    def delete_role(rol_id):
        role = Role.query.get(rol_id)
        if role:
            db.session.delete(role)
            db.session.commit()
