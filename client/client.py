""" 
Description: This represents banking client with validation for client number, names and email.
Implements Observer interface so instances can receive notifications from BankAccount subjects.
"""

__author__ = "Komalpreet Kaur"
__version__ = "1.0.0"

from email_validator import validate_email, EmailNotValidError
from patterns.observer.observer import Observer
from utility.file_utils import simulate_send_email
from datetime import datetime

class Client(Observer):
    """
    Represents a banking client and acts as an Observer for bank accounts.
    """

    def __init__(self, client_number: int, first_name: str, last_name: str, email_address: str):
        """Initialize a Client with validation.

        Args:
            client_number (int): Unique integer client number.
            first_name (str): Client's first name.
            last_name (str): Client's last name.
            email_address (str): Client's email address.

        Raises:
            ValueError: If client_number, first_name or last_name are invalid.
        """
        if isinstance(client_number, int):
            self.__client_number = client_number
        else:
            raise ValueError("Client number must be an integer.")

        if isinstance(first_name, str) and len(first_name.strip()) > 0:
            self.__first_name = first_name.strip()
        else:
            raise ValueError("First name cannot be blank")

        if isinstance(last_name, str) and len(last_name.strip()) > 0:
            self.__last_name = last_name.strip()
        else:
            raise ValueError("Last name cannot be blank.")

        try:
            validate_email(email_address)
            self.__email_address = email_address
        except EmailNotValidError:
            self.__email_address = "email@pixell-river.com"

    @property
    def client_number(self) -> int:
        """Return the client number."""
        return self.__client_number

    @property
    def first_name(self) -> str:
        """Return the first name."""
        return self.__first_name

    @property
    def last_name(self) -> str:
        """Return the last name."""
        return self.__last_name

    @property
    def email_address(self) -> str:
        """Return the email address."""
        return self.__email_address
    
    def update(self, message: str):
        """
        Receive a notification and produce a simulated email.

        The subject and message formats follow the assignment specification.

        Args:
            message (str): Message describing the event.
        """
        subject = f"ALERT: Unusual Activity: {datetime.now():%Y-%m-%d %H:%M:%S}"
        body = f"Notification for {self.client_number}: {self.first_name} {self.last_name}: {message}"
        simulate_send_email(self.email_address, subject, body)

    def __str__(self) -> str:
        """Return a string representation of the client."""
        return (
            f"Client Number: {self.__client_number}\n"
            f"First Name: {self.__first_name}\n"
            f"Last Name: {self.__last_name}\n"
            f"Email Address: {self.__email_address}"
        )
