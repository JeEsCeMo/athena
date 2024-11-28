from app import db
from datetime import datetime
class Bank(db.Model):
    __tablename__ = 'banks'

    bank_id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(70), nullable=False)
    bank_code = db.Column(db.String(10), nullable=True)
    country_code = db.Column(db.Integer, nullable=True)
    created_at = db.Column(db.DateTime, default=datetime.utcnow) 
