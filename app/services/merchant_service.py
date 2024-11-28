from app.repositories.merchant_repository import MerchantRepository

class MerchantService:

    @staticmethod
    def get_merchants(filters):
        return MerchantRepository.get_merchants(filters)
