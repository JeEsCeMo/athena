import jwt
import datetime
from flask import jsonify
from app.models.user import User
from app.repositories.user_repository import UserRepository

SECRET_KEY = 'amVzc1NlY3JldEtleQ=='

class AuthJWTService:

    @staticmethod
    def login(username, password):
        print("llega aca login ")
        user = UserRepository.get_user_by_username(username)
        if user and user.check_password(password):
            token = jwt.encode({
                'user_id': user.user_id,
                'exp': datetime.datetime.utcnow() + datetime.timedelta(minutes=30)
            }, SECRET_KEY, algorithm="HS256")
            return jsonify({'token': token})

        return jsonify({'message': 'Credenciales inválidas'}), 401

    @staticmethod
    def verify_token(token):
        try:
            decoded = jwt.decode(token, SECRET_KEY, algorithms=["HS256"])
            user = UserRepository.get_user_by_id(decoded['user_id'])
            if user:
                return user
        except jwt.ExpiredSignatureError:
            return jsonify({'message': 'Token expirado'}), 401
        except jwt.InvalidTokenError:
            return jsonify({'message': 'Token inválido'}), 401
