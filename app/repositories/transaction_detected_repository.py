from app.models.transaction_detected import TransactionDetected
from app.models.transaction import Transaction
from app.models.bank import Bank
from app.models.merchant import Merchant
from app.models.terms import Terms

class TransactionDetectedRepository:

    @staticmethod
    def get_detected_transactions(page, per_page, filters):
        query = TransactionDetected.query \
            .join(TransactionDetected.transaction) \
            .join(Transaction.bank, isouter=True) \
            .join(Transaction.merchant, isouter=True) \
            .join(Transaction.country, isouter=True)

        # Aplicar filtros si corresponden
        if filters.get('country_code') is not None:
            query = query.filter(Transaction.country_code == filters['country_code'])
        if filters.get('bank_id') is not None:
            query = query.filter(Transaction.bank_id == filters['bank_id'])
        if filters.get('merchant_id') is not None:
            query = query.filter(Transaction.merchant_id == filters['merchant_id'])
        if filters.get('status') is not None:
            query = query.filter(Transaction.status == filters['status'])

        # Paginación
        return query.paginate(page=page, per_page=per_page, error_out=False)
