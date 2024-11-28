from flask import Blueprint
from app.services.dashboard_service import DashboardService
from app.utils.cripto import encrypt_payment_data

dashboard_bp = Blueprint('dashboard_bp', __name__)

@dashboard_bp.route('/dashboard/fraudulent-transactions-by-bank', methods=['GET'])
def fraudulent_transactions_by_bank():
    data = DashboardService.get_fraudulent_transactions_by_bank()
    result = [{'bank_name': item.bank_name, 'fraudulent_count': item.fraudulent_count} for item in data]
    return result

@dashboard_bp.route('/dashboard/fraudulent-transactions-by-country', methods=['GET'])
def fraudulent_transactions_by_country():
    data = DashboardService.get_fraudulent_transactions_by_country()
    result = [{'country_name': item.country_name, 'fraudulent_count': item.fraudulent_count} for item in data]
    return result

@dashboard_bp.route('/dashboard/fraudulent-transactions-by-merchant', methods=['GET'])
def fraudulent_transactions_by_merchant():
    data = DashboardService.get_fraudulent_transactions_by_merchant()
    result = [{'merchant_name': item.merchant_name, 'fraudulent_count': item.fraudulent_count} for item in data]
    return result

#  payment = {"cardNumber" : "1234567890123456",
#             "holderName": "Jessica Cedeño",
#             "expirationDate": "1215",
#             "brand" :"VISA"}
    
#     KEY_ENCRIPY_DATA = 'amVzc1NlY3JldEtleQ=='
#     encrypted_data = encrypt_payment_data(payment, KEY_ENCRIPY_DATA)