"""
Unit tests for ChequingAccount class.
Follows the Pixell XLSX test plan.
"""

__author__ = "Komalpreet Kaur"
__version__ = "1.0.0"

import unittest
from chequing_account.chequing_account import ChequingAccount

class TestChequingAccount(unittest.TestCase):
    """Test cases for ChequingAccount."""

    def test_init_minimum_balance(self):
        """Minimum balance is set correctly."""
        account = ChequingAccount(40075, 2828, 640.00, 150.00)
        self.assertEqual(account.minimum_balance, 150.0)

    def test_service_charges_above_minimum(self):
        """Balance above minimum returns base service charge."""
        account = ChequingAccount(40076, 2828, 200.00, 100.00)
        self.assertEqual(account.get_service_charges(), 0.50)

    def test_service_charges_below_minimum(self):
        """Balance below minimum returns double service charge."""
        account = ChequingAccount(40077, 2828, 50.00, 100.00)
        self.assertEqual(account.get_service_charges(), 1.0)

    def test_str_method(self):
        """__str__ includes minimum balance info."""
        account = ChequingAccount(40078, 2828, 200.00, 100.00)
        expected = (
            "Account Number: 40078\n"
            "Client Number: 2828\n"
            "Minimum Balance: !00.00"
        )
        self.assertEqual(str(account), expected)