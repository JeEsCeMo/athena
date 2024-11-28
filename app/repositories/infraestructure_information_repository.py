from app.models.infraestructure_information import InfraestructureInformation

class InfraestructureRepository:

    @staticmethod
    def get_blacklist_ips():
        # Consulta todas las IPs marcadas como blacklist
        return [row.ip for row in InfraestructureInformation.query.filter_by(is_black_list=True).all()]
