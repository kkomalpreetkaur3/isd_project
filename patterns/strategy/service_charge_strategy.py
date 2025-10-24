from abc import ABC, abstractmethod

class ServiceChargeStrategy(ABC):
    """
    Abstract base for all service charge strategies.

    Attributes:
        BASE_SERVICE_CHARGE (float): A base service charge shared by strategies.
    """
    BASE_SERVICE_CHARGE = 0.50

    @abstractmethod
    def calculate_service_charges(self, account) -> float:
        """
        Calculate service charges for the provided account.
        
        Args:
            account: instance of a BankAccount subclass with at least 'balance' and 'account_number' attributes.
            
        Returns:
            float: service charge amount (>= 0)
        """
        raise NotImplementedError