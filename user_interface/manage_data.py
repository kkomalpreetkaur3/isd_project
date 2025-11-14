__author__ = "Komalpreet Kaur"
__version__ = "1.0.0"
__credits__ = ""

import os
import sys
sys.path.append(os.path.dirname(os.path.dirname(__file__)))

import csv
from datetime import datetime
import logging

from bank_account.chequing_account import ChequingAccount
from bank_account.savings_account import SavingsAccount
from bank_account.investment_account import InvestmentAccount
from client.client import Client
from bank_account.bank_account import BankAccount

# *******************************************************************************
# GIVEN LOGGING AND FILE ACCESS CODE
 
# Absolute path to root of directory
root_dir = os.path.dirname(os.path.dirname(__file__))
 
# Path to the log directory relative to the root directory
log_dir = os.path.join(root_dir, 'logs')
 
# Create the log directory if it doesn't exist
os.makedirs(log_dir, exist_ok = True)
 
# Specify the path to the log file within the log directory
log_file_path = os.path.join(log_dir, 'manage_data.log')
 
# Configure logging to use the specified log file
logging.basicConfig(filename=log_file_path, filemode='a',
                    format='%(name)s - %(levelname)s - %(message)s\n\n')
 
# Given File Path Code:
# Designed to locate the input files without providing any directory structure

# Construct the absolute path to the data directory at the root of the project
data_dir = os.path.join(root_dir, 'data')
 
# Construct the absolute paths to the data files
clients_csv_path = os.path.join(data_dir, 'clients.csv')
accounts_csv_path = os.path.join(data_dir, 'accounts.csv')
 
# END GIVEN LOGGING AND FILE ACCESS CODE
# *******************************************************************************

def load_data()->tuple[dict,dict]:
    """
    Populates a client dictionary and an account dictionary with 
    corresponding data from files within the data directory.
    Returns:
        tuple containing client dictionary and account dictionary.
    """
    client_listing = {}
    accounts = {}

    # READ CLIENT DATA 
    with open(clients_csv_path, newline='') as csvfile:
        reader = csv.DictReader(csvfile)

        for row in reader:
            try:
                client_number = int(row["client_number"])
                first_name = row["first_name"]
                last_name = row["last_name"]
                email = row["email_address"]

                # Handle missing names (like client 1011)
                if not first_name or not last_name:
                    logging.error(f"Missing name in clients.csv row: {row}")
                    continue

                client_listing[client_number] = Client(
                    client_number,
                    first_name,
                    last_name,
                    email
                )

            except ValueError:
                logging.error(f"Invalid client_number in row: {row}")
                continue

    # READ ACCOUNT DATA
    with open(accounts_csv_path, newline='') as csvfile:
        reader = csv.DictReader(csvfile)  

        for row in reader:
            try:
                account_number = int(row["account_number"])
                client_number = int(row["client_number"])

                # Skip rows where client does not exist
                if client_number not in client_listing:
                    logging.error(f"Account with client_number not found: {row}")
                    continue

                # Validate balance
                try:
                    balance = float(row["balance"])
                except ValueError:
                    logging.error(f"Invalid balance: {row}")
                    continue

                # Validate date
                try:
                    date_created = datetime.strptime(row["date_created"], "%Y-%m-%d")
                except ValueError:
                    logging.error(f"Invalid date format: {row}")
                    continue

                account_type = row["account_type"]

                # Create account object
                if account_type == "ChequingAccount":
                    account = ChequingAccount(
                        account_number,
                        client_number,
                        balance,
                        date_created,
                        float(row["overdraft_limit"]),
                        float(row["overdraft_rate"])
                    )

                elif account_type == "SavingsAccount":
                    account = SavingsAccount(
                        account_number,
                        client_number,
                        balance,
                        date_created,
                        float(row["minimum_balance"])
                    )

                elif account_type == "InvestmentAccount":
                    account = InvestmentAccount(
                        account_number,
                        client_number,
                        balance,
                        date_created,
                        float(row["management_fee"])
                    )
                
                else:
                    logging.error(f"Invalid account type: {row}")
                    continue

                accounts[account_number] = account

            except Exception as e:
                logging.error(f"Error parsing account row {row}: {e}")
                continue

    return client_listing, accounts
    
def update_data(updated_account: BankAccount) -> None:
    """
    A function to update the accounts.csv file with balance 
    data provided in the BankAccount argument.
    Args:
        updated_account (BankAccount): A bank account containing an updated balance.
    """
    updated_rows = []

    with open(accounts_csv_path, mode='r', newline='') as file:
        reader = csv.DictReader(file)
        fields = reader.fieldnames
        
        for row in reader:
            account_number = int(row['account_number'])
            # Check if the account number is in the dictionary
            if account_number == updated_account.account_number:
                # Update the balance column with the new balance from the dictionary
                row['balance'] = updated_account.balance
            updated_rows.append(row)

    # Write the updated data back to the CSV
    with open(accounts_csv_path, mode='w', newline='') as file:
        writer = csv.DictWriter(file, fieldnames=fields)
        writer.writeheader()
        writer.writerows(updated_rows)


# GIVEN TESTING SECTION:
if __name__ == "__main__":
    clients,accounts = load_data()

    print("=========================================")
    for client in clients.values():
        print(client)
        print(f"{client.client_number} Accounts\n=============")
        for account in accounts.values():
            if account.client_number == client.client_number:
                print(f"{account}\n")
        print("=========================================")