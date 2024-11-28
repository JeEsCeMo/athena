from flask import Flask, request, jsonify, make_response
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from config import Config
import jwt

db = SQLAlchemy()
migrate = Migrate()

def create_app():
    app = Flask(__name__)
    EXCLUDED_ROUTES = ['/api/login']
    from app.services.auth_jwt import SECRET_KEY

    app.config.from_object(Config)
    db.init_app(app)
    migrate.init_app(app, db)
    
    from app.routes.auth_routes import auth_bp
    from app.routes.user_routes import user_bp
    from app.routes.role_routes import role_bp
    from app.routes.transaction_routes import transaction_bp
    from app.routes.transaction_detected_routes import transaction_detected_bp
    from app.routes.bank_routes import bank_bp
    from app.routes.merchant_routes import merchant_bp
    from app.routes.terms_routes import country_bp
    from app.routes.dashboard_routes import dashboard_bp
    
    app.register_blueprint(auth_bp, url_prefix='/api')
    app.register_blueprint(user_bp, url_prefix='/api')
    app.register_blueprint(role_bp, url_prefix='/api')
    app.register_blueprint(transaction_detected_bp, url_prefix='/api')
    app.register_blueprint(transaction_bp, url_prefix='/api')
    app.register_blueprint(bank_bp, url_prefix='/api')
    app.register_blueprint(merchant_bp, url_prefix='/api')
    app.register_blueprint(country_bp, url_prefix='/api')
    app.register_blueprint(dashboard_bp, url_prefix='/api')

    @app.after_request
    def format_success_response(response):
        if response.is_json and response.status_code >= 200 and response.status_code < 300:
            data = response.get_json()

            if isinstance(data, dict) and 'status' in data:
                return response 

            formatted_response = {
                'status': True,
                'data': data
            }
            return make_response(jsonify(formatted_response), response.status_code)
        return response

    @app.errorhandler(Exception)
    def handle_exception(e):
        response = {
            'status': False,
            'message': str(e)
        }
        status_code = getattr(e, 'code', 400)
        return jsonify(response), status_code

    @app.before_request
    def require_jwt():
        if request.path in EXCLUDED_ROUTES:
            return None

        auth_header = request.headers.get('Authorization')
        if not auth_header or not auth_header.startswith('Bearer '):
            return jsonify({'status': False, 'message': 'Token inválido'}), 401

        token = auth_header.split(" ")[1]
        try:
            decoded = jwt.decode(token, SECRET_KEY, algorithms=["HS256"])
        except jwt.ExpiredSignatureError:
            return jsonify({'status': False, 'message': 'Token expirado'}), 401
        except jwt.InvalidTokenError:
            return jsonify({'status': False, 'message': 'Token inválido'}), 401

        return None
    

    return app