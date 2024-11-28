from app.models.payment import Payment
from app import db

class PaymentRepository:

    @staticmethod
    def get_card_numbers_by_transaction_ids(transaction_ids):
        if not transaction_ids:
            return []

        payments = Payment.query.filter(Payment.transaction_id.in_(transaction_ids)).all()
        return [p.card_number for p in payments]
