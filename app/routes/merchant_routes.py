from flask import Blueprint, request
from app.services.merchant_service import MerchantService

merchant_bp = Blueprint('merchant_bp', __name__)

@merchant_bp.route('/merchants', methods=['GET'])
def list_merchants():
    # Obtener filtros de los parámetros de la solicitud
    filters = {
        'country_code': request.args.get('country_code'),
        'name': request.args.get('name')
    }

    # Obtener comercios desde el servicio
    merchants = MerchantService.get_merchants(filters)

    # Serializar los resultados
    merchants_list = [{
        'merchant_id': merchant.merchant_id,
        'name': merchant.name,
        'merchant_code': merchant.merchant_code,
        'country_code': merchant.country_code,
        'created_at': merchant.created_at.isoformat()
    } for merchant in merchants]

    return {
        'merchants': merchants_list,
        'total': len(merchants_list)
    }
