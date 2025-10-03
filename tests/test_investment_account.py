"""
Unit tests for InvestmentAccount class.
Follows the Pixell XLSX test plan.
"""

__author__ = "Komalpreet Kaur"
__version__ = "1.0.0"

import unittest
from bank_account.investment_account import InvestmentAccount

class TestInvestmentAccount(unittest.TestCase):
    """Test cases for InvestmentAccount."""

    def test_init_interest_rate(self):
        """Interest rate is set correctly."""
        account = InvestmentAccount(40075, 2828, 1000.00, 0.07)
        self.assertEqual(account.interest_rate, 0.07)

    def test_apply_interest(self):
        """Interest is applied correctly."""
        account = InvestmentAccount(40076, 2828, 1000.00, 0.05)
        account.apply_interest()
        self.assertEqual(account.balance, 1050.00)

    def test_str_method(self):
        """__str__ includes interest rate."""
        account = InvestmentAccount(40077, 2828, 1000.00, 0.05)
        expected = (
            "Account Number: 40077\n"
            "Client Number: 2828\n"
            "Balance: $1000.00\n"
            "Interest Rate: 5.00%"
        )
        self.assertEqual(str(account), expected)

if __name__ == "__main__":
    unittest.main()