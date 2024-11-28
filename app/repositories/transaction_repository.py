from app.models.transaction import Transaction
from app.models.terms import Terms
from app.models.bank import Bank
from app.models.merchant import Merchant

class TransactionRepository:
    @staticmethod
    def get_transactions(page, per_page, filters):
        # Iniciar la consulta
        query = Transaction.query \
            .join(Terms, Transaction.country_code == Terms.term_id, isouter=True) \
            .join(Bank, Transaction.bank_id == Bank.bank_id, isouter=True) \
            .join(Merchant, Transaction.merchant_id == Merchant.merchant_id, isouter=True)

        # Aplicar filtros si existen
        if filters.get('country_code') is not None:
            query = query.filter(Transaction.country_code == filters['country_code'])
        if filters.get('bank_id') is not None:
            query = query.filter(Transaction.bank_id == filters['bank_id'])
        if filters.get('merchant_id') is not None:
            query = query.filter(Transaction.merchant_id == filters['merchant_id'])
        if filters.get('status') is not None:
            query = query.filter(Transaction.status == filters['status'])

        # Paginar resultados
        return query.paginate(page=page, per_page=per_page, error_out=False)
    
    @staticmethod
    def get_recent_transactions_by_public_id(public_id, start_time, end_time):
        return Transaction.query.filter(
            Transaction.public_id == public_id,
            Transaction.created_at >= start_time,
            Transaction.created_at < end_time
        ).all()

    @staticmethod
    def get_recent_transactions_by_ip(ip, start_time, end_time):
        return Transaction.query.filter(
            Transaction.ip == ip,
            Transaction.created_at >= start_time,
            Transaction.created_at < end_time
        ).all()
