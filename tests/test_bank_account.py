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

    def test_valid_account(self):
        acc = BankAccount(40075, 2828, 640.00)
        self.assertEqual(40075, acc._BankAccount__account_number)
        self.assertEqual(2828, acc._BankAccount__client_number)
        self.assertEqual(640.00, acc._BankAccount__balance)

    def test_invalid_account_number_raises(self):
        with self.assertRaises(ValueError):
            BankAccount("invalid", 2828, 640.00)

    def test_invalid_client_number_raises(self):
        with self.assertRaises(ValueError):
            BankAccount(40075, "bad", 640.00)

    def test_invalid_balance_defaults_to_zero(self):
        acc = BankAccount(40075, 2828, "beautiful")
        self.assertEqual(0.0, acc._BankAccount__balance)

    def test_deposit_valid(self):
        acc = BankAccount(40075, 2828, 200.00)
        acc.deposit(50.00)
        self.assertEqual(250.00, round(acc._BankAccount__balance, 2))

    def test_deposit_negative_raises(self):
        acc = BankAccount(40075, 2828, 100.00)
        with self.assertRaises(ValueError):
            acc.deposit(-50.00)
        with self.assertRaises(ValueError):
            acc.deposit("beautiful")

    def test_withdraw_valid(self):
        acc = BankAccount(40075, 2828, 150.00)
        acc.withdraw(40.00)
        self.assertEqual(110.00, round(acc._BankAccount__balance, 2))

    def test_withdraw_negative_raises(self):
        acc = BankAccount(40075, 2828, 110.00)
        with self.assertRaises(ValueError):
            acc.withdraw(-20.00)
        with self.assertRaises(ValueError):
            acc.withdraw("beautiful")

    def test_withdraw_exceed_balance_raises(self):
        acc = BankAccount(40075, 2828, 50.00)
        with self.assertRaises(ValueError):
            acc.withdraw(100.00)

if __name__ == "__main__":
    unittest.main

