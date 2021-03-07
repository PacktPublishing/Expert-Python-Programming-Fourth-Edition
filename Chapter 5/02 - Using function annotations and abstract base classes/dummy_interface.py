from abc import ABC, abstractmethod


class DummyInterface(ABC):
    @abstractmethod
    def dummy_method(self):
        ...

    @property
    @abstractmethod
    def dummy_property(self):
        ...


class InvalidDummy(DummyInterface):
    pass


class MissingPropertyDummy(DummyInterface):
    def dummy_method(self):
        pass


class MissingMethodDummy(DummyInterface):
    @property
    def dummy_property(self):
        return None


class Dummy(DummyInterface):
    def dummy_method(self):
        pass

    @property
    def dummy_property(self):
        return None


def intantiate(cls):
    print("instantiating", cls)
    try:
        cls()
    except Exception as err:
        print(" -", type(err), err)
    else:
        print(" - ok")


if __name__ == "__main__":
    intantiate(DummyInterface)
    intantiate(InvalidDummy)
    intantiate(MissingMethodDummy)
    intantiate(MissingPropertyDummy)
    intantiate(Dummy)
