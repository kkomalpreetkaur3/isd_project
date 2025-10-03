"""
Dscription: Represents a chequing account with service charges.
"""

__author__ = "Komalpreet Kaur"
__version__ = "1.0.0"

from bank_account.bank_account import BankAccount

class ChequingAccount(BankAccount):
    """Represents a chequing account with minimum balance and service charges."""

    def __init__(self, account_number: int, client_number: int, balance: float,
                 minimum_balance: float = 100.0):
        """
        Initialize a chequing account.

        Args:
            account_number (int)
            client_number (int)
            balance (float)
            minimum_balance (float): Minimum required balance
        """
        super().__init__(account_number, client_number, balance)
        try:
            self.__minimum_balance = float(minimum_balance)
        except (ValueError, TypeError):
            self.__minimum_balance = 100.0

    @property
    def minimum_balance(self) -> float:
        return self.__minimum_balance
    
    def get_service_charges(self) ->float:
        """Return service charge based on balance relative to minimum."""
        base_charge = 0.50
        if self.balance < self.__minimum_balance:
            return base_charge * 2
        return base_charge
    
    def __str__(self) -> str:
        return super().__str__() + f"\nMinimum Balance: ${self.__minimum_balance:,.2f}"