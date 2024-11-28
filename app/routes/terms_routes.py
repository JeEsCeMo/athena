from flask import Blueprint, request
from app.services.terms_service import TermsService

country_bp = Blueprint('country_bp', __name__)

@country_bp.route('/countries', methods=['GET'])
def list_countries():
    # Obtener filtros de los parámetros de la solicitud
    filters = {
        'description': request.args.get('description'),
        'code': request.args.get('code')
    }

    # Obtener países desde el servicio
    countries = TermsService.get_countries(filters)

    # Serializar los resultados
    countries_list = [{
        'term_id': country.term_id,
        'description': country.description,
        'code': country.code,
        'created_at': country.created_at.isoformat()
    } for country in countries]

    return {
        'countries': countries_list,
        'total': len(countries_list)
    }
