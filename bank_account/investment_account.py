"""
Description: Represents an investment account with fixed interest rate.
"""

__author__ = "Komalpreet Kaur"
__version__ = "1.0.0"

from bank_account.bank_account import BankAccount

class InvestmentAccount(BankAccount):
    """Represents an investment account with interest."""

    def __init__(self, account_number: int, client_number: int,
                 balance: float, interest_rate: float = 0.05):
        """
        Initialize an investment account.

        Args:
            account_number (int)
            client_number (int)
            balance (float)
            interest_rate (float): Interest rate as decimal
        """
        super().__init__(account_number, client_number, balance)
        try:
            self.__interest_rate = float(interest_rate)
        except (ValueError, TypeError):
            self.__interest_rate = 0.05

    @property
    def interest_rate(self) -> float:
        return self.__interest_rate
    
    def apply_interest(self):
        """Apply interest to balance."""
        self.update_balance(self.balance * self.__interest_rate)

    def __str__(self) -> str:
        return super().__str__() + f"\nInterest Rate: {self.__interest_rate * 100:.2f}%"