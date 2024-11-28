from app.models.merchant import Merchant
from app.models.terms import Terms

class MerchantRepository:

    @staticmethod
    def get_merchants(filters):
        query = Merchant.query.join(Terms, Merchant.country_code == Terms.term_id, isouter=True)

        # Aplicar filtros si existen
        if filters.get('country_code') is not None:
            query = query.filter(Merchant.country_code == filters['country_code'])
        if filters.get('name') is not None:
            query = query.filter(Merchant.name.ilike(f"%{filters['name']}%"))

        # Ordenar por nombre
        query = query.order_by(Merchant.name)
        return query.all()
