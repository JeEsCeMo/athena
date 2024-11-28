from app.repositories.transaction_repository import TransactionRepository
from app.repositories.payment_repository import PaymentRepository
from datetime import datetime, timedelta

class TransactionService:

    @staticmethod
    def get_transactions(page, per_page, filters):
        return TransactionRepository.get_transactions(page, per_page, filters)

    @staticmethod
    def calculate_similar_transaction(public_id, amount, created_at):
        recent_transactions = TransactionRepository.get_recent_transactions_by_public_id(
            public_id, created_at - timedelta(minutes=2), created_at
        )

        similar_transactions = [t for t in recent_transactions if t.amount == amount]
        return 1 if similar_transactions else 0

    @staticmethod
    def calculate_transactions_per_ip(ip, created_at):
        # Cuenta el número de transacciones desde la misma IP en los últimos 1 minuto.
        recent_transactions = TransactionRepository.get_recent_transactions_by_ip(
            ip, created_at - timedelta(minutes=1), created_at
        )
        return len(recent_transactions)

    @staticmethod
    def calculate_payment_variation(public_id, current_card_number):
        recent_transactions = TransactionRepository.get_recent_transactions_by_public_id(
            public_id, datetime.now() - timedelta(minutes=5), datetime.now()
        )

        payment_ids = [t.payment_id for t in recent_transactions if t.payment_id]
        recent_cards = PaymentRepository.get_card_numbers_by_payment_ids(payment_ids)
        recent_card_suffixes = {card[-4:] for card in recent_cards}
        current_card_suffix = current_card_number[-4:]

        return 1 if current_card_suffix in recent_card_suffixes else 0
