import random


class lazy_property(object):
    def __init__(self, function):
        self.fget = function

    def __get__(self, obj, cls):
        value = self.fget(obj)
        setattr(obj, self.fget.__name__, value)
        return value


class WithSortedRandoms:
    @lazy_property
    def lazily_initialized(self):
        return sorted([[random.random() for _ in range(5)]])


if __name__ == "__main__":
    m = WithSortedRandoms()
    print(m.lazily_initialized)
    print(m.lazily_initialized)
