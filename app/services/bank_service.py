from app.repositories.bank_repository import BankRepository

class BankService:

    @staticmethod
    def get_banks(filters):
        return BankRepository.get_banks(filters)
