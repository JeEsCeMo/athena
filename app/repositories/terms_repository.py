from app.models.terms import Terms

class TermsRepository:

    @staticmethod
    def get_countries(filters):
        query = Terms.query

        # Aplicar filtros si existen
        if filters.get('description') is not None:
            query = query.filter(Terms.description.ilike(f"%{filters['description']}%"))
        if filters.get('code') is not None:
            query = query.filter(Terms.code == filters['code'])

        # Ordenar por descripción
        query = query.order_by(Terms.description)
        return query.all()
