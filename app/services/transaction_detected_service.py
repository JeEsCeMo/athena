from app.repositories.transaction_detected_repository import TransactionDetectedRepository

class TransactionDetectedService:

    @staticmethod
    def get_detected_transactions(page, per_page, filters):
        return TransactionDetectedRepository.get_detected_transactions(page, per_page, filters)
