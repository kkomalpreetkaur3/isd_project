""" 
Description: This represents banking client with validation for client number, names and email.
"""

__author__ = "Komalpreet Kaur"
__version__ = "1.0.0"

class Client:
    """Represents a banking client."""
    
from email_validator import validate_email, EmailNotValidError
    
def __init__(self, client_number: int, first_name: str, last_name: str, email_address: str):
        
    if isinstance(client_number, int):
        self.__client_number = client_number
    else:
        raise ValueError("Client number must be an integer.")

    if len(first_name.strip()) > 0:
        self.__first_name = first_name
    else:
        raise ValueError("First name cannot be blank.")

    if len(last_name.strip()) > 0:
        self.__last_name = last_name
    else:
        raise ValueError("Last name cannot be blank.")

    try:
        validate_email(email_address)
        self.__email_address = email_address
    except EmailNotValidError:
        raise ValueError("Invalid email address provided.")

    
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
    
    def __str__(self) -> str:
        return (
            f"Client Number: {self.__client_number}"
            f"\nFirst Name: {self.__first_name}"
            f"\nLast Name: {self.__last_name}"
            f"\nEmail Address: {self.__email_address}"
        )

    


    
