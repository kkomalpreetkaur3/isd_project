__author__ = "ACE Faculty"
__version__ = "1.0.0"
__credits__ = ""

from ui_superclasses.details_window import DetailsWindow
from PySide6.QtWidgets import QMessageBox
from PySide6.QtCore import Signal
from bank_account.bank_account import BankAccount
import copy

class AccountDetailsWindow(DetailsWindow):
    """
    A class used to display account details and perform bank account transactions.
    """

    # Custom signal emitted when the user exits the window
    balance_updated = Signal(BankAccount)

    def __init__(self, account: BankAccount) -> None:
        """
        Initializes a new instance of the ExtendedAccountDetails window.
        Args:
            account: The bank account to be displayed.
        Returns:
            None
        """
        super().__init__()

        # Store original + working copy
        self.original_account = account
        self.account = copy.deepcopy(account)

        # Display account number and current balance
        self.account_number_label.setText(str(self.account.account_number))
        self.balance_label.setText(str(self.account.balance))

        # Connect UI buttons to event handlers
        self.deposit_button.clicked.connect(self.on_deposit)
        self.withdraw_button.clicked.connect(self.on_withdraw)
        self.exit_button.clicked.connect(self.on_exit)

    # ============================================================
    # EVENT HANDLER: DEPOSIT
    # ============================================================
    def on_deposit(self):
        """
        Deposits the entered amount into the BankAccount.

        Returns:
            None
        """
        try:
            amount = float(self.transaction_amount_edit.text())
        except ValueError:
            QMessageBox.warning(self, "Invalid Input",
                                "Transaction amount must be numeric.")
            return
        
        if amount <= 0:
            QMessageBox.warning(self, "Invalid Input",
                                "Deposit amount must be positive.")
            return

        self.account.deposit(amount)
        self.balance_label.setText(str(self.account.balance))

    # ============================================================
    # EVENT HANDLER: WITHDRAW
    # ============================================================
    def on_withdraw(self):
        """
        Attempts to withdraw the entered amount.
        Displays an error if the account's withdraw rules do not permit it.

        Returns:
            None
        """
        try:
            amount = float(self.transaction_amount_edit.text())
        except ValueError:
            QMessageBox.warning(self, "Invalid Input",
                                "Transaction amount must be numeric.")
            return
        
        if not self.account.withdraw(amount):
            QMessageBox.warning(self, "Withdrawal Denied",
                                "This withdrawal violates account rules.")
            return

        self.balance_label.setText(str(self.account.balance))

    # ============================================================
    # EVENT HANDLER: EXIT BUTTON CLICKED
    # ============================================================
    def on_exit(self):
        """
        Emits the balance_updated signal so that the Lookup Window
        can update both the CSV file and the displayed table.

        Returns:
            None
        """
        self.balance_updated.emit(self.account)
        self.close()
