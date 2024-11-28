from app.models.transaction_detected import TransactionDetected
from app.models.transaction import Transaction
from app.models.bank import Bank
from app import db
from app.models.merchant import Merchant
from app.models.terms import Terms

class DashboardRepository:

    @staticmethod
    def get_fraudulent_transactions_by_bank():
        query = (
            db.session.query(
                Bank.name.label('bank_name'),
                db.func.count(TransactionDetected.transaction_detected_id).label('fraudulent_count')
            )
            .join(Transaction, Transaction.transaction_id == TransactionDetected.transaction_id)
            .join(Bank, Transaction.bank_id == Bank.bank_id)
            .group_by(Bank.name)
            .order_by(db.func.count(TransactionDetected.transaction_detected_id).desc())
        )
        return query.all()
    
    @staticmethod
    def get_fraudulent_transactions_by_country():
        query = (
            db.session.query(
                Terms.description.label('country_name'),
                db.func.count(TransactionDetected.transaction_detected_id).label('fraudulent_count')
            )
            .join(Transaction, Transaction.transaction_id == TransactionDetected.transaction_id)
            .join(Terms, Transaction.country_code == Terms.term_id)
            .group_by(Terms.description)
            .order_by(db.func.count(TransactionDetected.transaction_detected_id).desc())
        )
        return query.all()
    
    @staticmethod
    def get_fraudulent_transactions_by_merchant():
        query = (
            db.session.query(
                Merchant.name.label('merchant_name'),
                db.func.count(TransactionDetected.transaction_detected_id).label('fraudulent_count')
            )
            .join(Transaction, Transaction.transaction_id == TransactionDetected.transaction_id)
            .join(Merchant, Transaction.merchant_id == Merchant.merchant_id)
            .group_by(Merchant.name)
            .order_by(db.func.count(TransactionDetected.transaction_detected_id).desc())
        )
        return query.all()
