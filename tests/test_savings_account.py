"""
Unit tests for SavingsAccount class.
Follows the Pixell XLSX test plan.
"""

__author__ = "Komalpreet Kaur"
__version__ = "1.0.0"

import unittest
from datetime import date
from bank_account.savings_account import SavingsAccount

class TestSavingsAccount(unittest.TestCase):
    """Test cases for SavingsAccount."""

    def test_init_attributes(self):
        """Attributes are correctly set."""
        account = SavingsAccount(30075, 0, 500.00, date.today(), 0.05, 50.00)
        self.assertEqual(account.balance, 500.0)
        self.assertEqual(account.minimum_balance, 50.0)

    def test_service_charges_above_minimum(self):
        """Balance above minimum returns base charge."""
        account = SavingsAccount(30076, 0, 100.00, date.today(), 0.05, 50.00)
        self.assertEqual(account.get_service_charges(), 0.50)

    def test_service_charges_below_minimum(self):
        """Balance below minimum returns double charge."""
        account = SavingsAccount(30077, 0, 49.00, date.today(), 0.05, 50.00)
        self.assertEqual(account.get_service_charges(), 1.0)

    def test_str_method(self):
        """__str__ includes creation date and minimum balance."""
        today = date.today()
        account = SavingsAccount(30078, 0, 100.00, date.today(), 0.05, 50.00)
        
        expected = (
            f"Account Number: 30078\n"
            f"Client Number: 0\n"
            f"Balance: $100.00\n"
            f"Creation Date: {today}\n"
            f"Minimum Balance: $50.00"
        )
        self.assertEqual(str(account), expected)

if __name__ == "__main__":
    unittest.main()