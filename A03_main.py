"""
Description: A client program written to verify implementation 
of the Observer Pattern.
"""
__author__ = "Komalpreet Kaur"
__version__ = "1.0.0"
__credits__ = ""

# 1.  Import all BankAccount types using the bank_account package
#     Import date
#     Import Client
from datetime import date
from client.client import Client
from bank_account.chequing_account import ChequingAccount
from bank_account.savings_account import SavingsAccount
from bank_account.investment_account import InvestmentAccount

# 2. Create a Client object with data of your choice.
client_one = Client(1001, "Komalpreet", "Kaur", "komalpreet@example.com")

# 3a. Create a ChequingAccount object with data of your choice, using the client_number 
# of the client created in step 2.
chequing_account_one = ChequingAccount(
    account_number=2001,
    client_number=client_one.client_number,
    balance=500.0,
    minimum_balance=50.0
)

# 3b. Create a SavingsAccount object with data of your choice, using the client_number 
# of the client created in step 2.
savings_account_one = SavingsAccount(
    account_number=2002,
    client_number=client_one.client_number,
    balance=1500.0,
    creation_date=date.today(),
    interest_rate=0.02, 
    minimum_balance=500.0
)

# 4 The ChequingAccount and SavingsAccount objects are 'Subject' objects.
# The Client object is an 'Observer' object.  
# 4a.  Attach the Client object (created in step 1) to the ChequingAccount object (created in step 2).
chequing_account_one.attach(client_one)

# 4a.  Attach the Client object (created in step 1) to the SavingsAccount object (created in step 2).
savings_account_one.attach(client_one)

# 5a. Create a second Client object with data of your choice.
client_two = Client(1002, "Raman", "Kaur", "raman@example.com")

# 5b. Create a SavingsAccount object with data of your choice, using the client_number 
# of the client created in this step.
savings_account_two = SavingsAccount(
    account_number=2004,
    client_number=client_two.client_number,
    balance=200.0,
    creation_date=date.today(),
    interest_rate=0.03,
    minimum_balance=300.0
)
savings_account_two.attach(client_two)

# 6. Use the ChequingAccount and SavingsAccount objects created 
# in steps 3 and 5 above to perform transactions (deposits and withdraws) 
# which would cause the Subject (BankAccount) to notify the Observer 
# (Client) as well as transactions that would not 
# cause the Subject to notify the Observer.  Ensure each 
# BankAccount object performs at least 3 transactions.
# REMINDER: the deposit() and withdraw() methods can raise exceptions
# ensure the methods are invoked using proper exception handling such 
# that any exception messages are printed to the console.

# 6. Perform transactions
print("\n--- Performing Transactions ---")

# Transactions for client_one (ChequingAccount)
try:
    chequing_account_one.deposit(200.0)
    print(f"Deposited $200 to ChequingAccount {chequing_account_one.account_number}")
except Exception as e:
    print("Error during deposit to chequing_account_one:", e)

try:
    chequing_account_one.deposit(15000.0)
    print(f"Deposited $15000 to ChequingAccount {chequing_account_one.account_number}")
except Exception as e:
    print("Error during large deposit to chequing_account_one:", e)

try:
    chequing_account_one.withdraw(100.0)
    print(f"Withdrew $100 from ChequingAccount {chequing_account_one.account_number}")
except Exception as e:
    print("Error during withdrawal from chequing_account_one:", e)

# Transactions for client_one (SavingsAccount)
try:
    savings_account_one.withdraw(1300.0)
    print(f"Withdrew $1300 from SavingsAccount {savings_account_one.account_number}")
except Exception as e:
    print("Error during withdrawal from savings_account_one:", e)

try:
    savings_account_one.deposit(200.0)
    print(f"Deposited $200 to SavingsAccount {savings_account_one.account_number}")
except Exception as e:
    print("Error during deposit to savings_account_one:", e)

try:
    savings_account_one.withdraw(100.0)
    print(f"Withdrew $100 from SavingsAccount {savings_account_one.account_number}")
except Exception as e:
    print("Error during withdrawal from savings_account_one:", e)

# Transacction for client_two (SavingsAccount)
try:
    savings_account_two.debit(100.0)
    print(f"Deposited $100.0 to SavingsAccount {savings_account_two.account_number}")
except Exception as e:
    print("Error during deposit to savings_account_two:", e)

try:
    savings_account_two.withdraw(250.0)
    print(f"Withdrew $250 from SavingsAccount {savings_account_two.account_number}")
except Exception as e:
    print("Error during withdrawal from savings_account_two:", e)

try:
    savings_account_two.deposit(50.0)
    print(f"Deposited $50 to SavingsAccount {savings_account_two.account_number}")
except Exception as e:
    print("Error during deposit to savings_account_two:", e)

print("\n--- Transactions Completed ---")
print("Check the 'output/observer_emails.txt' file for simulated email notifications.")
