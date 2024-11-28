from flask import Blueprint, request
from app.services.auth_jwt import AuthJWTService

auth_bp = Blueprint('auth_bp', __name__)

@auth_bp.route('/login', methods=['POST'])
def login():
    data = request.get_json()
    try:
        return AuthJWTService.login(data['username'], data['password'])
    except KeyError:
        print("aca etsamos", KeyError)
        return {'message': 'Datos incorrectos'}, 400
    # return AuthJWTService.login(data['username'], data['password'])
