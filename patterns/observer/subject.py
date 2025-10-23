class Subject:
    """
    Subject base class that maintains and notifies observers.
    """

    def __init__(self):
        self._observers = []

    def attach(self, observer):
        """
        Attach an observer if it is not already attached.
        """
        if observer not in self._observers:
            self._observers.append(observer)

    def detach(self, observer):
        """
        Detach an observer if it is currently attached.
        """
        if observer in self._observers:
            self._observers.remove(observer)
    
    def notify(self, message: str):
        """
        Notify all attached observers by calling their update method.
        Exceptions from one observer are caught so others still receive notifications.
        """
        for observer in list(self._observers):
            try:
                observer.update(message)
            except Exception:
                pass