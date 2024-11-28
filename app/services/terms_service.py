from app.repositories.terms_repository import TermsRepository

class TermsService:

    @staticmethod
    def get_countries(filters):
        return TermsRepository.get_countries(filters)
