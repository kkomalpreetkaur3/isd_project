"""
Description: This represents bank account with validation for account number, client number and balance.
Also includes ChequingAccount, SavingAccount, InvestmentAccount classes with service charge logic.
"""

__author__ = "Komalpreet Kaur"
__version__ = "1.0.0"

from abc import ABC, abstractmethod
class BankAccount(ABC):
    """Represents a generic bank account."""

    def __init__(self, account_number: int, client_number: int, balance: float):
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
    
    def update_balance(self, amount: float):
        """Update the account balance by a given amount."""
        try:
            amount = float(amount)
            self.__balance = self.__balance + amount  
        except (ValueError, TypeError):
            pass

    def deposit(self, amount: float):
        """Deposit a positive amount from the account."""
        if not isinstance(amount, (int, float)):
            raise ValueError(f"Deposit amount: {amount} must be numeric.")
        if amount <= 0:
            raise ValueError(f"Deposit amount: ${amount:,.2f} must be positive.")
        self.update_balance(amount)

    def withdraw(self, amount: float):
        """Withdraw a positive amount from the account."""
        if not isinstance(amount, (int, float)):
            raise ValueError(f"Withdraw amount: {amount} must be numeric.")
        if amount <= 0:
            raise ValueError(f"Withdraw amount: ${amount:,.2f} must be positive.")
        if amount > self.__balance:
            raise ValueError(f"Withdraw amount: ${amount:,.2f} must not exceed the account balance: ${self.__balance:,.2f}.")
        self.update_balance(-amount)

    @abstractmethod
    def debit(self, amount: float) -> bool:
        """Debit a specified amount from the account."""
        pass

    @abstractmethod
    def apply_interest(self):
        """Apply interest to the account balance."""
        pass

    @abstractmethod
    def account_info(self) -> str:
        """Return a string containing account information."""
        pass

    def __str__(self) -> str:
        return(
            f"Account Number: {self.__account_number}"
            f"\nClient Number: {self.__client_number}"
            f"\nBalance: ${self.__balance:,.2f}"
        )
    

        