from app import db
from datetime import datetime

class Terms(db.Model):
    __tablename__ = 'terms'

    term_id = db.Column(db.Integer, primary_key=True)
    description = db.Column(db.String(50), nullable=False)
    key = db.Column(db.String(50), nullable=False)
    code = db.Column(db.String(15), nullable=True)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
