from .service_charge_strategy import ServiceChargeStrategy

class MinimumBalanceStrategy(ServiceChargeStrategy):
    """
    Service charge for accounts that require a minimum balance (e.g. Savings).
    """
    def __init__(self, minimum_balance: float = 1000.0, service_charge_premium: float = 7.50):
        self._minimum_balance = float(minimum_balance)
        self._service_charge_premium = float(service_charge_premium)

    def calculate_service_charges(self, account) -> float:
        balance = float(account.balance)
        if balance < self._minimum_balance:
            return round(self.BASE_SERVICE_CHARGE + self._service_charge_premium, 2)
        return 0.0