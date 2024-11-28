from app import db
from datetime import datetime
from app.models.transaction import Transaction

class Payment(db.Model):
    __tablename__ = 'payments'

    payment_id = db.Column(db.Integer, primary_key=True)
    card_number = db.Column(db.String(22), nullable=False)
    ip = db.Column(db.String(30), nullable=False)
    transaction_id = db.Column(db.Integer, db.ForeignKey('transactions.transaction_id'), nullable=False)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)

    transaction = db.relationship('Transaction', backref='payments', lazy=True)

