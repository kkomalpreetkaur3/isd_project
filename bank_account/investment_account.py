"""
Description: Represents an investment account with fixed interest rate.
Uses ManagementFeeStrategy for service charge calculation.
"""

__author__ = "Komalpreet Kaur"
__version__ = "1.0.0"

from bank_account.bank_account import BankAccount
from patterns.strategy.management_fee_strategy import ManagementFeeStrategy
from datetime import date

class InvestmentAccount(BankAccount):
    """Represents an investment account with interest."""

    def __init__(self, account_number, client_number, balance, date_created, management_fee):
        """
        Initialize InvestmentAccount.

        Args:
            account_number (int): Unique account number.
            client_number (int): Owner client number.
            balance (float): Initial balance.
            interest_rate (float): Annual interest rate as decimal (e.g., 0.02).
            opened_date (date): Date when account was opened (optional).
        """
        super().__init__(account_number, client_number, balance, date_created)
        try:
            self.__interest_rate = float(interest_rate)
        except (ValueError, TypeError):
            self.__interest_rate = 0.0

        self.__service_strategy = ManagementFeeStrategy(annual_fee_percent=0.001, opened_date=opened_date)
        self.management_fee = management_fee
        
    @property
    def interest_rate(self) -> float:
        """Return the interest rate for this investment account."""
        return self.__interest_rate
    
    def apply_interest(self):
        """Apply interest to the account balance using the configured interest rate."""
        interest_amount = self.balance * self.__interest_rate
        self.update_balance(interest_amount)

    def debit(self, amount: float):
        """
        Withdraw an amount if sufficient funds exist.

        Args:
            amount (float): Amount to withdraw.

        Raises:
            ValueError: If invalid amount or insufficient funds.
        """
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
            f"Client Number: {self.client_number}\n"
            f"Balance: ${self.balance:.2f}\n"
            f"Interest Rate: {self.__interest_rate * 100:.2f%}"
        )
    
    def get_service_charges(self) -> float:
        """
        Delegates service charge calculation to ManagementFeeStrategy.
        """
        return self.__service_strategy.calculate_service_charges(self)
    
    def __str__(self) -> str:
        """Return a formatted string for the investment account."""
        return (
            f"Account Number: {self.account_number}\n"
            f"Client Number: {self.client_number}\n"
            f"Balance: ${self.balance:.2f}\n"
            f"Interest Rate: {self.__interest_rate * 100:.2f}%"
        )