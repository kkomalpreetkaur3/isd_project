from abc import ABC, abstractmethod

class Observer(ABC):
    """
    Abstract Observer interface. 
    Concrete observers implement update().

    Methods:
        update(message): Called by Subject to notify the observer.
    """

    @abstractmethod
    def update(self, message: str):
        """
        Handle notification from subject.
        
        Args:
            message (str): formatted message describing the event.
        """
        raise NotImplementedError