from .service_charge_strategy import ServiceChargeStrategy

class OverdraftStrategy(ServiceChargeStrategy):
    """
    Service charge strategy for chequing accounts with overdraft behaviour.
    """

    def __init__(self, minimum_balance, base_service_charge, overdraft_limit):
        """
        Initialize the overdraft strategy.

        Args:
            minimum_balance (float): Minimum balance required before extra charge applies.
            base_service_charge (float): Standard base charge.
            overdraft_limit (float): Maximum negative balance allowed (overdraft limit).
        """
        self.minimum_balance = minimum_balance
        self.base_service_charge = base_service_charge
        self.overdraft_limit = overdraft_limit

    def calculate_service_charges(self, balance):
        """
        Calculate service charges based on the account balance.

        - If the balance is below the overdraft limit, apply triple charge.
        - If the balance is below minimum but above overdraft, apply double charge.
        - Otherwise, apply base charge.

        Args:
            balance (float): Current account balance.

        Returns:
            float: Calculated service charge.
        """
        if balance < self.overdraft_limit:
            return self.base_service_charge * 3
        elif balance < self.minimum_balance:
            return self.base_service_charge * 2
        return self.base_service_charge
