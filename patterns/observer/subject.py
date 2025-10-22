class Subject:
    """Subject base class that maintains and notifies observers."""

    def __init__(self):
        self._observers = []

    def attach(self, observer):
        if observer not in self._observers:
            self._observers.append(observer)

    def detach(self, observer):
        if observer in self._observers:
            self._observers.remove(observer)
    
    def notify(self, message: str):
        for obs in list(self._observers):
            try:
                obs.update(message)
            except Exception:
                pass