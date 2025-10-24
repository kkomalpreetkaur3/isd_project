"""
Description: A client program written to verify correctness of 
the BankAccount sub classes.
"""
__author__ = "Komalpreet Kaur"
__version__ = "1.0.0"
__credits__ = ""

# 1.  Import all BankAccount types using the bank_account package
#     Import date from datetime
from datetime import date
from bank_account.chequing_account import ChequingAccount
from bank_account.savings_account import SavingsAccount
from bank_account.investment_account import InvestmentAccount

# 2. Create an instance of a ChequingAccount with values of your 
# choice including a balance which is below the overdraft limit.
chequing_account_example = ChequingAccount(
    account_number=10001, 
    client_number=1, 
    balance=-600.00,
    minimum_balance=0.0,
    overdraft_limit=-500.00
)


# 3. Print the ChequingAccount created in step 2.
print("Chequing Account Details (Initial):")
print(chequing_account_example)
# 3b. Print the service charges amount if calculated based on the 
print("Service Charges:", chequing_account_example.get_service_charges())
# current state of the ChequingAccount created in step 2.


# 4a. Use ChequingAccount instance created in step 2 to deposit 
chequing_account_example.deposit(2000.00)
# enough money into the chequing account to avoid overdraft fees.
# 4b. Print the ChequingAccount
print("Chequing Account Details (After Deposit):")
print(chequing_account_example)
# 4c. Print the service charges amount if calculated based on the 
print("Service Charges:", chequing_account_example.get_service_charges())
# current state of the ChequingAccount created in step 2.


print("===================================================")
# 5. Create an instance of a SavingsAccount with values of your 
savings_account_example = SavingsAccount(
    account_number=20001, 
    client_number=1,
    balance=500.00, 
    creation_date=date.today(), 
    minimum_balance=200.00
)
# choice including a balance which is above the minimum balance.


# 6. Print the SavingsAccount created in step 5.
print("Savings Account Details (Initial):")
print(savings_account_example)
# 6b. Print the service charges amount if calculated based on the 
print("Service Charges:", savings_account_example.get_service_charges())
# current state of the SavingsAccount created in step 5.


# 7a. Use this SavingsAccount instance created in step 5 to withdraw 
savings_account_example.debit(400.00)
# enough money from the savings account to cause the balance to fall 
# below the minimum balance.
# 7b. Print the SavingsAccount.
print("Savings Account Details (After Withdrawal):")
print(savings_account_example)
# 7c. Print the service charges amount if calculated based on the 
print("Service Charges:", savings_account_example.get_service_charges())
# current state of the SavingsAccount created in step 5.



print("===================================================")
# 8. Create an instance of an InvestmentAccount with values of your 
investment_account_recent = InvestmentAccount(
    account_number=30001, 
    client_number=3, 
    balance=10000.00,
    opened_date=date(2020, 5, 10)
)
# choice including a date created within the last 10 years.


# 9a. Print the InvestmentAccount created in step 8.
print("Investment Account (Recent) Details:")
print(investment_account_recent)
# 9b. Print the service charges amount if calculated based on the 
print("Service Charges:", investment_account_recent.get_service_charges())
# current state of the InvestmentAccount created in step 8.


# 10. Create an instance of an InvestmentAccount with values of your 
investment_account_old = InvestmentAccount(
    account_number=30002, 
    client_number=4, 
    balance=20000.00, 
    interest_rate=3.0,
    opened_date=date(2000, 8, 15)
)
# choice including a date created prior to 10 years ago.


# 11a. Print the InvestmentAccount created in step 10.
print("Investment Account (Old) Details:")
print(investment_account_old)
# 11b. Print the service charges amount if calculated based on the 
print("Service Charges:", investment_account_old.get_service_charges())
# current state of the InvestmentAccount created in step 10.


print("===================================================")

# 12. Update the balance of each account created in steps 2, 5, 8 and 10 
# by using the withdraw method of the superclass and withdrawing 
# the service charges determined by each instance invoking the 
# polymorphic get_service_charges method.
for bank_account_instance in [
    chequing_account_example,
    savings_account_example,
    investment_account_recent,
    investment_account_old
]:
    charges_amount = bank_account_instance.get_service_charges()
    try:
        bank_account_instance.debit(charges_amount)
    except Exception as exception_message:
        print(f"Could not withdraw charges from account {bank_account_instance.account_number}: {exception_message}")



# 13. Print each of the bank account objects created in steps 2, 5, 8 and 10.
print("Chequing Account Details (After Service Charges):")
print(chequing_account_example)
print("Savings Accounts Details (After Service Charges):")
print(savings_account_example)
print("Investment Account (Recent) Details (After Service Charges):")
print(investment_account_recent)
print("Investment Account (Old) Details (After Service Charges):")
print(investment_account_old)
