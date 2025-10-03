"""
Description: Represents a savings account with minimum balance and service charges.
"""

__author__ = "Komalpreet Kaur"
__version__ = "1.0.0"

from datetime import date
from bank_account.bank_account import BankAccount

class SavingsAccount(BankAccount):
    """Represents a savings account with minimum balance and service charges."""

    BASE_SERVICE_CHARGE = 0.50

    def __init__(self, account_number,  balance, creation_date: date, minimum_balance: float):
        super().__init__(account_number, 0, balance)  
        self.creation_date = creation_date
        self.__minimum_balance = minimum_balance

    @property
    def minimum_balance(self):
        return self.__minimum_balance
    
    def get_service_charges(self):
        """Return service charge based on balance relative to minimum."""
        if self.balance < self.__minimum_balance:
            return self.BASE_SERVICE_CHARGE * 2
        return self.BASE_SERVICE_CHARGE
    
    
    def apply_interest(self):
        """Savings account has no interest by default (tests expect this stub)."""
        return 0.0

    def debit(self, amount):
        """Withdraw if possible, ensuring minimum balance is not violated."""
        if amount <= 0:
            raise ValueError("Debit amount must be positive")
        if amount > self.balance:
            raise ValueError("Insufficient funds")
        self.update_balance(-amount)

    def account_info(self):
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
        