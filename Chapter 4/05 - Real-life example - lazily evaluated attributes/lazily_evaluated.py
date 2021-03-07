import random


class InitOnAccess:
    def __init__(self, init_func, *args, **kwargs):
        self.klass = init_func
        self.args = args
        self.kwargs = kwargs
        self._initialized = None

    def __get__(self, instance, owner):
        if self._initialized is None:
            print("initialized!")
            self._initialized = self.klass(*self.args, **self.kwargs)
        else:
            print("cached!")
        return self._initialized


class WithSortedRandoms:
    lazily_initialized = InitOnAccess(sorted, [random.random() for _ in range(5)])


if __name__ == "__main__":
    m = WithSortedRandoms()
    print(m.lazily_initialized)
    print(m.lazily_initialized)
