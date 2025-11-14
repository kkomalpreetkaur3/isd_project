"""
Description: Provides the ClientLookupWindow class for searching clients and displaying
their bank accounts. Handles user interactions and opens the
AccountDetailsWindow for selected accounts.
"""
__author__ = "Komalpreet Kaur"
__version__ = "1.0.0"
__credits__ = ""

from PySide6.QtWidgets import QTableWidgetItem, QMessageBox
from PySide6.QtCore import Qt

from ui_superclasses.lookup_window import LookupWindow
from user_interface.account_details_window import AccountDetailsWindow
from user_interface.manage_data import load_data
from user_interface.manage_data import update_data
from bank_account.bank_account import BankAccount

class ClientLookupWindow(LookupWindow):
    """
    A class used to retrieve and display Client and BankAccount
    information. This class extends the LookupWindow superclass,
    which provides the UI layout and widgets.

    ClientLookupWindow adds:
        - Event handling logic
        - Retrieving Client data
        - Populating the account table
        - Opening the AccountDetailsWindow on selection
        - Receiving updated balances via signals
    """

    def __init__(self):
        """
        Initializes the Client Lookup window.

        Loads client/account data and connects UI widgets
        to event handler functions (lookup button, table selection,
        and text-changed event).
        """
        super().__init__()

        # Load dictionaries from manage_data.py
        self.clients, self.accounts = load_data()

        # Connect Lookup button to event handler
        self.lookup_button.clicked.connect(self.on_lookup_client)

        # Connect double-click on account table to account selection handler
        self.account_table.cellDoubleClicked.connect(self.on_select_account)

        # Clear table whenever text changes
        self.client_number_edit.textChanged.connect(self.on_text_changed)

    # ============================================================
    # EVENT HANDLER: TEXT CHANGED
    # ============================================================
    def on_text_changed(self):
        """
        Clears client info label and removes all rows from the
        account table whenever the user edits the client number.
        """
        self.client_info_label.setText("")
        self.account_table.setRowCount(0)

        # Disable filter controls
        self.filter_label.setEnabled(False)
        self.filter_edit.setEnabled(False)
        self.filter_button.setEnabled(False)

    # ============================================================
    # EVENT HANDLER: LOOKUP BUTTON PRESSED
    # ============================================================
    def on_lookup_client(self):
        """
        Retrieves a Client object using the number typed
        by the user. If the client exists, their full name and email
        are displayed, along with all associated accounts.

        Returns:
            None
        """
        try:
            client_number = int(self.client_number_edit.text())
        except ValueError:
            QMessageBox.warning(self, "Invalid Input",
                                "Client number must contain digits only.")
            return
        
        # Ensure client exists
        if client_number not in self.clients:
            QMessageBox.information(self, "Not Found",
                                    "Client number does not exist.")
            return

        # Display client info
        client = self.clients[client_number]
        self.client_info_label.setText(
            f"{client.first_name} {client.last_name} | {client.email_address}"
        )

        # Gather accounts for the selected client
        client_accounts = [
            acc for acc in self.accounts.values()
            if acc.client_number == client_number
        ]

        # Populate the account table
        self.account_table.setRowCount(len(client_accounts))

        for row_index, account in enumerate(client_accounts):
            self.account_table.setItem(row_index, 0,
                                       QTableWidgetItem(str(account.account_number)))
            self.account_table.setItem(row_index, 1,
                                       QTableWidgetItem(str(account.balance)))
            self.account_table.setItem(row_index, 2,
                                       QTableWidgetItem(str(account.date_created)))
            self.account_table.setItem(row_index, 3,
                                       QTableWidgetItem(account.__class__.__name__))
            
        # Enable filter controls
        self.filter_label.setEnabled(True)
        self.filter_edit.setEnabled(True)
        self.filter_button.setEnabled(True)

    # ============================================================
    # EVENT HANDLER: USER DOUBLE-CLICKS A ROW
    # ============================================================
    def on_select_account(self, row, col):
        """
        Opens the AccountDetailsWindow for the selected BankAccount
        when the user double-clicks on a table row.

        Args:
            row: The table row the user clicked.
            col: The table column (unused).

        Returns:
            None
        """
        account_number = int(self.account_table.item(row, 0).text())
        account = self.accounts[account_number]

        # Create and display the AccountDetailsWindow
        self.details_window = AccountDetailsWindow(account)

        # Connect custom signal to refresh table when balance changes
        self.details_window.balance_updated.connect(self.on_account_updated)

        # Display as modal window
        self.details_window.exec()

    # ============================================================
    # EVENT HANDLER: SIGNAL — ACCOUNT UPDATED
    # ============================================================
    def on_account_updated(self, updated_account: BankAccount):
        """
        Triggered when AccountDetailsWindow emits the balance_updated signal.
        Updates accounts.csv THEN refreshes the account table.

        Args:
            updated_account (BankAccount): The modified account object.

        Returns:
            None
        """
        # Update CSV file
        update_data(updated_account)

        # Update in-memory dictionary
        self.accounts[updated_account.account_number] = updated_account

        # Refresh the table display
        self.on_lookup_client()
        
