from abc import ABC, abstractmethod

class ServiceChargeStrategy(ABC):
    """
    Abstract base for all service charge strategies.

    BASE_SERVICE_CHARGE constant moved here (previously in BankAccount).
    Concrete strategies implement calculate_service_charges(account) and return
    a float representing the charge amount (>= 0).
    """
    BASE_SERVICE_CHARGE = 2.50

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