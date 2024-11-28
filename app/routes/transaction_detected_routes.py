from flask import Blueprint, request
from app.services.transaction_detected_service import TransactionDetectedService

transaction_detected_bp = Blueprint('transaction_detected_bp', __name__)

@transaction_detected_bp.route('/transactions_detected', methods=['GET'])
def list_detected_transactions():
    page = request.args.get('page', 1, type=int)
    per_page = request.args.get('per_page', 15, type=int)
    filters = {
        'country_code': request.args.get('country_code'),
        'bank_id': request.args.get('bank_id'),
        'merchant_id': request.args.get('merchant_id'),
        'status': request.args.get('status')
    }

    detected_transactions = TransactionDetectedService.get_detected_transactions(page, per_page, filters)

    detected_transactions_list = []
    for dt in detected_transactions.items:
        transaction = dt.transaction
        detected_transactions_list.append({
            'transaction_detected_id': dt.transaction_detected_id,
            'transaction_id': transaction.transaction_id,
            'amount': transaction.amount,
            'country_code': transaction.country_code,
            'country_description': transaction.country.description if transaction and transaction.country else None,
            'bank_id': transaction.bank_id,
            'bank_name': transaction.bank.name if transaction and transaction.bank else None,
            'merchant_id': transaction.merchant_id,
            'merchant_name': transaction.merchant.name if transaction and transaction.merchant else None,
            'status': transaction.status,
            'transaction_created_at': transaction.created_at,
            'created_at': dt.created_at
        })

    return {
        'transactions_detected': detected_transactions_list,
        'total': detected_transactions.total,
        'pages': detected_transactions.pages,
        'current_page': detected_transactions.page
    }
