from .service_charge_strategy import ServiceChargeStrategy

class OverdraftStrategy(ServiceChargeStrategy):
    """
    Service charge strategy for chequing/overdraft behaviour.

    - If account balance < 0, apply BASE_SERVICE_CHARGE + overdraft_penalty.
    - Otherwise no service charge.
    """

    def __init__(self, overdraft_penalty: float = 5.00, per_dollar_penalty: float = 0.0):
        self._overdraft_penalty = float(overdraft_penalty)
        self._per_dollar_penalty = float(per_dollar_penalty)

    def calculate_service_charges(self, account) -> float:
        balance = float(account.balance)
        if balance >= 0:
            return 0.0
        additional = self._overdraft_penalty + (abs(balance) * self._per_dollar_penalty)
        return round(self.BASE_SERVICE_CHARGE + additional, 2)
        