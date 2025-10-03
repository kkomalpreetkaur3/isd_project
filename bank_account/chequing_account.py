"""
Dscription: Represents a chequing account with service charges.
"""

__author__ = "Komalpreet Kaur"
__version__ = "1.0.0"

from bank_account.bank_account import BankAccount

class ChequingAccount(BankAccount):
    """
    Represents a chequing account with minimum balance and service charges.
    Inherits from BankAccount and implements abstract methods.
    """

    def __init__(self, account_number, client_number, balance, minimum_balance=0.0):
                super().__init__(account_number, client_number, balance)
                self.minimum_balance = minimum_balance

    def account_info(self):
          """
          Returns account information as a string.
          """
          return f"Account Number: {self.account_number}\nClient Number: {self.client_number}\nBalance: ${self.balance:.2f}"
    
    def apply_interest(self):
           """
           Chequing accounts do not earn interest.
           """
           pass
    
    def debit(self, amount):
           """
           Withdraws money from the account, ensuring minimum balance is maintained.
           """
           if amount < 0:
                  raise ValueError("Debit amount must be positive")
           if self.balance - amount < self.minimum_balance:
                  raise ValueError("Cannot withdraw beyond minimum balance")
           self.update_balance(-amount)

    def deposit(self, amount):
           """
           Deposits money into the account.
           """
           if amount < 0:
                  raise ValueError("Deposits amount must be positive")
           self.update_balance(amount)

    def get_service_charges(self):
        if self.balance >= self.minimum_balance:
            return 0.50  
        else:
            return 1.00 
    
    def __str__(self):
        return (f"Account Number: {self.account_number}\n"
                f"Client Number: {self.client_number}\n"
                f"Balance: ${self.balance:.2f}"
                f"Minimum Balance: ${self.minimum_balance:.2f}")
    