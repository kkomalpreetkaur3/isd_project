class Subject:
    """
    Subject base class that maintains and notifies observers.

     Attributes:
        _observers (list): Internal list of attached observers.
    """

    def __init__(self):
        """
        Initialize the Subject with an empty observer list.
        """
        self._observers = []

    def attach(self, observer):
        """
        Attach an observer if it is not already attached.

        Args:
            observer: An object implementing the Observer interface.
        """
        if observer not in self._observers:
            self._observers.append(observer)

    def detach(self, observer):
        """
        Detach an observer if it is currently attached.

        Args:
            observer: The observer to remove.
        """
        if observer in self._observers:
            self._observers.remove(observer)
    
    def notify(self, message: str):
        """
        Notify all attached observers by calling their update method.
        Exceptions from one observer are caught so others still receive notifications.
        Args:
            message (str): A formatted message describing the event.
        """
        for observer in list(self._observers):
            try:
                observer.update(message)
            except Exception:
                pass