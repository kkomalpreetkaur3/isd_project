from .service_charge_strategy import ServiceChargeStrategy
from datetime import date, timedelta

class ManagementFeeStrategy(ServiceChargeStrategy):
    """
    Management fee strategy used by InvestmentAccount.
    Applies a small proportional fee plus the base service charge.
    """
    TEN_YEARS_AGO = date.today() - timedelta(days = int(10 * 365.25))

    def __init__(self, annual_fee_percent: float = 0.001, opened_date: date = None):
        """
        Initialize the management fee strategy.

        Args:
            annual_fee_percent (float): Proportional fee applied to balance.
            opened_date (date): Account opened date (optional).
        """
        self._annual_fee_percent = float(annual_fee_percent)
        self._opened_date = opened_date

    def calculate_service_charges(self, account) -> float:
        """
        Calculate the management fee for the investment account.

        Args:
            account: A BankAccount instance.

        Returns:
            float: The service charge amount.
        """
        balance = float(account.balance)
        charge = self.BASE_SERVICE_CHARGE
        if balance > 0:
            fee = balance * self._annual_fee_percent
            charge += fee
        return round(max(charge, 0.0), 2)
