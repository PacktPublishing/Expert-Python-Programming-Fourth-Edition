import itertools

from blinker import signal


class SelfWatch:
    _new_id = itertools.count(1)

    def __init__(self):
        self._id = next(self._new_id)
        init_signal = signal("SelfWatch.init")
        init_signal.send(self)
        init_signal.connect(self.receiver)

    def receiver(self, sender):
        print(f"{self}: received event from {sender}")

    def __str__(self):
        return f"<{self.__class__.__name__}: {self._id}>"


# >>> from topic_based_events import SelfWatch
# >>> selfwatch1 = SelfWatch()
# >>> selfwatch2 = SelfWatch()
# <SelfWatch: 1>: received event from <SelfWatch: 2>
# >>> selfwatch3 = SelfWatch()
# <SelfWatch: 2>: received event from <SelfWatch: 3>
# <SelfWatch: 1>: received event from <SelfWatch: 3>
# >>> selfwatch4 = SelfWatch()
# <SelfWatch: 2>: received event from <SelfWatch: 4>
# <SelfWatch: 3>: received event from <SelfWatch: 4>
# <SelfWatch: 1>: received event from <SelfWatch: 4>
