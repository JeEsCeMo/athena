from app import db
from datetime import datetime
from app.models.transaction import Transaction

class TransactionDetected(db.Model):
    __tablename__ = 'transactions_detected'

    transaction_detected_id = db.Column(db.Integer, primary_key=True)
    transaction_id = db.Column(db.Integer, db.ForeignKey('transactions.transaction_id'), nullable=False)
    ip = db.Column(db.String(30), nullable=False)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)

    # Relación con Transaction
    transaction = db.relationship('Transaction', backref='detected_transactions', lazy=True)
