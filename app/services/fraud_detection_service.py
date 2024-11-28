from app.repositories.infraestructure_information_repository import InfraestructureRepository

class FraudDetectionService:

    @staticmethod
    def get_blacklisted_ips():
        return InfraestructureRepository.get_blacklist_ips()
