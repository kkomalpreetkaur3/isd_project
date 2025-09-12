"""
Description: Unit tests for the Client class.
Author: ACE Faculty
Usage: To execute all tests in the terminal execute 
the following command:
    python -m unittest tests/test_client.py
"""

__author__ = "Komalpreet Kaur"
__version__ = "1.0.0"

import unittest
from client.client import Client

class TestClient(unittest.TestCase):

    def test_init_valid(self):
        # Arrange & Act
        client = Client(2025, "Komal", "Aulakh", "komalaulakh@gmail.com")

        # Assert
        self.assertEqual(2025, client._Client__client_number)
        self.assertEqual("Komal", client._Client__first_name)
        self.assertEqual("Aulakh", client._Client__last_name)
        self.assertEqual("komalaulakh@gmail.com", client._Client__email_address)

    def test_blank_first_name_raises(self):
        with self.assertRaises(ValueError):
            Client(1001, "   ", "Aulakh", "valid@email.com")

    def test_blank_last_name_raises(self):
        with self.assertRaises(ValueError):
            Client(1002, "Komal", "   ", "valid@email.com")       

    def test_invalid_client_number_raises(self):
        with self.assertRaises(ValueError):
            Client("wrong", "Komal", "Aulakh", "valid@gmail.com")

    def test_invalid_email_defaults(self):
        client = Client(2003, "Komal", "Aulakh", "not-an-email")
        self.assertEqual("email@pixell-river.com", client._Client__email_address)

    def test_client_number_property(self):
        client = Client(2025, "Komal", "Aulakh", "komalaulakh@gmail.com")
        self.assertEqual(2025, client.client_number)

    def test_first_name_property(self):
        client = Client(2025, "Komal", "Aulakh", "komalaulakh@gmail.com")
        self.assertEqual("Komal", client.first_name)

    def test_last_name_property(self):
        client = Client(2025, "Komal", "Aulakh", "komalaulakh@gmail.com")
        self.assertEqual("Aulakh", client.last_name)

    def test_email_address_property(self):
        client = Client(2025, "Komal", "Aulakh", "komalaulakh@gmail.com")
        self.assertEqual("komalaulakh@gmail.com", client.email_address)

    def test_str_method(self):
        client = Client(2025, "Komal", "Aulakh", "komalaulakh@gmail.com")
        expected = ("Client Number: 2025\nFirst Name: Komal\nLast Name: Aulakh\n"
                    "Email Address: komalaulakh@gmail.com")
        self.assertEqual(expected, str(client))

if __name__ == "__main__":
    unittest.main()