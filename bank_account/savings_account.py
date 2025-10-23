"""
Description: Represents a savings account with minimum balance and service charges.
Uses the MinimumBalanceStrategy for service charge calculation.
"""

__author__ = "Komalpreet Kaur"
__version__ = "1.0.0"

from datetime import date
from bank_account import BankAccount
from patterns.strategy.minimum_balance_strategy import MinimumBalanceStrategy

class SavingsAccount(BankAccount):
    """
    Represents a savings account with minimum balance and service charges.
    Service charge is delegated to MinimumBalanceStrategy.
    """

    def __init__(self, account_number: int, client_number: int,  balance: float, creation_date: date, minimum_balance: float):
        super().__init__(account_number, client_number, balance)  
        self.creation_date = creation_date
        self.__minimum_balance = float(minimum_balance)
        self.__service_strategy = MinimumBalanceStrategy(minimum_balance=self.__minimum_balance, service_charge_premium=0.50)

    @property
    def minimum_balance(self) -> float:
        return self.__minimum_balance
    
    def get_service_charges(self) -> float:
        """Delegate service charge calculation to strategy."""
        return self.__service_strategy.calculate_service_charges(self)
    
    
    def apply_interest(self):
        """Savings account has no interest by default (tests expect this stub)."""
        return 0.0

    def debit(self, amount: float):
        """Withdraw if possible, ensuring minimum balance is not violated."""
        if amount <= 0:
            raise ValueError("Debit amount must be positive")
        if amount > self.balance:
            raise ValueError("Insufficient funds")
        self.update_balance(-amount)
        self._post_transaction_checks(amount)

    def account_info(self) -> str:
        """Return account info as a string."""
        return (
            f"Account Number: {self.account_number}\n"
            f"Balance: ${self.balance:.2f}\n"
            f"Creation Date: {self.creation_date}\n"
            f"Minimum Balance: ${self.__minimum_balance:.2f}"
        )
    
    def __str__(self):
        return (
            f"Account Number: {self.account_number}\n"
            f"Client Number: {self.client_number}\n"
            f"Balance: ${self.balance:.2f}\n"
            f"Creation Date: {self.creation_date}\n"
            f"Minimum Balance: ${self.minimum_balance:.2f}"
        )
        