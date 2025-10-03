"""
Description: Unit tests for the BankAccount class.
Author: ACE Faculty
Usage: To execute all tests in the terminal execute 
the following command:
    python -m unittest tests/test_bank_account.py
"""

__author__ = "Komalpreet Kaur"
__version__ = "1.0.0"

import unittest
from bank_account.chequing_account import ChequingAccount
from datetime import date


class TestBankAccount(unittest.TestCase):
    """Test cases for BankAccount."""

    def test_attributes_set_to_input_values(self):
        """Attributes are set correctly for initialisation."""
        account = ChequingAccount(40075, 2828, 640.00, minimum_balance=100.00)
        self.assertEqual(account.account_number, 40075)
        self.assertEqual(account.client_number, 2828)
        self.assertEqual(account.balance, 640.00)
        self.assertEqual(account.minimum_balance, 100.00)

    def test_balance_update(self):
        """Update balance increases correctly."""
        account = ChequingAccount(40075, 2828, 100.00, minimum_balance=100.00)
        account.update_balance(50.00)
        self.assertEqual(account.balance, 150.0)
        account.update_balance(-20.0)
        self.assertEqual(account.balance, 130.0)

    def test_deposit_valid(self):
        """Depositing positive amount works."""
        account = ChequingAccount(40075, 2828, 200.00, minimum_balance=100.00)
        account.deposit(50.00)
        self.assertEqual(account.balance, 250)

    def test_deposit_negative_raises(self):
        """Depositing negative amount raises ValueError."""
        account = ChequingAccount(40075, 2828, 200.00, minimum_balance=100.00)
        with self.assertRaises(ValueError):
            account.deposit(-50.0)

    def test_withdraw_valid(self):
        """Withdrawing valid amount decreases balance."""
        account = ChequingAccount(40075, 2828, 200.00, minimum_balance=100.00)
        account.withdraw(50.0)
        self.assertEqual(account.balance, 150.0)

    def test_withdraw_exceed_balance_raises(self):
        """Withdrawing more than balance raises ValueError."""
        account = ChequingAccount(40075, 2828, 100.00, minimum_balance=100.00)
        with self.assertRaises(ValueError):
            account.withdraw(200.00)

    def test_str_method(self):
        """__str__ returns expected string representation."""
        account = ChequingAccount(40075, 2828, 200.00, minimum_balance=100.00)
        expected = (
            "Account Number: 40075\n"
            "Client Number: 2828\n"
            "Balance: $200.00"
            "Minimum Balance: $100.00"
        )
        self.assertEqual(str(account), expected)


if __name__ == "__main__":
    unittest.main()