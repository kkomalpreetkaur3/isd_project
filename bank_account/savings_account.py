"""
Description:
Represents a savings account with minimum balance and service charges.
Uses the MinimumBalanceStrategy for service charge calculation.
"""

__author__ = "Komalpreet Kaur"
__version__ = "1.0.0"

from datetime import date
from bank_account.bank_account import BankAccount
from patterns.strategy.minimum_balance_strategy import MinimumBalanceStrategy

class SavingsAccount(BankAccount):
    """
    SavingsAccount includes creation_date and minimum balance.
    Service charge is delegated to MinimumBalanceStrategy.
    """

    def __init__(self, account_number, client_number, balance, date_created, creation_date, minimum_balance):
        """
        Initialize SavingsAccount.

        Args:
            account_number (int): Unique account number.
            client_number (int): Owner client number.
            balance (float): Initial balance.
            creation_date (date): Account creation date.
            minimum_balance (float): Required minimum balance.
        """
        super().__init__(account_number, client_number, balance, date_created)
        self.creation_date = creation_date
        self.__minimum_balance = float(minimum_balance)
        self.__service_strategy = MinimumBalanceStrategy(minimum_balance=self.__minimum_balance, service_charge_premium=0.50)

        self.creation_date = date_created

    @property
    def minimum_balance(self) -> float:
        """Return the minimum balance for this savings account."""
        return self.__minimum_balance
    
    def get_service_charges(self) -> float:
        """
        Delegate service charge calculation to strategy.

        Returns:
            float: Calculated service charge amount.
        """
        return self.__service_strategy.calculate_service_charges(self)

    def apply_interest(self):
        """
        Apply interest for savings account; default implementation returns 0.0 for assignment tests.
        """
        return 0.0

    def debit(self, amount: float):
        """
        Withdraw money from the savings account.

        Args:
            amount (float): Amount to withdraw.

        Raises:
            ValueError: If amount is invalid or insufficient funds.
        """
        if amount <= 0:
            raise ValueError("Debit amount must be positive.")
        if amount > self.balance:
            raise ValueError("Insufficient funds.")
        self.update_balance(-amount)
        self._post_transaction_checks(amount)

    def account_info(self) -> str:
        """Return descriptive information about this account."""
        return (
            f"Account Number: {self.account_number}\n"
            f"Balance: ${self.balance:.2f}\n"
            f"Creation Date: {self.creation_date}\n"
            f"Minimum Balance: ${self.__minimum_balance:.2f}"
        )

    def __str__(self) -> str:
        """Return a formatted string for the savings account."""
        return (
            f"Account Number: {self.account_number}\n"
            f"Client Number: {self.client_number}\n"
            f"Balance: ${self.balance:.2f}\n"
            f"Creation Date: {self.creation_date}\n"
            f"Minimum Balance: ${self.minimum_balance:.2f}"
        )
