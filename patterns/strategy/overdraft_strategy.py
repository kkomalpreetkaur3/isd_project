from .service_charge_strategy import ServiceChargeStrategy

class OverdraftStrategy(ServiceChargeStrategy):
    """
    Service charge strategy for chequing/overdraft behaviour.

    - If account balance < 0, apply BASE_SERVICE_CHARGE and overdraft_penalty.
    - Otherwise no service charge.
    """

    def __init__(self, overdraft_penalty: float = 0.50):
        self._overdraft_penalty = float(overdraft_penalty)

    def calculate_service_charges(self, account) -> float:
        balance = float(account.balance)
        if balance >= 0:
            return 0.0
        return round(self.BASE_SERVICE_CHARGE + self._overdraft_penalty, 2)
        