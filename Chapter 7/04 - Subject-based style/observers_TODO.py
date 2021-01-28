import itertools


class Subject:
    _new_id = itertools.count(1)

    def __init__(self):
        self._id = next(self._new_id)
        self._observers = []

    def register(self, observer):
        self._notify_observers(f"register({observer})")
        self._observers.append(observer)

    def _notify_observers(self, event):
        for observer in self._observers:
            observer.notify(self, event)

    def __str__(self):
        return f"<{self.__class__.__name__}: {self._id}>"


class Observer:
    _new_id = itertools.count(1)

    def __init__(self):
        self._id = next(self._new_id)

    def notify(self, subject, event):
        print(f"{self}: received event '{event}' from {subject}")

    def __str__(self):
        return f"<{self.__class__.__name__}: {self._id}>"

# >>> from subject_based_events import Subject
# >>> subject = Subject()
# >>> observer1 = Observer()
# >>> observer2 = Observer()
# >>> observer3 = Observer()
# >>> subject.register(observer1)
# >>> subject.register(observer2)
# <Observer: 1>: received event 'register(<Observer: 2>)' from <Subject: 1>
# >>> subject.register(observer3)
# <Observer: 1>: received event 'register(<Observer: 3>)' from <Subject: 1>
# <Observer: 2>: received event 'register(<Observer: 3>)' from <Subject: 1>
