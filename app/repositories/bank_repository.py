from app.models.bank import Bank
from app.models.terms import Terms

class BankRepository:

    @staticmethod
    def get_banks(filters):
        query = Bank.query.join(Terms, Bank.country_code == Terms.term_id, isouter=True)

        # Aplicar filtros si existen
        if filters.get('country_code') is not None:
            query = query.filter(Bank.country_code == filters['country_code'])
        if filters.get('name') is not None:
            query = query.filter(Bank.name.ilike(f"%{filters['name']}%"))
        if filters.get('bank_code') is not None:
            query = query.filter(Bank.bank_code.ilike(f"%{filters['bank_code']}%"))

        # Ordenar por nombre
        query = query.order_by(Bank.name)
        return query.all()
