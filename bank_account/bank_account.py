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
    """

    LOW_BALANCE_LEVEL = 25.00
    LARGE_TRANSACTION_THRESHOLD = 10000.00

    def __init__(self, account_number: int, client_number: int, balance: float):
        super().__init__()
        """
        Initialises a bank account.
        Args:
            account_number (int): Unique account number
            client_number (int): Client identifier
            balance (float): Initial account balance

        Raises:
            ValueError: If account_number or client_number is not an integer.
        """
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

    @property
    def account_number(self) -> int:
        return self.__account_number

    @property
    def client_number(self) -> int:
        return self.__client_number
    
    @property
    def balance(self) -> float:
        return self.__balance
    
    def _post_transaction_checks(self, transaction_amount: float):
        """
        After a deposit or withdrawal, notify attached observers if:
        balance has dropped below LOW_BALANCE_LEVEL
        absolute value of transaction_amount exceeds LARGE_TRANSACTION_THRESHOLD
        """
        if self.__balance < self.LOW_BALANCE_LEVEL:
            message = f"Low balance warning ${self.__balance:.2f}: on account {self.__account_number}."
            self.notify(message)

        if abs(transaction_amount) > self.LARGE_TRANSACTION_THRESHOLD:
            message = f"Large transaction ${transaction_amount:.2f}: on account {self.__account_number}."
            self.notify(message)
    
    def update_balance(self, amount: float):
        """
        Deposit a positive amount into the account and run notification checks.
        Raises ValueError on invalid input.
        """
        try:
            amount_converted = float(amount)
            self.__balance = self.__balance + amount_converted  
        except (ValueError, TypeError):
            pass

    def deposit(self, amount: float):
        """
        Deposit a positive amount from the account and runs notification checks.
        Raises ValueError on invalid input.
        """
        if not isinstance(amount, (int, float)):
            raise ValueError(f"Deposit amount: {amount} must be numeric.")
        if amount <= 0:
            raise ValueError(f"Deposit amount: ${amount:,.2f} must be positive.")
        
        self.update_balance(amount)
        self._post_transaction_checks(amount)

    def withdraw(self, amount: float):
        """
        Withdraw a positive amount from the account, with basic balance check.
        Raises ValueError on invalid input or insufficient funds.
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
        """Debit a specified amount from the account."""
        pass

    @abstractmethod
    def apply_interest(self):
        """Apply interest to the account balance."""
        pass

    @abstractmethod
    def apply_interest(self):
        """Apply interest to the account balance(abstract)."""
        pass

    @abstractmethod
    def account_info(self) -> str:
        """Return a string containing account information."""
        pass

    def __str__(self):
        return(
            f"Account Number: {self.__account_number}\n"
            f"Client Number: {self.__client_number}\n"
            f"Balance: ${self.__balance:,.2f}"
        )
    

        