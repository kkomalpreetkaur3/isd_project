from .service_charge_strategy import ServiceChargeStrategy

class OverdraftStrategy(ServiceChargeStrategy):
    """
    Service charge strategy for chequing/overdraft behaviour.
    """

    def __init__(self, overdraft_penalty: float = 0.50):
        """
        Initialize the overdraft strategy.

        Args:
            overdraft_penalty (float): Penalty applied when balance is negative.
        """
        self._overdraft_penalty = float(overdraft_penalty)

    def calculate_service_charges(self, account) -> float:
        """
        Calculate service charges for accounts with overdraft rules.

        If the account balance is negative, return BASE_SERVICE_CHARGE + penalty.
        Otherwise, return 0.0.

        Args:
            account: A BankAccount instance.

        Returns:
            float: The service charge amount.
        """
        balance = float(account.balance)
        if balance >= 0:
            return 0.0
        return round(self.BASE_SERVICE_CHARGE + self._overdraft_penalty, 2)
        