# Intermediate Software Development Automated Teller Project
This project will be developed over the course of several assignments.  Each assignment will build on the work done in the previous assignment(s).  Ultimately, an entire system will be created to manage bank transactions for clients who have one or more bank accounts.

## Author
Komalpreet Kaur

## Assignments
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

### Assignment 3:
This assignment demonstrates the use of two Behavioral Design Patterns:  
- Strategy Pattern – used to make service charge calculations flexible and scalable.  
- Observer Pattern – used to notify clients of unusual account activity.

## Strategy Pattern
The Strategy Pattern moves service charge algorithms into separate classes so account types can delegate calculation work. This reduces code duplication and allows adding new service-charge behaviours without changing existing account classes.

- 'patterns/strategy/service_charge_strategy.py'  
  Abstract base class with 'BASE_SERVICE_CHARGE' constant and 'calculate_service_charges()' abstract method.

- 'patterns/strategy/overdraft_strategy.py'  
  Concrete strategy used by 'ChequingAccount'. Applies an overdraft penalty plus the base service charge when the balance is negative.

- 'patterns/strategy/minimum_balance_strategy.py'  
  Concrete strategy used by 'SavingsAccount'. Applies a premium when the balance is below the required minimum.

- 'patterns/strategy/management_fee_strategy.py' 
  Concrete strategy used by 'InvestmentAccount'. Applies a small proportional management fee plus the base service charge. Includes logic to reference accounts older than 10 years (TEN_YEARS_AGO constant).

Each account class ('ChequingAccount', 'SavingsAccount', 'InvestmentAccount') keeps a private instance of its service charge strategy and calls 'get_service_charges()' which delegates to the strategy object.

---

## Observer Pattern
The Observer Pattern decouples account logic from notification delivery.

- 'patterns/observer/subject.py'  
  Implements 'attach()', 'detach()', and 'notify()' for managing observers.

- 'patterns/observer/observer.py'  
  Defines the 'Observer' abstract interface (with 'update()' method).

- 'client.py' 
  Implements 'Client' as a concrete observer. 'Client.update()' uses 'utility/file_utils.simulate_send_email()' to write a simulated email to 'output/observer_emails.txt'.

- 'bank_account.py' 
  'BankAccount' now inherits from 'Subject' first, then 'ABC'. It defines constants:
  - `LOW_BALANCE_LEVEL' — triggers a low balance notification when balance falls below this level.
  - 'LARGE_TRANSACTION_THRESHOLD' — triggers a large transaction notification when the absolute transaction amount exceeds this threshold.


### Assignment 4:
GUI Client and Account Management: 
This assignment introduces the use of PySide6 to build graphical user interfaces for client lookup and account details. It expands on previous project structure by integrating new UI classes and connecting them to existing account data.

## Event-Driven Programming Paradigm

This application uses the Event-Driven Programming Paradigm as follows:

- GUI components (widgets) emit signals when interacted with (e.g., buttons clicked, table cells selected, text changed).
- Slots (methods) are connected to these signals to handle events dynamically.
- Examples:
  - `lookup_button.clicked` → `on_lookup_client()`
  - `client_number_edit.textChanged` → `on_text_changed()`
  - `account_table.cellClicked` → `on_select_account()`
  - `deposit_button.clicked` / `withdraw_button.clicked` → `on_apply_transaction()`
- The AccountDetailsWindow emits a custom `balance_updated` signal after transactions, which is received by the ClientLookupWindow to refresh account balances in real-time.
