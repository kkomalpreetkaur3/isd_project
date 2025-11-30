"""
Description: Provides the ClientLookupWindow class for searching clients and displaying
their bank accounts, including filtering functionality.
"""
__author__ = "Komalpreet Kaur"
__version__ = "1.0.0"
__credits__ = ""

from PySide6.QtWidgets import QTableWidgetItem, QMessageBox
from PySide6.QtCore import Qt

from ui_superclasses.lookup_window import LookupWindow
from user_interface.account_details_window import AccountDetailsWindow
from user_interface.manage_data import load_data, update_data
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
    Added Filtering for Assignment 5:
        - Apply Filter
        - Reset Filter
        - Toggle UI state
        - Exact-match filtering using setRowHidden()
    """

    def __init__(self):
        """
        Initialize the ClientLookupWindow, load data, and wire event handlers.
        """
        super().__init__()

        # Load dictionaries
        self.clients, self.accounts = load_data()

        # Connect Lookup button
        self.lookup_button.clicked.connect(self.on_lookup_client)

        # Connect double-click on account table
        self.account_table.cellDoubleClicked.connect(self.on_select_account)

        # Detect typing in client number
        self.client_number_edit.textChanged.connect(self.on_text_changed)

        # Connect Filter button
        self.filter_button.clicked.connect(self.on_filter_clicked)

        # Filtering widgets start disabled
        self.toggle_filter(False)

    # ============================================================
    # TEXT CHANGE - CLEAR DISPLAY
    # ============================================================
    def on_text_changed(self):
        """
        Clear everything when user edits client number.
        """
        self.client_info_label.setText("")
        self.account_table.setRowCount(0)
        self.toggle_filter(False)

    # ============================================================
    # LOOKUP CLIENT — POPULATE TABLE
    # ============================================================
    def on_lookup_client(self):
        """Retrieve a client and display all of their accounts."""
        try:
            client_number = int(self.client_number_edit.text())
        except ValueError:
            QMessageBox.warning(self, "Invalid Input",
                                "Client number must contain digits only.")
            return

        if client_number not in self.clients:
            QMessageBox.information(self, "Not Found",
                                    "Client number does not exist.")
            return

        # Show client info
        client = self.clients[client_number]
        self.client_info_label.setText(
            f"{client.first_name} {client.last_name} | {client.email_address}"
        )

        # Collect accounts
        client_accounts = [
            acc for acc in self.accounts.values()
            if acc.client_number == client_number
        ]

        # Fill table
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

        # enable filtering again
        self.toggle_filter(False)

    # ============================================================
    # FILTER BUTTON CLICKED
    # ============================================================
    def on_filter_clicked(self):
        """
        Applies or resets filtering based on the filter_button text.
        """
        # Case 1 → Button says "Apply Filter"
        if self.filter_button.text() == "Apply Filter":
            column_index = self.filter_combo_box.currentIndex()
            search_text = self.filter_edit.text().strip()

            # Filtering Algorithm (Exact Match)
            for row in range(self.account_table.rowCount()):
                cell_value = self.account_table.item(row, column_index).text()

                if search_text == "" or cell_value != search_text:
                    self.account_table.setRowHidden(row, True)
                else:
                    self.account_table.setRowHidden(row, False)

            # Switch UI state → Filter is ON
            self.toggle_filter(True)

        else:
            # Case 2 → Button says "Reset"
            self.toggle_filter(False)

    # ============================================================
    # TOGGLE FILTERING STATE
    # ============================================================
    def toggle_filter(self, filter_on: bool):
        """
        Update the UI to indicate whether data is filtered.
        """
        self.filter_button.setEnabled(True)

        if filter_on:
            self.filter_button.setText("Reset")
            self.filter_combo_box.setEnabled(False)
            self.filter_edit.setEnabled(False)
            self.filter_label.setText("Data is Currently Filtered")
        else:
            self.filter_button.setText("Apply Filter")
            self.filter_combo_box.setEnabled(True)
            self.filter_edit.setEnabled(True)

            # Reset filter inputs
            self.filter_edit.setText("")
            self.filter_combo_box.setCurrentIndex(0)

            # Show all rows
            for row in range(self.account_table.rowCount()):
                self.account_table.setRowHidden(row, False)

            self.filter_label.setText("Data is Not Currently Filtered")

    # ============================================================
    # OPEN ACCOUNT WINDOW
    # ============================================================
    def on_select_account(self, row, col):
        """Opens the account details dialog for the selected account."""
        account_number = int(self.account_table.item(row, 0).text())
        account = self.accounts[account_number]

        self.details_window = AccountDetailsWindow(account)
        self.details_window.balance_updated.connect(self.on_account_updated)
        self.details_window.exec()

    # ============================================================
    # ACCOUNT UPDATED SIGNAL
    # ============================================================
    def on_account_updated(self, updated_account: BankAccount):
        """Update CSV and refresh table."""
        update_data(updated_account)
        self.accounts[updated_account.account_number] = updated_account
        self.on_lookup_client()