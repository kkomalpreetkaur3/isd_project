"""
Dscription: Represents a chequing account with minimum balance and service charges.
Uses the OverdraftStrategy for service charge calculation.
"""

__author__ = "Komalpreet Kaur"
__version__ = "1.0.0"

from bank_account import BankAccount
from patterns.strategy.overdraft_strategy import OverdraftStrategy

class ChequingAccount(BankAccount):
    """
    Represents a chequing account with minimum balance and service charges.
    Inherits from BankAccount and implements abstract methods.
    This class delegates service charge calculation to OverdraftStrategy.
    """

    def __init__(self, account_number: int, client_number: int, balance: float, overdraft_limit=None, minimum_balance: float = 0.0):
                super().__init__(account_number, client_number, balance)
                self.overdraft_limit = overdraft_limit
                self.minimum_balance = float(minimum_balance)
                self.__service_strategy = OverdraftStrategy(overdraft_penalty=0.50)

    def account_info(self) -> str:
          """
          Returns account information as a string.
          """
          return f"Account Number: {self.account_number}\nClient Number: {self.client_number}\nBalance: ${self.balance:.2f}"
    
    def apply_interest(self):
           """
           Chequing accounts do not earn interest.
           """
           pass
    
    def debit(self, amount: float):
           """
           Withdraws money from the account, ensuring minimum balance is maintained.
           """
           if amount < 0:
                  raise ValueError("Debit amount must be positive")
           if self.balance - amount < self.minimum_balance:
                  raise ValueError("Cannot withdraw beyond minimum balance")
           self.update_balance(-amount)
           self._post_transaction_checks(amount)

    def deposit(self, amount: float):
           """
           Deposits money into the account.
           """
           if amount < 0:
                  raise ValueError("Deposits amount must be positive")
           self.update_balance(amount)
           self._post_transaction_checks(amount)

    def get_service_charges(self) -> float:
       """
       Delegate calculation to the configured strategy.
       """
       return self.__service_strategy.calculate_service_charges(self)
    
    def __str__(self) -> str:
       return (
             f"Account Number: {self.account_number}\n"
             f"Client Number: {self.client_number}\n"
             f"Balance: ${self.balance:.2f}\n"
             f"Minimum Balance: ${self.minimum_balance:.2f}"
       )