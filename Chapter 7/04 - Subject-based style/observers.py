import os
import sys
import re
from abc import ABC, abstractmethod
from glob import glob


class ObserverABC(ABC):
    @abstractmethod
    def notify(self, event):
        ...


class SubjectABC(ABC):
    @abstractmethod
    def register(self, observer: ObserverABC):
        ...


class Grepper(SubjectABC):
    _observers: list[ObserverABC]

    def __init__(self):
        self._observers = []

    def register(self, observer: ObserverABC):
        self._observers.append(observer)

    def notify_observers(self, path):
        for observer in self._observers:
            observer.notify(path)

    def grep(self, path: str, pattern: str):
        r = re.compile(pattern)

        for item in glob(path, recursive=True):
            if not os.path.isfile(item):
                continue

            try:
                with open(item) as f:
                    self.notify_observers(("opened", item))
                    if r.findall(f.read()):
                        self.notify_observers(("matched", item))
            finally:
                self.notify_observers(("closed", item))


class Presenter(ObserverABC):
    def notify(self, event):
        event_type, file = event
        if event_type == "matched":
            print(f"Found in: {file}")


class Auditor(ObserverABC):
    def notify(self, event):
        event_type, file = event
        print(f"{event_type:8}: {file}")


if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("usage: program PATH PATTERN")
        sys.exit(1)

    grepper = Grepper()
    grepper.register(Presenter())
    grepper.grep(sys.argv[1], sys.argv[2])


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
