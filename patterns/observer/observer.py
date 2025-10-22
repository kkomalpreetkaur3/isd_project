from abc import ABC, abstractmethod

class Observer(ABC):
    """Abstract Observer interface. Concrete observers implement update()."""

    @abstractmethod
    def update(self, message: str):
        """
        Handle notification from subject.
        
        Args:
            message: formatted message describing the event.
        """
        raise NotImplementedError