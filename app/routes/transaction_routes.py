from flask import Blueprint, request
from app.services.transaction_service import TransactionService
import json


transaction_bp = Blueprint('transaction_bp', __name__)

@transaction_bp.route('/transactions', methods=['GET'])
def list_transactions():
    page = request.args.get('page', 1, type=int)
    per_page = request.args.get('per_page', 15, type=int)
    filters = {
        'country_code': request.args.get('country_code'),
        'bank_id': request.args.get('bank_id'),
        'merchant_id': request.args.get('merchant_id'),
        'status': request.args.get('status')
    }

    transactions = TransactionService.get_transactions(page, per_page, filters)

    # Construir la lista con datos relacionados
    transactions_list = [{
        'transaction_id': t.transaction_id,
        'amount': t.amount,
        'country_code': t.country_code,
        'country_description': t.country.description if t.country else None,
        'bank_id': t.bank_id,
        'bank_name': t.bank.name if t.bank else None,
        'merchant_id': t.merchant_id,
        'merchant_name': t.merchant.name if t.merchant else None,
        'status': t.status,
        'created_at': t.created_at
    } for t in transactions.items]

    return {
        'transactions': transactions_list,
        'total': transactions.total,
        'pages': transactions.pages,
        'current_page': transactions.page
    }
