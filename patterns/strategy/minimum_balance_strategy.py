from .service_charge_strategy import ServiceChargeStrategy

class MinimumBalanceStrategy(ServiceChargeStrategy):
    """
    Minimum balance strategy used by SavingAccount.
    If balance falls below minimum_balance, charge base and premium.
    """
    def __init__(self, minimum_balance: float = 1000.0, service_charge_premium: float = 0.50):
        """
        Initialize the minimum balance strategy.

        Args:
            minimum_balance (float): The required minimum balance.
            service_charge_premium (float): Extra charge applied when below minimum.
        """
        self._minimum_balance = float(minimum_balance)
        self._service_charge_premium = float(service_charge_premium)

    def calculate_service_charges(self, account) -> float:
        """
        Calculate service charges based on minimum balance requirement.

        Args:
            account: A BankAccount instance.

        Returns:
            float: The service charge amount.
        """
        balance = float(account.balance)
        if balance < self._minimum_balance:
            return round(self.BASE_SERVICE_CHARGE + self._service_charge_premium, 2)
        return 0.0