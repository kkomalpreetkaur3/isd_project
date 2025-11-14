"""
Description: This represents bank account with validation for account number, client number and balance.
Refactored to act as Subject in Observer Pattern and to provide hooks for Strategy Pattern.
"""

__author__ = "Komalpreet Kaur"
__version__ = "1.0.0"

from abc import ABC, abstractmethod
from patterns.observer.subject import Subject
class BankAccount(Subject, ABC):
    """
    Generic bank account class. Inherits Subject first to support observer behaviour.

    Attributes:
        LOW_BALANCE_LEVEL (float): Threshold below which a low balance notification is sent.
        LARGE_TRANSACTION_THRESHOLD (float): Absolute transaction amount that triggers a large-transaction notification.
    """

    LOW_BALANCE_LEVEL = 25.00
    LARGE_TRANSACTION_THRESHOLD = 10000.00

    def __init__(self, account_number: int, client_number: int, balance: float, date_created=None):
        """
        Initialize a BankAccount instance.

        Args:
            account_number (int): Unique account number.
            client_number (int): Client identifier.
            balance (float): Initial balance.

        Raises:
            ValueError: If account_number or client_number is not an integer.
        """
        super().__init__()
        if isinstance(account_number, int):
            self.__account_number = account_number
        else:
            raise ValueError("Account number must be an integer.")
    
        if isinstance(client_number, int):
            self.__client_number = client_number
        else:
            raise ValueError("Client number must be an integer.")
        
        try:
            self.__balance = float(balance)
        except (ValueError, TypeError):
            self.__balance = 0.0

        self.date_created = date_created

    @property
    def account_number(self) -> int:
        """Return the account number."""
        return self.__account_number

    @property
    def client_number(self) -> int:
        """Return the client number associated with this account."""
        return self.__client_number
    
    @property
    def balance(self) -> float:
        """Return the current account balance."""
        return self.__balance
    
    def _post_transaction_checks(self, transaction_amount: float):
        """
        Check for conditions that should trigger observer notifications.

        Sends notifications for low balance and for large absolute transactions.

        Args:
            transaction_amount (float): The amount of the transaction (positive for deposit, positive for withdraw amount).
        """
        if self.__balance < self.LOW_BALANCE_LEVEL:
            message = f"Low balance warning ${self.__balance:.2f}: on account {self.__account_number}."
            self.notify(message)

        if abs(transaction_amount) > self.LARGE_TRANSACTION_THRESHOLD:
            message = f"Large transaction ${transaction_amount:.2f}: on account {self.__account_number}."
            self.notify(message)
    
    def update_balance(self, amount: float):
        """Update the account balance by the specified amount.

        This method is robust to non-numeric input and will ignore invalid updates.

        Args:
            amount (float): Amount to add (deposit) or subtract (withdraw).
        """
        try:
            amount_converted = float(amount)
            self.__balance = self.__balance + amount_converted  
        except (ValueError, TypeError):
            pass

    def deposit(self, amount: float):
        """
        Deposit a positive amount to the account and run notification checks.

        Args:
            amount (float): Amount to deposit.

        Raises:
            ValueError: If amount is not numeric or not positive.
        """
        if not isinstance(amount, (int, float)):
            raise ValueError(f"Deposit amount: {amount} must be numeric.")
        if amount <= 0:
            raise ValueError(f"Deposit amount: ${amount:,.2f} must be positive.")
        
        self.update_balance(amount)
        self._post_transaction_checks(amount)

    def withdraw(self, amount: float):
        """
        Withdraw a positive amount from the account and run notification checks.

        Args:
            amount (float): Amount to withdraw.

        Raises:
            ValueError: If amount is not numeric, not positive, or exceeds balance.
        """
        if not isinstance(amount, (int, float)):
            raise ValueError(f"Withdraw amount: {amount} must be numeric.")
        if amount <= 0:
            raise ValueError(f"Withdraw amount: ${amount:,.2f} must be positive.")
        if amount > self.__balance:
            raise ValueError(f"Withdraw amount: ${amount:,.2f} must not exceed the account balance: ${self.__balance:,.2f}.")
        
        self.update_balance(-amount)
        self._post_transaction_checks(amount)

    @abstractmethod
    def debit(self, amount: float) -> bool:
        """Abstract method to debit the account.

        Args:
            amount (float): Amount to debit.

        Returns:
            bool: True if the debit was successful, otherwise False.
        """
        pass

    @abstractmethod
    def apply_interest(self):
        """Abstract method to apply interest to the account balance."""
        pass

    @abstractmethod
    def account_info(self) -> str:
        """Return a string containing account information."""
        pass

    def __str__(self):
        """Return a string representation of the account."""
        return(
            f"Account Number: {self.__account_number}\n"
            f"Client Number: {self.__client_number}\n"
            f"Balance: ${self.__balance:,.2f}"
        )
    

        