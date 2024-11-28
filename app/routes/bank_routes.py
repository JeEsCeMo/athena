from flask import Blueprint, request
from app.services.bank_service import BankService

bank_bp = Blueprint('bank_bp', __name__)

@bank_bp.route('/banks', methods=['GET'])
def list_banks():
    # Obtener filtros de los parámetros de la solicitud
    filters = {
        'country_code': request.args.get('country_code'),
        'name': request.args.get('name'),
        'bank_code': request.args.get('bank_code')
    }

    # Obtener bancos desde el servicio
    banks = BankService.get_banks(filters)

    # Serializar los resultados
    banks_list = [{
        'bank_id': bank.bank_id,
        'name': bank.name,
        'bank_code': bank.bank_code,
        'country_code': bank.country_code,
        'created_at': bank.created_at.isoformat()
    } for bank in banks]

    return {
        'banks': banks_list,
        'total': len(banks_list)
    }