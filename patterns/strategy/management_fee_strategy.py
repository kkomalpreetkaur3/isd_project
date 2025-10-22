from .service_charge_strategy import ServiceChargeStrategy
from datetime import date, timedelta

class ManagementFeeStrategy(ServiceChargeStrategy):
    """
    Service charge strategy for investment accounts (management fee).
    """
    TEN_YEARS_AGO = date.today() - timedelta(days = int(10 * 365.25))

    def __init__(self, annual_fee_percent: float = 0.005, senior_discount_percent: float = 0.0, opened_date=None):
        self._annual_fee_percent = float(annual_fee_percent)
        self._senior_discount_percent = float(senior_discount_percent)
        self._opened_date = opened_date

    def calculate_service_charges(self, account) -> float:
        balance = float(account.balance)
        charge = self.BASE_SERVICE_CHARGE
        if balance > 0:
            fee = balance * self._annual_fee_percent
            if self._opened_date and self._opened_date <= self.TEN_YEARS_AGO:
                fee *= max(0.0, 1.0 - self._senior_discount_percent)
            charge += fee
        return round(max(charge, 0.0), 2)
