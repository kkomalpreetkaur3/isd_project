# chequing_account.py
"""
Description:
Represents a chequing account with minimum balance and service charges.
Uses the OverdraftStrategy for service charge calculation.
"""

__author__ = "Komalpreet Kaur"
__version__ = "1.0.0"

from bank_account.bank_account import BankAccount 
from patterns.strategy.overdraft_strategy import OverdraftStrategy

class ChequingAccount(BankAccount):
    """
    ChequingAccount extends BankAccount and includes minimum_balance enforcement.
    This class delegates service charge calculation to OverdraftStrategy.
    """

    def __init__(self, account_number: int, client_number: int, balance: float, minimum_balance: float = 0.0, overdraft_limit=None):
        """
        Initialize ChequingAccount.

        Args:
            account_number (int): Unique account number.
            client_number (int): Owner client number.
            balance (float): Initial balance.
            minimum_balance (float): Minimum required balance.
        """
        super().__init__(account_number, client_number, balance)
        self.minimum_balance = float(minimum_balance)
        self.__service_strategy = OverdraftStrategy(overdraft_penalty=0.50)
        self.overdraft_limit = overdraft_limit

    def account_info(self) -> str:
        """
        Return account information string.
        """
        return f"Account Number: {self.account_number}\nClient Number: {self.client_number}\nBalance: ${self.balance:.2f}"

    def apply_interest(self):
        """
        Chequing accounts do not earn interest by default.
        """
        pass

    def debit(self, amount: float):
        """
        Debit (withdraw) an amount from the account if minimum balance remains satisfied.

        Args:
            amount (float): Amount to withdraw.

        Raises:
            ValueError: If amount is invalid or minimum balance would be violated.
        """
        if amount <= 0:
            raise ValueError("Debit amount must be positive.")
        if self.balance - amount < self.minimum_balance:
            raise ValueError("Cannot withdraw beyond minimum balance.")
        self.update_balance(-amount)
        self._post_transaction_checks(amount)

    def deposit(self, amount: float):
        """
        Deposit an amount and run notification checks.

        Args:
            amount (float): Amount to deposit.

        Raises:
            ValueError: If amount is not positive.
        """
        if amount <= 0:
            raise ValueError("Deposit amount must be positive.")
        self.update_balance(amount)
        self._post_transaction_checks(amount)

    def get_service_charges(self) -> float:
        """
        Delegate calculation to the configured strategy.

        Returns:
            float: Calculated service charge amount.
        """
        return self.__service_strategy.calculate_service_charges(self)

    def __str__(self) -> str:
        """Return a formatted string for the chequing account."""
        return (
            f"Account Number: {self.account_number}\n"
            f"Client Number: {self.client_number}\n"
            f"Balance: ${self.balance:.2f}\n"
            f"Minimum Balance: ${self.minimum_balance:.2f}"
        )
