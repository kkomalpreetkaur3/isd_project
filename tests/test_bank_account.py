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
from bank_account.bank_account import BankAccount

class TestBankAccount(unittest.TestCase):

    def test_attributes_set_to_input_values(self):
        acc = BankAccount(40075, 2828, 640.00)
        self.assertEqual(40075, acc._BankAccount__account_number)
        self.assertEqual(2828, acc._BankAccount__client_number)
        self.assertEqual(640.00, acc._BankAccount__balance)

    def test_balance_defaults_to_zero_when_invalid(self):
        acc = BankAccount(40075, 2828, "beautiful")
        self.assertEqual(0.0, acc._BankAccount__balance)

    def test_non_numeric_account_number_raises(self):
        with self.assertRaises(ValueError):
            BankAccount("bad", 2828, 640.00)

    def test_non_numeric_client_number_raises(self):
        with self.assertRaises(ValueError):
            BankAccount(40075, "bad", 640.00)

    def test_return_account_number(self):
        acc = BankAccount(40075, 2828, 640.00)
        self.assertEqual(40075, acc.account_number)

    def test_return_client_number(self):
        acc = BankAccount(40075, 2828, 640.00)
        self.assertEqual(2828, acc.client_number)

    def test_return_balance(self):
        acc = BankAccount(40075, 2828, 640.00)
        self.assertEqual(640.00, acc.balance)

    def test_update_balance_positive(self):
        acc = BankAccount(40075, 2828, 140.00)
        acc.update_balance(50.00)
        self.assertEqual(190.00, acc.balance)

    def test_update_balance_negative(self):
        acc = BankAccount(40075, 2828, 90.00)
        acc.update_balance(-40.00)
        self.assertEqual(50.00, acc.balance)

    def test_update_balance_non_numeric(self):
        acc = BankAccount(40075, 2828, 200.00)
        acc.update_balance("beautiful")
        self.assertEqual(200.00, acc.balance)

    def test_deposit_valid(self):
        acc = BankAccount(40075, 2828, 200.00)
        acc.deposit(50.00)
        self.assertEqual(250.00, acc.balance)

    def test_deposit_negative_raises(self):
        acc = BankAccount(40075, 2828, 100.00)
        with self.assertRaises(ValueError):
            acc.deposit(-50.00)

    def test_withdraw_valid(self):
        acc = BankAccount(40075, 2828, 250.00)
        acc.withdraw(50.00)
        self.assertEqual(200.00, acc.balance)

    def test_withdraw_negative_raises(self):
        acc = BankAccount(40075, 2828, 100.00)
        with self.assertRaises(ValueError):
            acc.withdraw(-20.00)   

    def test_withdraw_exceed_balance_raises(self):
        acc = BankAccount(40075, 2828, 50.00)
        with self.assertRaises(ValueError):
            acc.withdraw(100.00)

    def test_str_returns_expected_format(self):
        acc = BankAccount(40075, 2828, 640.00)
        expected = "Account Number: 40075\nClient Number: 2828\nBalance: $640.00"
        self.assertEqual(expected, str(acc))

   
if __name__ == "__main__":
    unittest.main()

