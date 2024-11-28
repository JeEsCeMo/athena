from app.repositories.dashboard_repository import DashboardRepository

class DashboardService:

    @staticmethod
    def get_fraudulent_transactions_by_bank():
        return DashboardRepository.get_fraudulent_transactions_by_bank()
    
    @staticmethod
    def get_fraudulent_transactions_by_country():
        return DashboardRepository.get_fraudulent_transactions_by_country()
    
    @staticmethod
    def get_fraudulent_transactions_by_merchant():
        return DashboardRepository.get_fraudulent_transactions_by_merchant()