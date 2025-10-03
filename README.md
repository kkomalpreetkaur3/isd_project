# Intermediate Software Development Automated Teller Project
This project will be developed over the course of several assignments.  Each assignment will build on the work done in the previous assignment(s).  Ultimately, an entire system will be created to manage bank transactions for clients who have one or more bank accounts.

## Author
Komalpreet Kaur

## Assignment
### Assignment 1: Project Setup
The main tasks included in this assignment are:
- Downloading and managing project file(isd_project)
- Initializing a Git Repository
- Creating Remote Repository in GitHub
- Adding instructor as collaborator
- Connecting Local Repository to Remote Repository
- Launching VS code
- Updating Remote Repository
- Installing email-validator

## Encapsulation

## BankAccount Class

- Private attributes: '__account_number', '__client_number', '__balance'
- Controlled access: @property decorator

## Client Class

- Private attributes: '__client_number', '__first_name', '__last_name', __email_address'
Controlled access: @property decorator

### Assignment 2:
 Added ChequingAccount, InvestmentAccount, SavingAccount classes. Created new test files and updated the project with a new client program.

## Polymorphism 
Polymorphism in this project is demonstrated through the 'BankAccount' abstract base class and its subclasses: 'ChequingAccount', 'SavingsAccount', and 'InvestmentAccount'. Each subclass inherits from 'BankAccount' and implements the abstract methods 'debit()', 'apply_interest()', and 'account_info()' in its own way. 

For example:  
- 'ChequingAccount' implements 'debit()' to enforce a minimum balance and calculates service charges differently from other accounts.  
- 'SavingsAccount' implements 'debit()' with its own minimum balance rules and has its own 'get_service_charges()' logic.  
- 'InvestmentAccount' implements 'apply_interest()' to add interest to the balance, which is not applicable to chequing or savings accounts.  
