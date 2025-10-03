"""
Description: Represents a savings account with minimum balance and service charges.
"""

__author__ = "Komalpreet Kaur"
__version__ = "1.0.0"

from datetime import date
from bank_account.bank_account import BankAccount

class SavingsAccount(BankAccount):
    """Represents a savings account with minimum balance and service charges."""

    def __init__(self, account_number: int, balance: float,
                 creation_date: date, minimum_balance: float = 50.0):
        """
        Initialize a savings account.
   
         Args:
            account_number (int)
            balance (float)
            creation_date (date)
            minimum_balance (float)
        """
        super().__init__(account_number, 0, balance)  
        self.creation_date = creation_date
        try:
            self.__minimum_balance = float(minimum_balance)
        except (ValueError, TypeError):
            self.__minimum_balance = 50.0

    @property
    def minimum_balance(self) -> float:
        return self.__minimum_balance
    
    def get_service_charges(self) -> float:
        """Return service charge based on balance relative to minimum."""
        base_charge = 0.50
        if self.balance < self.__minimum_balance:
            return base_charge * 2
        return base_charge
    
    def __str__(self) -> str:
        return (
            super().__str__() +
            f"\nCreation Date: {self.creation_date}" +
            f"\nMinimum Balance: ${self.__minimum_balance:,.2f}"
        )