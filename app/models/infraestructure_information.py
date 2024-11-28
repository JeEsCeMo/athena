from app import db
from datetime import datetime
from app.models.terms import Terms

class InfraestructureInformation(db.Model):
    __tablename__ = 'infraestructure_informations'

    infraestructure_information_id = db.Column(db.Integer, primary_key=True)
    ip = db.Column(db.String(45), nullable=False, unique=True)  # IP debe ser única
    is_white_list = db.Column(db.Boolean, default=False, nullable=False)
    is_black_list = db.Column(db.Boolean, default=False, nullable=False)
    country_code = db.Column(db.Integer, db.ForeignKey('terms.term_id'), nullable=True)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    updated_at = db.Column(db.DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)

    # Relación con la tabla `Terms` para los datos del país
    country = db.relationship('Terms', backref='infraestructures', lazy=True)
