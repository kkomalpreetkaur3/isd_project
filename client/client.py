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
        return self.__client_number

    @property
    def first_name(self) -> str:
        return self.__first_name

    @property
    def last_name(self) -> str:
        return self.__last_name

    @property
    def email_address(self) -> str:
        return self.__email_address
    
    def update(self, message: str):
        """
        Observer.update implementation.
        Writes a simulated email using simulate_send_email().
        
        Subject format: ALERT: Unusual Activity: {current date/time}
        Message format: Notification for {client number}: {first name} {last name}: {message}
        """
        subject = f"ALERT: Unusual Activity: {datetime.now():%Y-%m-%d %H:%M:%S}"
        body = f"Notification for {self.client_number}: {self.first_name} {self.last_name}: {message}"
        simulate_send_email(self.email_address, subject, body)

    def __str__(self) -> str:
        return (
            f"Client Number: {self.__client_number}\n"
            f"First Name: {self.__first_name}\n"
            f"Last Name: {self.__last_name}\n"
            f"Email Address: {self.__email_address}"
        )
