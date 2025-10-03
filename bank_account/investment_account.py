"""
Description: Represents an investment account with fixed interest rate.
"""

__author__ = "Komalpreet Kaur"
__version__ = "1.0.0"

from bank_account.bank_account import BankAccount

class InvestmentAccount(BankAccount):
    """Represents an investment account with interest."""

    def __init__(self, account_number, client_number, balance, interest_rate=0.0):
        super().__init__(account_number, client_number, balance)
        try:
            self.__interest_rate = float(interest_rate)
        except (ValueError, TypeError):
            self.__interest_rate = 0.0

    @property
    def interest_rate(self):
        return self.__interest_rate
    
    def apply_interest(self):
        """Apply interest to balance."""
        interest = self.balance * self.__interest_rate
        self.update_balance(interest)

    def debit(self, amount):
        """Withdraw a positive amount if balance allows."""
        if amount <= 0:
            raise ValueError("Debit amount must be positive")
        if amount > self.balance:
            raise ValueError("Insufficient funds")
        self.update_balance(-amount)

    def account_info(self):
        """Return account info as a string."""
        return (
            f"Account Number: {self.account_number}\n"
            f"Client Number: {self.client_number}\n"
            f"Balance: ${self.balance:.2f}\n"
            f"Interest Rate: {self.__interest_rate * 100:.2%}"
        )
    def __str__(self):
        return (
            f"Account Number: {self.account_number}\n"
            f"Client Number: {self.client_number}\n"
            f"Balance: ${self.balance:.2f}\n"
            f"Interest Rate: {self.__interest_rate * 100:.2f}%"
        )