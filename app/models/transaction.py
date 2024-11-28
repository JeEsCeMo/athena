from app import db
from datetime import datetime
from app.models.bank import Bank
from app.models.merchant import Merchant
from app.models.terms import Terms

class Transaction(db.Model):
    __tablename__ = 'transactions'

    transaction_id = db.Column(db.Integer, primary_key=True)
    amount = db.Column(db.String(20), nullable=False)
    public_id = db.Column(db.String(50), nullable=False)
    ip = db.Column(db.String(30), nullable=False)

    country_code = db.Column(db.Integer, db.ForeignKey('terms.term_id'), nullable=True)
    bank_id = db.Column(db.Integer, db.ForeignKey('banks.bank_id'), nullable=True)

    merchant_id = db.Column(db.Integer, db.ForeignKey('merchants.merchant_id'), nullable=True)
    status = db.Column(db.Integer, nullable=False)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)

    # Relación con Bank
    bank = db.relationship('Bank', backref='transaction', lazy=True)
    merchant = db.relationship('Merchant', backref='transaction', lazy=True)
    country = db.relationship('Terms', backref='transactions', lazy=True)

    def serialize(self):
        return {
            'transaction_id': self.transaction_id,
            'amount': self.amount,
            'country_code': self.country_code,
            'bank_id': self.bank_id,
            'merchant_id': self.merchant_id,
            'status': self.status,
            'public_id': self.public_id,
            'ip': self.ip,
            'created_at': self.created_at.isoformat()
        }
